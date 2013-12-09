SM2015 - Dashboard
=========================

### Install Requirements

 * Python >= 2.7.4
 * Virtualenv >= 1.10
 * Mysql >= 5.6
 * Git >= 1.8

### Running the Project

    Install all the requirements above. After that, follow the 
    instructions bellow:

    1. Create a virtualenv for the project:
        $ mkdir -p ~/.Virtualenv/ && cd ~/.Virtualenv/
        $ virtualenv sm2015 --no-site-packages
        $ source sm2015/bin/activate

    2. Create a Workspace (or use the onde that you already have):
        $ mkdir -p ~/Workspace/
        
    3. Clone project from GitHub:
        $ cd ~/Workspace && git clone git@github.com:CreativeWorksAg/sm2015-dashboard.git

    4. Install all the project's requirements:
        $ cd ~/Workspace/sm2015-dashboard
        $ pip install -r requirements_dev.txt

    5. Configuring database:
        $ mysql -u root -p -e 'CREATE DATABASE sm2015_dashboard;'
        $ cd dashboard && python manage.py syncdb
        >>> NOTE: Type 'yes' for the first answer. Then, Django will ask you about a username, 
        password and email. These are datas that you are going to use on your local enviroment
        to access Django CMS. You can put whatever you want.
        $ python manage.py migrate

    6. Running:
        $ python manage.py runserver
        >>> Now you can access on your browser: http://localhost:8000/admin

    * After doing all these steps, for the next time you just need
    activate you virtualenv and run the project:
        >>> source ~/.Virtualenv/sm2015/bin/activate
        >>> cd ~/Workspace/sm2015-dashboard/dashboard && python manage.py runserver

### Deploy Script
    
    1. Activate your virtualenv:
        $ source ~/.Virtualenv/sm2015/bin/activate

    2. Deploying:
        $ cd ~/Workspace/sm2015-dashboard/
        $ fab prod deploy:dashboard --user [server_username]

    3. Update Server Configurations:
        $ cd ~/Workspace/sm2015-dashboard/
        $ fab prod server_configuration --user [server_username]

    4. Initial Configuration for Server (Rebuild all server configuration and installation):
        $ cd ~/Workspace/sm2015-dashboard/
        $ fab prod initial_setup:dashboard --user [server_username]

    5. Run "service" command on server:
        $ cd ~/Workspace/sm2015-dashboard/
        $ fab prod service:[service_name]:[op] --user [server_username]
        >>> Ex.: fab prod service:nginx:restart
        >>> This will execute: sudo service nginx restart

### Useful informations

    1. For an easy experience with virtualenv, you can install VirtualenvWrapper
    2. If you get a database error when doing "./manage.py runserver", try to do
    "python manage.py migrate" first. This will update your database with recents
    modifications of the project.
