# coding: utf-8
import os
from datetime import date
import codecs
from py2docx.docx import Docx
from py2docx.elements import Block
from py2docx.elements.image import Image
from py2docx.elements.table import Table, Cell
from py2docx.elements.text import InlineText, Break, BlockText
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _
from django.template.loader import render_to_string
from django.shortcuts import HttpResponse
from django.template import RequestContext
from tables.models import Hito, AvanceFisicoFinanciero, EstadoActual, Operation
from graphs.models import TriangleGraph
from core.models import Country

@login_required
def render_export_hitos_and_avances2(request, country_slug):
    context = RequestContext(request)
    hitos = Hito.objects.filter(country__slug=country_slug)
    estados_actuais = EstadoActual.objects.all()
    country = Country.objects.get(slug=country_slug)
    options_estados_actuais = {}
    hitos_estados_actuais = {}
    for estado in estados_actuais:
        options_estados_actuais.update({
            "{id}".format(id=estado.id): str(estado.name)
        })

    for hito in hitos:
        options_estados_actuais.update({
            'selected': str(hito.estado_actual.id)
        })
        hito.options_estados_actuais = options_estados_actuais

    avances = AvanceFisicoFinanciero.objects.filter(country=country)

    context.update({'hitos': hitos})
    context.update({'avances': avances})
    context.update({'operation': Operation.objects.get(country=country)})

    rendered = render_to_string("tables/word/hitos_and_avances.html", context)

    response = HttpResponse(mimetype='text/html')
    response['Content-Disposition'] = 'attachment; filename={country_slug}_hitos_y_avances.docx'.format(country_slug=country_slug)
    response['Content-Encoding'] = 'UTF-8'
    response['Content-type'] = 'text/html; charset=UTF-8'
    response.write(rendered.encode('utf8'))
    return response


@login_required
def render_export_hitos_and_avances(request, country_slug):
    context = RequestContext(request)
    hitos = Hito.objects.filter(country__slug=country_slug)
    estados_actuais = EstadoActual.objects.all()
    country = Country.objects.get(slug=country_slug)
    options_estados_actuais = {}
    hitos_estados_actuais = {}
    triangle_path, triangle_file_name = TriangleGraph.export_graph(country=country)
    operation = Operation.objects.get(country=country)
    for estado in estados_actuais:
        options_estados_actuais.update({
            "{id}".format(id=estado.id): str(estado.name)
        })

    for hito in hitos:
        options_estados_actuais.update({
            'selected': str(hito.estado_actual.id)
        })
        hito.options_estados_actuais = options_estados_actuais

    avances = AvanceFisicoFinanciero.objects.filter(country=country)

    # DOCX
    document = Docx()
    logo_bid = Image("./logo-bid.png")
    document.append(logo_bid)

    # Heading
    date_today_str = date.today().strftime("%d de {MONTH} de %Y").lstrip("0")
    month_translated = _(date.today().strftime("%B"))
    date_today_str = date_today_str.replace("{MONTH}", month_translated)
    heading = Block([InlineText(u"División de Protección Social y Salud, SCL/SPH", bold=True), Break(),
                     InlineText(u"Iniciativa Salud Mesoamérica 2015, SM2015", bold=True), Break(),
                     InlineText(u"Conclusiones de la reunión realizada el: {0}".format(date_today_str), bold=True), Break(),
                     Break(),
                     InlineText(u"Operación: {0}".format(operation.name), bold=True), Break(),
                     InlineText(u"Tipo de Reunión: Seguimiento Mensual de la Ejecución", bold=True), Break(),
                     InlineText(u"Participantes: {0}, Ferdinando Regalia, Emma Iriarte".format(context.get('user').get_full_name()), bold=True)])
    document.append(heading)

    # Avances
    if avances:
        avance = avances[0]
        document.append(BlockText("AVANCE FISICO Y FINANCIERO"))

        fecha_de_actualization_str = avance.fecha_de_actualizacion.strftime("%d de {MONTH} de %Y").lstrip("0")
        month_translated = _(avance.fecha_de_actualizacion.strftime("%B"))
        fecha_de_actualization_str = fecha_de_actualization_str.replace("{MONTH}", month_translated)

        row1 = [Cell(BlockText(u'Cual es la fecha en que la información que está registrando fue actualizada')), 
                Cell(BlockText(fecha_de_actualization_str))]
        row2 = [Cell(BlockText(u'Avances Fiscos Planificados (Meta Ejecución)')), 
                Cell(BlockText(avance.avance_fisico_planificado))]
        row3 = [Cell(BlockText(u'Avances Físicos reales (Avance en la ejecución real segun el PEP)')), 
                Cell(BlockText(avance.avance_fisico_real))]
        row4 = [Cell(BlockText(u'Avances financieros planificados (Ejecución financiera planificados)')), 
                Cell(BlockText(avance.avance_financiero_planificado))]
        row5 = [Cell(BlockText(u'Avances financieros actuales (Ejecución financiera real según el estados financieros del ejecutor hasta la fecha (%))')), 
                Cell(BlockText(avance.avance_financiero_actual))]
        row6 = [Cell(BlockText(u'Monto total desembolsado (BID a PAIS)')),
                Cell(BlockText(avance.monto_desembolsado))]

        table_avances = Table(width="100%", margin='1pt')
        table_avances.add_row(row1)
        table_avances.add_row(row2)
        table_avances.add_row(row3)
        table_avances.add_row(row4)
        table_avances.add_row(row5)
        table_avances.add_row(row6)
        document.append(table_avances)

    # Add Triangle Graph
    document.append(BlockText(u"Gráficos del Tablero de Control"))
    document.append(Image("./{0}".format(triangle_file_name)))

    # HITOS
    document.append(BlockText("ALERTAS TEMPRANAS Y ESTADO DE LOS HITOS"))
    table_hitos = Table(width="100%", margin='1pt')
    table_hitos.add_row([Cell(BlockText(u'Indicador de Pago')),
                        Cell(BlockText(u'Hito')),
                        Cell(BlockText(u'Trimestre')),
                        Cell(BlockText(u'Audiencia')),
                        Cell(BlockText(u'Estado Actual')),
                        Cell(BlockText(u'Alerta/Notas')),
                        Cell(BlockText(u'Recomendación')),
                        Cell(BlockText(u'Acuerdo'))])
    for hito in hitos:
        if hito.alerta_notas or hito.recomendacion:
            audiencias = []
            for audiencia in hito.audiencia.all():
                audiencias.append(audiencia.name)

            table_hitos.add_row([
                Cell(BlockText(hito.indicador_de_pago)),
                Cell(BlockText(hito.hito)),
                Cell(BlockText(hito.quarter.name)),
                Cell(BlockText(", ".join(audiencias))),
                Cell(BlockText(hito.estado_actual.name)),
                Cell(BlockText(hito.alerta_notas or '')),
                Cell(BlockText(hito.recomendacion or '')),
                Cell(BlockText(hito.acuerdo or ''))
            ])
    document.append(table_hitos)

    # Save our document
    path = "{root}/tables/files/{country_slug}_hitos_y_avances.docx".format(country_slug=country_slug, root=os.path.realpath('./'))
    document.save(path)

    file_docx = open(path, 'r')
    response = HttpResponse(mimetype='text/html')
    response['Content-Disposition'] = 'attachment; filename={country_slug}_hitos_y_avances.docx'.format(country_slug=country_slug)
    response['Content-Encoding'] = 'UTF-8'
    response['Content-type'] = 'text/html; charset=UTF-8'
    response.write(file_docx.read())
    file_docx.close()
    return response
