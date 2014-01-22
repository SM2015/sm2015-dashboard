# coding: utf-8
import os
from django.core.management.base import BaseCommand, CommandError
from tables.models import GrantsFinances

class Command(BaseCommand):

    def handle(self, file_name, *args, **options):
        path = "{root}/core/csv/{file_name}".format(root=os.path.realpath('./'), file_name=file_name)

        file_obj = open(path, 'r')
        file_content = file_obj.read()

        GrantsFinances.objects.all().delete()
        

        for row in file_content.split('\n'):
            if row:
                columns = row.split(',')

                GrantsFinances.objects.create(
                    period = columns[0],
                    contribution_accumulated_bmgf = float(columns[1]) if columns[1] else 0,
                    contribution_accumulated_icss = float(columns[2]) if columns[2] else 0,
                    contribution_spanish_government = float(columns[3]) if columns[3] else 0,
                    korean_tc_accumulated = float(columns[4]) if columns[4] else 0,
                    contribution_donates = float(columns[5]) if columns[5] else 0,
                    contribution_real_bmgf = float(columns[6]) if columns[6] else 0,
                    contribution_real_icss = float(columns[7]) if columns[7] else 0,
                    contribution_real_gos = float(columns[8]) if columns[8] else 0,
                    korea_actual = float(columns[9]) if columns[9] else 0
                )
