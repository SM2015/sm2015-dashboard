# coding: utf-8
import os
import json
import logging
from datetime import datetime
from django.utils.translation import ugettext as _
from tables.models import AvanceFisicoFinanciero, Operation, LifeSave, \
    CountryDisbursement, CountryOperation, Quarter

class CountryDisbursementGraph(object):

    @classmethod
    def get_values_graph(cls, country):
        actual_quarter = Quarter.get_actual_quarter()
        table, quarters = CountryOperation.get_table_to_show(country=country,
                                                             until_quarter=actual_quarter)

        data = {
            "cols": [{
                 "id": "D",
                 "label": "Quarter",
                 "type": "string",
                 "pattern": ""
             }, {
                 "id": "B",
                 "label": "Whos in Charge",
                 "type": "string",
                 "pattern": ""
             }, {
                 "id": "sum-G",
                 "label": "sum Amount (US$)",
                 "type": "number",
                 "pattern": ""
             }],
             "rows": [],
             "p": None
        }

        for i_quarter in xrange(0, len(quarters)):
            quarter = quarters[i_quarter]

            for row in table:
                if row['field']['field'] == 'it_disbursements_planned':
                    field = 'SM2015 Projected Disbursements'
                elif row['field']['field'] == 'it_disbursements_actual':
                    field = 'SM2015 Actual Disbursements'
                elif row['field']['field'] == 'it_execution_planned':
                    field = 'Planned Financial Execution'
                elif row['field']['field'] == 'it_execution_actual':
                    field = 'Actual Financial Execution'

                data['rows'].append({"c": [
                    {"v": quarter['quarter__name']},
                    {"v": field},
                    {"v": row['values'][i_quarter]['v']}
                ]})

        return data

class LiveSaveGraph(object):

    @classmethod
    def get_values_graph(cls, country):
        life_saves = LifeSave.objects.filter(country=country)
        data = {
            'series': [],
            'pie': []
        }

        for obj in life_saves:
            data['series'].append({"name": obj.field.abbr, "data": [obj.number_saving]})
            data['pie'].append({"name": obj.field.abbr, "y": obj.percentage})

        return data

class TriangleGraph(object):

    @classmethod
    def export_graph(cls, country, lang):
        path_options_highcharts = TriangleGraph.export_graph_options(country=country, lang=lang)
        file_name = "chart-{country_name}.png".format(country_name=country.slug)

        dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path_chart = "{root}/tables/files/{file_name}".format(root=dir_path, file_name=file_name)

        os.system("phantomjs {root}/website/static/js/highcharts/highcharts-convert.js "\
                  "-infile {options_path} -outfile {path_chart}  -scale 3 -width 350"
                  .format(root=dir_path, country_name=country.slug, path_chart=path_chart, options_path=path_options_highcharts))
        return path_chart, file_name

    @classmethod
    def export_graph_options(cls, country, lang):
        options = u""\
            'options = {'\
                'chart: {'\
                    'polar: true,'\
                    'type: "line",'\
                    'marginLeft: 10,'\
                    'marginRight: 10'\
                '},'\
                'title: {'\
                    '"text": "%s SM2015"'\
                '},'\
                'pane: {'\
                    'size: "85%%"'\
                '},'\
                'xAxis: {'\
                    'categories: %s,'\
                    'tickmarkPlacement: "on",'\
                    'lineWidth: 0,'\
                    'labels: {'\
                        'style: {'\
                            'width: "30px"'\
                        '}'\
                    '}'\
                '},'\
                'yAxis: {'\
                    'gridLineInterpolation: "polygon",'\
                    'lineWidth: 0,'\
                    'min: 0,'\
                    'width: 30'\
                '},'\
                'tooltip: {'\
                    'shared: true,'\
                    'pointFormat: "%sspan style=\'color:{series.color}\'%s{series.name}: %sb%s{point.y}%% %s/b%s%sbr/%s"'\
                '},'\
                'exporting: {'\
                    'enabled: true'\
                '},'\
                'credits: {'\
                    'enabled: false'\
                '},'\
                'series: %s'\
            '}' % (country.name, json.dumps(cls.get_triangle_categories()),\
                 "<", ">", "<", ">", "<", ">", "<", ">", json.dumps(cls.get_triangle_series(country=country, lang=lang)))

        dir_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'graphs', 'files')
        path = "{dir_path}/options-{country_name}.js".format(dir_path=dir_path, country_name=country.slug)
        file_obj = open(path, 'w')
        file_obj.write(options)
        file_obj.close()
        return path

    @classmethod
    def get_graph_data_by_country(cls, country, lang, operation_number=None):
        graph_data = {
            'country_slug': country.slug,
            'country': country.name,
            'triangle_categories': cls.get_triangle_categories(),
            'series': cls.get_triangle_series(country=country, lang=lang, operation_number=operation_number)
        }
        return graph_data

    @classmethod
    def get_triangle_categories(cls):
        return [_("% Avance Tiempo"), _("Ejecucion Financiera"), _("Ejecucion Fisica")]

    @classmethod
    def get_triangle_series(cls, country, lang, operation_number=None):
        if operation_number:
            operation = Operation.objects.filter(country=country, number=operation_number)[0]
            if not operation:
                operation = Operation.objects.filter(country=country).order_by('-id')[0]
        else:
            operation = Operation.objects.filter(country=country).order_by('-id')[0]

        avances = AvanceFisicoFinanciero.objects.filter(country=country,
                                                        language__acronym=lang, operation=operation).last()

        if not avances:
            return []

        try:
            total_days_operation = operation.finish_date - operation.starting_date
            total_days_operation = total_days_operation.days

            total_days_left = operation.finish_date - avances.fecha_de_actualizacion
            total_days_left = total_days_left.days

            if total_days_left < 0:
                time_remaining = 0
            elif total_days_left > total_days_operation:
                time_remaining = 100
            else:
                time_remaining = (float(total_days_left) / float(total_days_operation)) * 100
            avance_tiempo = round(100 - time_remaining, 2)

        except (Operation.DoesNotExist, ZeroDivisionError):
            avance_tiempo = 0

        financiera = {
            'actual': avances.avance_financiero_actual or '',
            'programada': avances.avance_financiero_planificado or '',
            'original_programada': avances.avances_financieros_original_programado or ''
        }
        fisica = {
            'actual': avances.avance_fisico_real or '',
            'programada': avances.avance_fisico_planificado or '',
            'original_programada': avances.avances_fisicos_original_programado or ''
        }

        return [
           {'name': 'Ejecucion Actual (%)', 'data': [avance_tiempo, financiera.get('actual'), fisica.get('actual')], 'pointPlacement': 'on'},
           {'name': 'Ejecucion Programada (%)', 'data': [avance_tiempo, financiera.get('programada'), fisica.get('programada')], 'pointPlacement': 'on'},
           {'name': 'Ejecucion Original Programada (%)', 'data': [avance_tiempo, financiera.get('original_programada'), fisica.get('original_programada')], 'pointPlacement': 'on'}
        ]
