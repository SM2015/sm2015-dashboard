# encoding: utf-8
from fabric.api import *
from fabric.colors import green
from datetime import datetime

INSTALL_PREFIX = '/data'
PROJECT_PATH = '{prefix}/sites/dashboard'.format(prefix=INSTALL_PREFIX)
PYTHON_DOWNLOAD_URL = 'http://www.python.org/ftp/python/2.7.5/Python-2.7.5.tgz'

def prod():
    env.hosts = ['66.228.41.76']
    env.user = 'rafaelsantos'
    env.name = 'prod'

def setup():
    install_nginx_conf()

def upload(site):
    
    print(green("Deploying site %s" % site))

    # Generate package file
    today = datetime.now().strftime('%Y%m%d-%H%M%S')
    commit_id = str(local('git rev-parse HEAD', True)).strip()
    current = "%s-%s" % (today, commit_id[:8])
    
    local("git archive --format=tar --prefix={site}/ HEAD:{path}/ | gzip > /tmp/{site}.tgz".format(site=site, path=site))
    put("/tmp/{site}.tgz".format(site=site), "/tmp/")
    run("tar -C /tmp -xzf /tmp/{site}.tgz".format(site=site))

    sudo("mv /tmp/{site} {project_path}/ ".format(site=site, project_path=PROJECT_PATH))
    run("rm /tmp/{site}.tgz".format(site=site))
    local("rm /tmp/{site}.tgz".format(site=site))


def create_project_structure():
    print(green("Creating directory structure in %s" % INSTALL_PREFIX))
    
    sudo('mkdir -p {prefix}'.format(prefix=INSTALL_PREFIX))
    sudo('chown %s. %s' % (env.user, INSTALL_PREFIX))
    sudo('mkdir -p %s' % INSTALL_PREFIX)
    sudo('mkdir -p /cache')
    sudo('mkdir -p /static')

def run_command(site, command, database=''):
    """executa um comando, :site,command"""

    with cd("{prefix}/sites/{site}/{site}".format(prefix=INSTALL_PREFIX, site=site)):

        return run("sudo PATH={prefix}/sites/{site}/virtualenv:$PATH PYTHONPATH='{prefix}/sites/{site}:$PYTHONPATH' {prefix}/sites/{site}/virtualenv/bin/python manage.py {command} --settings=settings_wsgi {database}"\
            .format(site=site, prefix=INSTALL_PREFIX, command=command, database='--database='+database if database else ''))

def migrate(site):
    """executa a migração do site, :site"""

    mod = __import__(site, globals(), locals(), ['settings'], -1)
    settings = mod.settings

    for app in settings.INSTALLED_APPS:
        if _is_valid_app(app):
            database = settings.CUSTOM_APP_DATABASE.get(app, 'default') if hasattr(settings, 'CUSTOM_APP_DATABASE') else 'default'

            print(green("Migrate app %s in db '%s'" % (app, database)))
            migrate_list = run_command(site, 'migrate %s --list' % app, database)
            migrates_to_run = False
            
            for line in migrate_list.splitlines()[1:]:
                if re.match("^\s+\([^\*]\).*$", line):
                    migrates_to_run = True
                    break
            
            if not migrates_to_run:
                print(green("Nothing to do."))
                continue
                
            if confirm("Deseja executar as migracoes acima?", False):
                run_command(site, 'migrate '+app, database)

def install_nginx_conf():
    """Atualiza as configurações do nginx"""

    print(green("Installing nginx conf"))
    put('deploy/{env}/nginx.conf'.format(env=env.name), '/tmp/nginx.conf')
    sudo('mv /tmp/nginx.conf %s/nginx/conf/nginx.conf' % INSTALL_PREFIX)
