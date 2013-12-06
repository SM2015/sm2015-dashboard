# encoding: utf-8
import os
import sys
from fabric.api import *
from fabric.colors import green
from fabric.contrib.files import exists
from datetime import datetime

PROJECT_PATH = '/var/www/sm2015dashboard.org'

MYSQL_USER = 'sm2015_dashboard'
MYSQL_PASSWORD = '$Sm2015_dashboarD$'
MYSQL_DB = 'sm2015_dashboard'
MYSQL_ROOT_PASSWORD = '#SM2015Dashboard*'

def prod():
    env.hosts = ['66.228.41.76']
    env.user = 'rafaelsantos'
    env.name = 'prod'

def initial_setup(site='dashboard'):
    create_project_structure()
    sudo("echo \"localhost\" > /etc/hostname")
    sudo("hostname localhost")
    sudo("apt-get update")
    sudo("apt-get upgrade")
    install_packages()
    create_virtualenv()
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

def service(service,op):
    sudo("service {service} {op}".format(service=service, op=op))

def create_project_structure():
    print(green("Creating directory structure in %s" % PROJECT_PATH))
    sudo("mkdir -p {project_path}".format(project_path=PROJECT_PATH))
    with cd(PROJECT_PATH):
        sudo("mkdir -p conf src logs releases")

    sudo("mkdir -p /static /media")

def install_packages():
    f = open('./deploy/packages.txt')
    list_packages = ' '.join(f.read().split('\n'))
    sudo("apt-get install {list_packages}".format(list_packages=list_packages))

def create_virtualenv():
    with cd(PROJECT_PATH):
        if not exists("virtualenv"):
            sudo("mkdir -p virtualenv")
            sudo("virtualenv ./virtualenv")

def configure_nginx():
    put("deploy/{env}/conf/nginx.conf".format(env=env.name), "/tmp/nginx.conf")
    sudo("mv /tmp/nginx.conf {project_path}/conf/nginx.conf".format(project_path=PROJECT_PATH))

    sudo("ln -s {project_path}/conf/nginx.conf /etc/nginx/sites-enabled/dashboard.conf".format(project_path=PROJECT_PATH))
    sudo("service nginx stop")
    sudo("service nginx start")

def configure_uwsgi():
    put("deploy/{env}/conf/uwsgi.ini".format(env=env.name), "/tmp/uwsgi-conf.ini")
    sudo("mv /tmp/uwsgi-conf.ini {project_path}/conf/uwsgi.ini".format(project_path=PROJECT_PATH))

    put("deploy/{env}/conf/uwsgi_params.conf".format(env=env.name), "/tmp/uwsgi_params.conf")
    sudo("mv /tmp/uwsgi_params.conf {project_path}/conf/uwsgi_params.conf".format(project_path=PROJECT_PATH))

    put("deploy/init/uwsgi.conf", "/tmp/uwsgi.conf")
    sudo("mv /tmp/uwsgi.conf /etc/init/")
    sudo("/etc/init.d/uwsgi stop")
    sudo("/etc/init.d/uwsgi start")


def configure_locale():
    run("export LANGUAGE=en_US.UTF-8")
    run("export LANG=en_US.UTF-8")
    run("export LC_ALL=en_US.UTF-8")
    run("locale-gen en_US.UTF-8")
    sudo("dpkg-reconfigure locales")

def initial_mysql_configuration():
    query = 'GRANT ALL ON {db}.* TO "{user}"@"%" IDENTIFIED BY "{password}";'.format(db=MYSQL_DB, user=MYSQL_USER, password=MYSQL_PASSWORD)
    query += 'CREATE DATABASE IF NOT EXISTS {db} DEFAULT CHARACTER SET utf8;'.format(db=MYSQL_DB)
    run("mysql -u root -p{root_password} -e '{query}'".format(query=query, root_password=MYSQL_ROOT_PASSWORD))

def install_requirements():
    print(green("Installing requirements"))

    requirements_path = os.path.join('requirements.txt')
    with cd(PROJECT_PATH):
        for line in open(requirements_path):
            package = line.replace("\n", "")
            run('virtualenv/bin/pip install {package}'.format(package=package), shell=False)

def upload(site):

    print(green("Deploying site %s" % site))

    # Generate package file
    today = datetime.now().strftime('%Y%m%d-%H%M%S')
    commit_id = str(local('git rev-parse HEAD', True)).strip()
    current = "%s-%s" % (today, commit_id[:8])
    
    # upload site
    local("git archive --format=tar --prefix={site}/ HEAD:{path}/ | gzip > /tmp/{site}.tgz".format(site=site, path=site))
    put("/tmp/{site}.tgz".format(site=site), "/tmp/")
    run("tar -C /tmp -xzf /tmp/{site}.tgz".format(site=site))
    sudo("rm -rf {project_path}/src/{site}".format(site=site, project_path=PROJECT_PATH))
    sudo("mv /tmp/{site} {project_path}/src/".format(site=site, project_path=PROJECT_PATH))
    run("rm /tmp/{site}.tgz".format(site=site)) 
    local("rm /tmp/{site}.tgz".format(site=site))

    with cd("{project_path}/src/{site}/core/".format(site=site, project_path=PROJECT_PATH)):
        run("mv settings_prod.py settings_wsgi.py")

def _is_valid_app(app_name):
    try:
        exec("from %s import migrations" % app_name)
    except ImportError:
        return False        
    return True

def migrate(site):
    sys.path.append(os.path.join(os.getcwd(), 'dashboard'))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings_prod")

    mod = __import__('core', globals(), locals(), ['settings'], -1)
    settings = mod.settings

    with cd("{project_path}/src/{site}".format(project_path=PROJECT_PATH, site=site)):
        for app in settings.INSTALLED_APPS:
            if _is_valid_app(app):
                print(green("Migrate app {app}".format(app=app)))
                run('{project_path}/virtualenv/bin/python manage.py migrate {app} --settings=core.settings_wsgi' \
                    .format(app=app, project_path=PROJECT_PATH))

def collect_static(site):
    with cd("{project_path}/src/{site}".format(project_path=PROJECT_PATH, site=site)):
        sudo('{project_path}/virtualenv/bin/python manage.py collectstatic --noinput --settings=core.settings_wsgi' \
            .format(project_path=PROJECT_PATH))
