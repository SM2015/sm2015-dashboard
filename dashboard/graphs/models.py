# coding: utf-8
import os
from datetime import datetime
from django.db import models
from tables.models import AvanceFisicoFinanciero, Operation, LifeSave, \
        CountryDisbursement

class CountryDisbursementGraph(object):

    @classmethod
    def get_values_graph(cls, country):
        objs = CountryDisbursement.objects.filter(country=country).order_by('quarter')
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

        for obj in objs:
            data['rows'].append({"c": [
                {"v": obj.quarter}, 
                {"v": obj.charger.name}, 
                {"v": obj.amount}
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
    def export_graph(cls, country):
        path_options_highcharts = TriangleGraph.export_graph_options(country=country)
        file_name = "chart-{country_name}.png".format(country_name=country.slug)
        path_chart = "{root}/{file_name}".format(root=os.path.realpath('./'), file_name=file_name)

        os.system("phantomjs {root}/website/static/js/highcharts/highcharts-convert.js "\
                "-infile {options_path} -outfile {path_chart}  -scale 5 -width 280"
                .format(root=os.path.realpath('./'), country_name=country.slug, path_chart=path_chart, options_path=path_options_highcharts))
        return path_chart, file_name

    @classmethod
    def export_graph_options(cls, country):
        options = u""\
            "options = {"\
                "chart: {"\
                    "polar: true,"\
                    "type: 'line',"\
                    "marginLeft: 10,"\
                    "marginRight: 10,"\
                "},"\
                "title: {"\
                    "text: '%s Primera Operacion SM2015'"\
                "},"\
                "pane: {"\
                    "size: '85%%'"\
                "},"\
                "xAxis: {"\
                    "categories: %s,"\
                    "tickmarkPlacement: 'on',"\
                    "lineWidth: 0,"\
                    "labels: {"\
                        "style: {"\
                            "width: '30px'"\
                        "}"\
                    "}"\
                "},"\
                "yAxis: {"\
                    "gridLineInterpolation: 'polygon',"\
                    "lineWidth: 0,"\
                    "min: 0,"\
                    "width: 30"\
                "},"\
                "tooltip: {"\
                    "shared: true,"\
                    "pointFormat: '%sspan style=\"color:{series.color}\"%s{series.name}: %sb%s{point.y}%% %s/b%s%sbr/%s'"\
                "},"\
                "exporting: {"\
                    "enabled: true"\
                "},"\
                "credits: {"\
                    "enabled: false"\
                "},"\
                "series: %s"\
            "}" % (country.name, unicode(cls.get_triangle_categories()),\
                 "<", ">", "<", ">", "<", ">", "<", ">", unicode(cls.get_triangle_series(country=country)))
            
        path = "{root}/graphs/files/options-{country_name}.js".format(root=os.path.realpath('./'), country_name=country.slug)
        file_obj = open(path, 'w')
        file_obj.write(options)
        file_obj.close()
        return path

    @classmethod
    def get_graph_data_by_country(cls, country):
        graph_data = {
            'country_slug': country.slug,
            'country': country.name,
            'triangle_categories': cls.get_triangle_categories(),
            'series': cls.get_triangle_series(country=country)
        }
        return graph_data

    @classmethod
    def get_triangle_categories(cls):
        return ["% Avance Tiempo", "Ejecucion Financiera", "Ejecucion Fisica"]

    @classmethod
    def get_triangle_series(cls, country):
        try:
            avances = AvanceFisicoFinanciero.objects.get(country=country)
        except AvanceFisicoFinanciero.DoesNotExist:
            return []

        try: 
            operation = Operation.objects.get(country=country)
            total_days_operation = operation.finish_date - operation.starting_date
            total_days_operation = total_days_operation.days

            total_days_left = operation.finish_date - datetime.date(datetime.today())
            total_days_left = total_days_left.days
            if total_days_left < 0:
                total_days_let = 0

            time_remaining = total_days_operation / total_days_left
            avance_tiempo = round(100 - time_remaining, 2)

        except Operation.DoesNotExist:
            avance_tiempo = 0

        financiera = {
            'actual': avances.avance_financiero_actual,
            'programada': avances.avance_financiero_planificado,
            'original_programada': avances.avances_financieros_original_programado,
            'monto_comprometido': avances.monto_comprometido
        }
        fisica = {
            'actual': avances.avance_fisico_real,
            'programada': avances.avance_fisico_planificado,
            'original_programada': avances.avances_fisicos_original_programado,
            'monto_comprometido': avances.monto_comprometido
        }
        return [
           {'name': 'Ejecucion Actual', 'data': [avance_tiempo, financiera.get('actual'), fisica.get('actual')], 'pointPlacement': 'on'},
           {'name': 'Ejecucion Programada', 'data': [avance_tiempo, financiera.get('programada'), fisica.get('programada')], 'pointPlacement': 'on'},
           {'name': 'Ejecucion Original Programada', 'data': [avance_tiempo, financiera.get('original_programada'), fisica.get('original_programada')], 'pointPlacement': 'on'},
           {'name': '$ Comprometido', 'data': ['-', '-', '-'], 'pointPlacement': 'on'}
        ]
