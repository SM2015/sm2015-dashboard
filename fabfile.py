# encoding: utf-8
from fabric.api import *
from fabric.colors import green
from datetime import datetime

PROJECT_PATH = '/var/www/sm2015dashboard.org'

def prod():
    env.hosts = ['66.228.41.76']
    env.user = 'rafaelsantos'
    env.name = 'prod'

def create_project_structure():
    print(green("Creating directory structure in %s" % PROJECT_PATH))
    sudo("mkdir -p {project_path}".format(project_path=PROJECT_PATH))
    with cd(PROJECT_PATH):
        sudo("mkdir conf src logs")

def install_packages():
    f = open('./deploy/packages.txt')
    list_packages = ' '.join(f.read().split('\n'))
    sudo("apt-get install {list_packages}".format(list_packages=list_packages))

def install_virtualenv():
    with cd(PROJECT_PATH):
        sudo("mkdir virtualenv")
        sudo("virtualenv ./virtualenv")

def configure_nginx():
    sudo("mv /etc/nginx/nginx.conf /etc/nginx/nginx.conf-initial-bkp")
    sudo("ln -s {project_path}/conf/nginx.conf /etc/nginx/nginx.conf")
    sudo("service nginx stop")
    sudo("service nginx start")

def configure_uwsgi():
    put("deploy/{env}/conf/uwsgi.ini", "/tmp/uwsgi.ini")
    sudo("mv /tmp/uwsgi.ini {project_path}/conf/".format(project_path=PROJECT_PATH))

    put("deploy/init/uwsgi.ini", "/tmp/uwsgi.ini")
    sudo("mv /tmp/uwsgi.ini /etc/init/")

def initial_setup():
    create_project_structure()
    upload()
    sudo("echo \"localhost\" > /etc/hostname")
    sudo("hostname localhost")
    sudo("apt-get update")
    sudo("apt-get upgrade")
    install_packages()
    install_virtualenv()
    configure_nginx()
    sudo("reboot")

def upload():
    print(green("Deploying site %s" % site))

    site = 'dashboard'

    # Generate package file
    today = datetime.now().strftime('%Y%m%d-%H%M%S')
    commit_id = str(local('git rev-parse HEAD', True)).strip()
    current = "%s-%s" % (today, commit_id[:8])
    
    local("git archive --format=tar --prefix={site}/ HEAD:{path}/ | gzip > /tmp/{site}.tgz".format(site=site, path=site))
    put("/tmp/{site}.tgz".format(site=site), "/tmp/")
    run("tar -C /tmp -xzf /tmp/{site}.tgz".format(site=site))

    sudo("mv /tmp/{site} {project_path}/src/ ".format(site=site, project_path=PROJECT_PATH))
    run("rm /tmp/{site}.tgz".format(site=site))
    local("rm /tmp/{site}.tgz".format(site=site))
