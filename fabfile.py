# encoding: utf-8
from fabric.api import *
from fabric.colors import green
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

def service(service,op):
    sudo("service {service} {op}".format(service=service, op=op))

def create_project_structure():
    print(green("Creating directory structure in %s" % PROJECT_PATH))
    sudo("mkdir -p {project_path}".format(project_path=PROJECT_PATH))
    with cd(PROJECT_PATH):
        sudo("mkdir -p conf src logs releases")

def install_packages():
    f = open('./deploy/packages.txt')
    list_packages = ' '.join(f.read().split('\n'))
    sudo("apt-get install {list_packages}".format(list_packages=list_packages))

def install_virtualenv():
    with cd(PROJECT_PATH):
        sudo("mkdir -p virtualenv")
        sudo("virtualenv ./virtualenv")

def configure_nginx():
    put("deploy/{env}/conf/nginx.conf".format(env=env.name), "/tmp/nginx.conf")
    sudo("mv /tmp/nginx.conf {project_path}/conf/nginx.conf".format(project_path=PROJECT_PATH))

    sudo("rm -rf /etc/nginx/nginx.conf")
    sudo("ln -s {project_path}/conf/nginx.conf /etc/nginx/nginx.conf".format(project_path=PROJECT_PATH))
    sudo("service nginx stop")
    sudo("service nginx start")

def configure_uwsgi():
    put("deploy/{env}/conf/uwsgi.ini".format(env=env.name), "/tmp/uwsgi-conf.ini")
    sudo("mv /tmp/uwsgi-conf.ini {project_path}/conf/uwsgi.ini".format(project_path=PROJECT_PATH))

    put("deploy/init/uwsgi.ini", "/tmp/uwsgi.ini")
    sudo("mv /tmp/uwsgi.ini /etc/init/")

def configure_locale():
    run("export LANGUAGE=en_US.UTF-8")
    run("export LANG=en_US.UTF-8")
    run("export LC_ALL=en_US.UTF-8")
    run("locale-gen en_US.UTF-8")
    sudo("dpkg-reconfigure locales")

def initial_mysql_configuration():
    query = 'CREATE USER "{user}"@"localhost" IDENTIFIED BY "{password}";'.format(user=MYSQL_USER, password=MYSQL_PASSWORD)
    query += 'GRANT ALL ON {db}.* TO "{user}"@"%";'.format(db=MYSQL_DB, user=MYSQL_USER)
    query += 'CREATE DATABASE IF NOT EXISTS {db} DEFAULT CHARACTER SET utf8;'.format(db=MYSQL_DB)
    run("mysql -u root -p{root_password} -e '{query}'".format(query=query, root_password=MYSQL_ROOT_PASSWORD))

def initial_setup():
    create_project_structure()
    sudo("echo \"localhost\" > /etc/hostname")
    sudo("hostname localhost")
    sudo("apt-get update")
    sudo("apt-get upgrade")
    configure_locale()
    upload()
    install_packages()
    install_virtualenv()
    configure_nginx()
    initial_mysql_configuration()

    sudo("reboot")

def upload(site='dashboard'):

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
