# encoding: utf-8
import os
import sys
from fabric.api import *
from fabric.colors import green
from fabric.contrib.files import exists
from datetime import datetime

MYSQL_ROOT_PASSWORD = '#SM2015Dashboard*'


def prod():
    env.hosts = ['66.228.41.76']
    env.name = 'prod'
    env.WEBHOST = 'sm2015dashboard.org'
    env.PROJECT_PATH = '/var/www/{host_name}'.format(host_name=env.WEBHOST)
    env.MYSQL_USER = 'sm2015_dashboard'
    env.MYSQL_PASSWORD = '$Sm2015_dashboarD$'
    env.MYSQL_DB = 'sm2015_dashboard'


def homolog():
    env.hosts = ['66.228.41.76']
    env.name = 'homolog'
    env.WEBHOST = 'homolog.sm2015dashboard.org'
    env.PROJECT_PATH = '/var/www/{host_name}'.format(host_name=env.WEBHOST)
    env.MYSQL_USER = 'sm2015_homolog'
    env.MYSQL_PASSWORD = '$Sm2015_dashboarD$HomoloG'
    env.MYSQL_DB = 'sm2015_dashboard_homolog'


def initial_setup(site='dashboard'):
    create_project_structure()
    sudo("echo \"localhost\" > /etc/hostname")
    sudo("hostname localhost")
    sudo("apt-get update")
    sudo("apt-get upgrade")
    install_packages()
    create_virtualenv()
    install_requirements()
    server_configuration()
    initial_mysql_configuration()
    deploy(site)

    sudo("reboot")


def server_configuration():
    configure_locale()
    configure_nginx()
    configure_uwsgi()


def deploy(site='dashboard'):
    upload(site)
    install_requirements()
    migrate(site)
    collect_static(site)

    service("nginx", "stop")
    service("nginx", "start")
    restart_uwsgi()


def service(service, op):
    sudo("service {service} {op}".format(service=service, op=op))


def create_project_structure():
    print(green("Creating directory structure in %s" % env.PROJECT_PATH))
    run("mkdir -p {project_path}".format(project_path=env.PROJECT_PATH))
    with cd(env.PROJECT_PATH):
        run("mkdir -p conf src logs/nginx logs/app logs/uwsgi releases run")

    sudo("mkdir -p /static/{env}/{host_name} /media/{env}/{host_name}".format(env=env.name,
                                                                              host_name=env.WEBHOST))


def install_packages():
    f = open('./deploy/packages.txt')
    list_packages = ' '.join(f.read().split('\n'))
    sudo("apt-get install {list_packages}".format(list_packages=list_packages))


def create_virtualenv():
    with cd(env.PROJECT_PATH):
        if not exists("virtualenv"):
            run("mkdir -p virtualenv")
            run("virtualenv ./virtualenv")


def configure_nginx():
    put("deploy/{env}/conf/nginx.conf".format(env=env.name), "/tmp/nginx.conf")
    sudo("mv /tmp/nginx.conf {project_path}/conf/nginx.conf".format(project_path=env.PROJECT_PATH))

    sudo("rm -f /etc/nginx/sites-enabled/dashboard_{env}.conf".format(env=env.name))
    sudo("ln -s {project_path}/conf/nginx.conf /etc/nginx/sites-enabled/dashboard_{env}.conf".format(project_path=env.PROJECT_PATH, env=env.name))
    service("nginx", "stop")
    service("nginx", "start")


def configure_uwsgi():
    put("deploy/{env}/conf/uwsgi.conf".format(env=env.name), "/tmp/uwsgi_{env}.conf".format(env=env.name))
    sudo("mv /tmp/uwsgi_{env}.conf /etc/init/".format(env=env.name))
    restart_uwsgi()


def restart_uwsgi():
    sudo("{project_path}/virtualenv/bin/uwsgi --reload {project_path}/run/uwsgi.pid".format(project_path=env.PROJECT_PATH))


def configure_locale():
    run("export LANGUAGE=en_US.UTF-8")
    run("export LANG=en_US.UTF-8")
    run("export LC_ALL=en_US.UTF-8")
    run("locale-gen en_US.UTF-8")
    sudo("dpkg-reconfigure locales")


def initial_mysql_configuration():
    query = 'GRANT ALL ON {db}.* TO "{user}"@"%" IDENTIFIED BY "{password}";'.format(db=env.MYSQL_DB, user=env.MYSQL_USER, password=env.MYSQL_PASSWORD)
    query += 'CREATE DATABASE IF NOT EXISTS {db} DEFAULT CHARACTER SET utf8;'.format(db=env.MYSQL_DB)
    run("mysql -u root -p{root_password} -e '{query}'".format(query=query, root_password=MYSQL_ROOT_PASSWORD))


def install_requirements():
    print(green("Installing requirements"))

    requirements_path = os.path.join('requirements.txt')
    with cd(env.PROJECT_PATH):
        for line in open(requirements_path):
            package = line.replace("\n", "")
            run('virtualenv/bin/pip install {package}'.format(package=package), shell=False)


def upload(site):

    print(green("Deploying site %s" % site))

    # upload site
    local("git archive --format=tar --prefix={site}/ HEAD:{path}/ | gzip > /tmp/{site}.tgz".format(site=site, path=site))
    put("/tmp/{site}.tgz".format(site=site), "/tmp/")
    run("tar -C /tmp -xzf /tmp/{site}.tgz".format(site=site))
    run("rm -rf {project_path}/src/{site}".format(site=site, project_path=env.PROJECT_PATH))
    run("mv /tmp/{site} {project_path}/src/".format(site=site, project_path=env.PROJECT_PATH))
    run("rm /tmp/{site}.tgz".format(site=site))
    local("rm /tmp/{site}.tgz".format(site=site))

    with cd("{project_path}/src/{site}/core/".format(site=site, project_path=env.PROJECT_PATH)):
        run("mv settings_{env}.py settings_wsgi.py".format(env=env.name))


def _is_valid_app(app_name):
    try:
        exec("from %s import migrations" % app_name)
    except ImportError:
        return False
    return True


def migrate(site):
    sys.path.append(os.path.join(os.getcwd(), 'dashboard'))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

    mod = __import__('core', globals(), locals(), ['settings'], -1)
    settings = mod.settings

    with cd("{project_path}/src/{site}".format(project_path=env.PROJECT_PATH, site=site)):
        run('{project_path}/virtualenv/bin/python manage.py syncdb --settings=core.settings_wsgi'.format(project_path=env.PROJECT_PATH))

        for app in settings.INSTALLED_APPS:
            if _is_valid_app(app):
                print(green("Migrate app {app}".format(app=app)))
                run('{project_path}/virtualenv/bin/python manage.py migrate {app} --settings=core.settings_wsgi' \
                    .format(app=app, project_path=env.PROJECT_PATH))


def collect_static(site):
    with cd("{project_path}/src/{site}".format(project_path=env.PROJECT_PATH, site=site)):
        run('{project_path}/virtualenv/bin/python manage.py collectstatic --noinput --settings=core.settings_wsgi' \
            .format(project_path=env.PROJECT_PATH))


def run_command(site, command, *args):
    comando = "{command} {args}".format(command=command, args=" ".join(args))

    print(green("Running command: python manage.py {comando} --settings=core.settings_wsgi" \
            .format(comando=comando)))

    with cd("{project_path}/src/{site}".format(project_path=env.PROJECT_PATH, site=site)):
        run('{project_path}/virtualenv/bin/python manage.py {comando} --settings=core.settings_wsgi' \
            .format(project_path=env.PROJECT_PATH, comando=comando))
