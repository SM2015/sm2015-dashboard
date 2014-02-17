# coding: utf-8
from datetime import date
import codecs
from docx import *
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
    relationships = relationshiplist()
    document = newdocument()
    body = document.xpath('/w:document/w:body', namespaces=nsprefixes)[0]

    # Add BID logo
    relationships, picpara = picture(relationships, 'logo-bid.png', '')
    body.append(picpara)

    # First Heading
    date_today_str = date.today().strftime("%d de {MONTH} de %Y").lstrip("0")
    month_translated = _(date.today().strftime("%B"))
    date_today_str = date_today_str.replace("{MONTH}", month_translated)
    body.append(paragraph([(u"División de Protección Social y Salud, SCL/SPH", 'b')]))
    body.append(paragraph([(u"Iniciativa Salud Mesoamérica 2015, SM2015", 'b')]))
    body.append(paragraph([(u"Conclusiones de la reunión realizada el: {0}".format(date_today_str), 'b')]))
    body.append(paragraph(u''))
 
    # Second Heading
    body.append(paragraph([(u"Operación: {0}".format(operation.name), 'b')]))
    body.append(paragraph([(u"Tipo de Reunión: Seguimiento Mensual de la Ejecución", 'b')]))
    body.append(paragraph([(u"Participantes: {0}, Ferdinando Regalia, Emma Iriarte".format(context.get('user').get_full_name()), 'b')]))
    
    if avances:
        avance = avances[0]
        # Table Avances
        body.append(heading(u"AVANCE FISICO Y FINANCIERO", 1))
        fecha_de_actualization_str = avance.fecha_de_actualizacion.strftime("%d de {MONTH} de %Y").lstrip("0")
        month_translated = _(avance.fecha_de_actualizacion.strftime("%B"))
        fecha_de_actualization_str = fecha_de_actualization_str.replace("{MONTH}", month_translated)
        tbl_rows = [[u'Cual es la fecha en que la información que está registrando fue actualizada', unicode(avance.avance_fisico_planificado)],
                    [u'Avances Fiscos Planificados (Meta Ejecución)', unicode(avance.avance_fisico_planificado)],
                    [u'Avances Físicos reales (Avance en la ejecución real segun el PEP)', unicode(avance.avance_fisico_real)],
                    [u'Avances financieros planificados (Ejecución financiera planificados)', unicode(avance.avance_financiero_planificado)],
                    [u'Avances financieros actuales (Ejecución financiera real según el estados financieros del ejecutor hasta la fecha (%))', unicode(avance.avance_financiero_actual)],
                    [u'Monto total desembolsado (BID a PAIS)', unicode(avance.monto_desembolsado)],
                   ]
        body.append(table(tbl_rows, heading=False))


    # Add Triangle Graph
    body.append(heading(u"Gráficos del Tablero de Control", 1))
    relationships, picpara = picture(relationships, triangle_file_name, '')
    body.append(picpara)

    # HITOS
    body.append(heading(u"ALERTAS TEMPRANAS Y ESTADO DE LOS HITOS", 1))
    tbl_rows = [[u'Indicador de Pago', u'Hito', u'Trimestre', u'Audiencia', u'Estado Actual', u'Alerta/Notas', u'Recomendación', u'Acuerdo']]
    for hito in hitos:
        audiencias = []
        for audiencia in hito.audiencia.all():
            audiencias.append(audiencia.name)

        tbl_rows.append([
            hito.indicador_de_pago,
            hito.hito,
            hito.quarter.name,
            ", ".join(audiencias),
            hito.estado_actual.name,
            hito.alerta_notas or '',
            hito.recomendacion or '',
            hito.acuerdo or ''
        ])

    body.append(table(tbl_rows, heading=False))


    title = 'Hitos e Avances - {0}'.format(country.name)
    creator = 'SM2015 Dashboard'
    coreprops = coreproperties(title=title, creator=creator, subject='', keywords=[])
    appprops = appproperties()
    contenttypes_v = contenttypes()
    websettings_v = websettings()
    wordrelationships_v = wordrelationships(relationships)

    # Save our document
    path = "{root}/tables/files/{country_slug}_hitos_y_avances.docx".format(country_slug=country_slug, root=os.path.realpath('./'))
    savedocx(document, coreprops, appprops, contenttypes_v, websettings_v,
             wordrelationships_v, path)

    file_docx = open(path, 'r')
    response = HttpResponse(mimetype='text/html')
    response['Content-Disposition'] = 'attachment; filename={country_slug}_hitos_y_avances.docx'.format(country_slug=country_slug)
    response['Content-Encoding'] = 'UTF-8'
    response['Content-type'] = 'text/html; charset=UTF-8'
    response.write(file_docx.read())
    file_docx.close()
    return response
