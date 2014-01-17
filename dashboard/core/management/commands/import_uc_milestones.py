# coding: utf-8
import os
from django.core.management.base import BaseCommand, CommandError
from tables.models import UcMilestone
from core.models import Language

class Command(BaseCommand):

    def handle(self, lang, file_name, *args, **options):
        language = Language.objects.get(acronym=lang)
        path = "{root}/core/csv/{file_name}".format(root=os.path.realpath('./'), file_name=file_name)

        file_obj = open(path, 'r')
        file_content = file_obj.read()

        UcMilestone.objects.filter(language=language).delete()
        
        for row in file_content.split('\n'):
            if row:
                columns = row.split(',')

                UcMilestone.objects.create(
                    language = language,
                    objective = columns[0].replace(';',','),
                    coordination_unit_milestone = columns[1].replace(';',','),
                    quarter = columns[2].replace(';',','),
                    status = columns[3].replace(';',','),
                    observation = columns[4].replace(';',',')
                )
