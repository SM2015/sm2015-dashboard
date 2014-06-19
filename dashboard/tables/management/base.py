# coding:utf-8

import os
import re
import sys
import nose
import time
import socket
import commands
import warnings

from os.path import dirname
from optparse import make_option

from django.conf import settings
from django.core.management.base import BaseCommand

class TestCommand(BaseCommand):

    option_list = BaseCommand.option_list + (
        make_option("-a", "--app", dest="app", default=None),
    )

    def __init__(self, test_type=None, *args, **options):
        self.test_type = test_type
        super(TestCommand, self).__init__(*args, **options)
        
    def handle(self, *args, **options):
        
        print 'Running %s tests...' % self.test_type

        warnings.filterwarnings('ignore', '.*',)

        app = options["app"]
        if app:
            apps = [app]
        else:
            apps = [a for a in settings.INSTALLED_APPS if not a.startswith('django')]

        self.args = args
        self.options = options
        self.running_test(apps)

    def running_test(self, apps, test_file=None, capturar_log=False):
        nose_argv = ['nosetests','-sd', '--verbosity=2']
        if not capturar_log:
            nose_argv.append('--nologcapture')

        modules = []
        has_exclude_test = getattr(settings, 'EXCLUDE_TEST_APPS', False)
        nose_argv.append('--with-coverage')
        nose_argv.append('--cover-erase')
        if not test_file:
            for app in apps:
                if has_exclude_test and app in settings.EXCLUDE_TEST_APPS:
                    continue

                test_module_path = "%s.tests" % (app)

                try:
                    try:
                        module = getattr(__import__(test_module_path, locals(), globals(), [self.test_type], 3), self.test_type)
                    except AttributeError, e:
                        print 'Está faltando o módulo de testes %s.%s na sua django-app' % (test_module_path, self.test_type)
                        raise SystemExit(1)

                    modules.append(module)

                except ImportError, e:
                    import traceback
                    sys.stderr.write('%s\n\n' % traceback.format_exc(e))
                    sys.stderr.write('Aparentemente a app "%s" não possui ' \
                                     'as subpastas "tests/%s" ou está ' \
                                     'faltando um arquivo __init__.py em ' \
                                     'cada uma delas\n' % (app, self.test_type))

                    raise SystemExit(666)

                nose_argv.append("--cover-package=%s" % app)

            nose_argv.extend([dirname(x.__file__) for x in modules])

        else:
            nose_argv.append(test_file)

        ret = nose.run(argv=nose_argv)
        if ret:
            code = 0
        else:
            code = 1

        raise SystemExit(code)