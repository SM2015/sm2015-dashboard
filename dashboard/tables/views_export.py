# coding: utf-8
import os
from datetime import date
from py2docx.docx import Docx
from py2docx.elements import Block
from py2docx.elements.image import Image
from py2docx.elements.table import Table, Cell
from py2docx.elements.text import InlineText, Break, BlockText
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _
from django.shortcuts import HttpResponse
from django.template import RequestContext
from tables.models import Hito, AvanceFisicoFinanciero, EstadoActual, Operation
from graphs.models import TriangleGraph
from core.models import Country


@login_required
def render_export_hitos_and_avances(request, country_slug):
    context = RequestContext(request)
    if country_slug in ['belize']:
        language_code = 'en'
    else:
        language_code = 'es'
    root_dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    hitos = Hito.objects.filter(country__slug=country_slug,
                                language__acronym=language_code)
    estados_actuais = EstadoActual.objects.all()
    country = Country.objects.get(slug=country_slug)
    options_estados_actuais = {}
    triangle_path, triangle_file_name = TriangleGraph.export_graph(country=country, lang=request.LANGUAGE_CODE)
    operation = Operation.objects.get(country=country)
    for estado in estados_actuais:
        options_estados_actuais.update({
            "{id}".format(id=estado.id): str(estado.name)
        })

    avances = AvanceFisicoFinanciero.objects.filter(country=country)

    # DOCX
    document_font = 'Times New Roman'
    document = Docx()

    logo_salud = Image("{root}/tables/files/logo_saludmesoam.png".format(root=root_dir_path),
                       document=document, width="70%", height="70%")
    logo_bid = Image("{root}/tables/files/logo-del-BID.jpg".format(root=root_dir_path),
                     document=document, width="70%", height="70%")
    table_logos = Table(width="100%")
    table_logos.add_row([Cell(logo_salud, width="50%"), Cell(logo_bid, width="50%")])
    document.append(table_logos)
    document.append(Break())

    # Heading
    date_today_str = date.today().strftime("%d de {MONTH} de %Y").lstrip("0")
    month_translated = _(date.today().strftime("%B"))
    date_today_str = date_today_str.replace("{MONTH}", month_translated)
    heading = Block([InlineText(u"División de Protección Social y Salud, SCL/SPH", bold=True, font=document_font), Break(),
                     InlineText(u"Iniciativa Salud Mesoamérica 2015, SM2015", bold=True, font=document_font), Break(),
                     InlineText(u"Conclusiones de la reunión realizada el: {0}".format(date_today_str), bold=True, font=document_font), Break(),
                     Break(),
                     InlineText(u"Operación: ", bold=True, font=document_font), InlineText(operation.name, font=document_font), Break(),
                     InlineText(u"Tipo de Reunión: ", bold=True, font=document_font), InlineText(u"Seguimiento Mensual de la Ejecución", font=document_font), Break(),
                     InlineText(u"Participantes: ", bold=True, font=document_font), InlineText(u"{0}, Ferdinando Regalia, Emma Iriarte".format(context.get('user').get_full_name()), font=document_font)])
    document.append(heading)

    document.append(Break())

    # Avances
    if avances:
        avance = avances[0]
        document.append(Block(InlineText("AVANCE FISICO Y FINANCIERO", size=12, font=document_font, bold=True), align='center'))

        if avance.fecha_de_actualizacion:
            fecha_de_actualization_str = avance.fecha_de_actualizacion.strftime("%d de {MONTH} de %Y").lstrip("0")
            month_translated = _(avance.fecha_de_actualizacion.strftime("%B"))
            fecha_de_actualization_str = fecha_de_actualization_str.replace("{MONTH}", month_translated)
        else:
            fecha_de_actualization_str = ''

        row1 = [Cell(BlockText(u'¿Cuándo fue la última vez que actualizó los datos?', bold=True, font=document_font, size=10)),
                Cell(BlockText(u'Avances Fisicos Planificados (Meta Ejecución)', bold=True, font=document_font, size=10)),
                Cell(BlockText(u'Avances Físicos Reales (Avance en la ejecución real)', bold=True, font=document_font, size=10)),
                Cell(BlockText(u'Avances Financieros Planificados (Ejecución financiera planificados)', bold=True, font=document_font, size=10)),
                Cell(BlockText(u'Avances Financieros Actuales (Ejecución financiera real)', bold=True, font=document_font, size=10)),
                Cell(BlockText(u'Monto Desembolsado', bold=True, font=document_font, size=10))]

        row2 = [Cell(BlockText(fecha_de_actualization_str, size=10, font=document_font)),
                Cell(BlockText("{0}%".format(avance.avance_fisico_planificado), size=10, font=document_font)),
                Cell(BlockText("{0}%".format(avance.avance_fisico_real), size=10, font=document_font)),
                Cell(BlockText("{0}%".format(avance.avance_financiero_planificado), size=10, font=document_font)),
                Cell(BlockText("{0}%".format(avance.avance_financiero_actual), size=10, font=document_font)),
                Cell(BlockText(avance.monto_desembolsado, size=10, font=document_font))]

        table_avances = Table(width="100%", padding='3pt',
                              border={'top': {'color': '#000000', 'size': '1pt', 'style': 'solid'},
                                      'right': {'color': '#000000', 'size': '1pt', 'style': 'solid'},
                                      'bottom': {'color': '#000000', 'size': '1pt', 'style': 'solid'},
                                      'left': {'color': '#000000', 'size': '1pt', 'style': 'solid'}})
        table_avances.add_row(row1)
        table_avances.add_row(row2)
        document.append(table_avances)

    document.append(Break())
    # Add Triangle Graph
    document.append(Block(InlineText(u"Gráficos del Tablero de Control", size=12, font=document_font, bold=True), align='center'))
    document.append(Image("{0}".format(triangle_path), document=document, align='center'))
    document.append(Break())

    # ALERTS, RECOMENDATIONS AND UPCOMING... FROM AVANCES
    row1 = [Cell(BlockText(u'Alertas Temprana en General', color='#6F7B8A', font=document_font), bgcolor='#ECF0F2', width='7cm', valign='center'),
            Cell(BlockText(avance.alerta, size=10, font=document_font), valign='center')]

    row2 = [Cell(BlockText(u'Recomendaciones', color='#6F7B8A', font=document_font), bgcolor='#ECF0F2', width='7cm', valign='center'),
            Cell(BlockText(avance.recomendacion, size=10, font=document_font), valign='center')]

    row3 = [Cell(BlockText(u'Upcoming Policy Dialogue Events', color='#6F7B8A', font=document_font), bgcolor='#ECF0F2', width='7cm', valign='center'),
            Cell(BlockText(avance.upcoming_policy_dialogue_events or '', size=10, font=document_font), valign='center')]

    table_avances2 = Table(width="100%", padding='3pt')
    table_avances2.add_row(row1)
    table_avances2.add_row(row2)
    table_avances2.add_row(row3)
    document.append(table_avances2)
    document.append(Break())

    # HITOS
    is_avaliable_hito = False
    table_hitos = Table(width="100%", padding='3pt')
    table_hitos.add_row([Cell(Block(InlineText(u'Indicador de Pago', bold=True, font=document_font, size=10), align='center')),
                         Cell(Block(InlineText(u'Hito', bold=True, font=document_font, size=10), align='center')),
                         Cell(Block(InlineText(u'Trimestre', bold=True, font=document_font, size=10), align='center')),
                         Cell(Block(InlineText(u'Audiencia', bold=True, font=document_font, size=10), align='center')),
                         Cell(Block(InlineText(u'Estado Actual', bold=True, font=document_font, size=10), align='center')),
                         Cell(Block(InlineText(u'Alerta/Notas', bold=True, font=document_font, size=10), align='center')),
                         Cell(Block(InlineText(u'Recomendación', bold=True, font=document_font, size=10), align='center')),
                         Cell(Block(InlineText(u'Acuerdo', bold=True, font=document_font, size=10), align='center'))])

    for hito in hitos:
        if hito.recomendacion \
           or hito.alerta_notas \
           or (hito.estado_actual and hito.estado_actual.name
               in ['Retrasado', 'En proceso']):
            is_avaliable_hito = True

            audiencias = []
            for audiencia in hito.audiencia.all():
                audiencias.append(audiencia.name)

            bg_estado = '#FFFFFF'
            if hito.estado_actual:
                if hito.estado_actual.name == 'Cumplido':
                    bg_estado = '#77FF77'
                elif hito.estado_actual.name == 'Retrasado':
                    bg_estado = '#FF8888'
                elif hito.estado_actual.name == 'En proceso':
                    bg_estado = '#FEFF00'
                estado_actual_name = hito.estado_actual.name
            else:
                estado_actual_name = ''

            table_hitos.add_row([
                Cell(BlockText(hito.indicador_de_pago, font=document_font, size=10)),
                Cell(BlockText(hito.hito, font=document_font, size=10)),
                Cell(BlockText(hito.quarter.name, font=document_font, size=10)),
                Cell(BlockText(", ".join(audiencias), font=document_font, size=10)),
                Cell(BlockText(estado_actual_name, font=document_font, size=10), bgcolor=bg_estado),
                Cell(BlockText(hito.alerta_notas or '', font=document_font, size=10)),
                Cell(BlockText(hito.recomendacion or '', font=document_font, size=10)),
                Cell(BlockText(hito.acuerdo or '', font=document_font, size=10))
            ])

    if is_avaliable_hito:
        document.append(Block(InlineText(u"ALERTAS TEMPRANAS Y ESTADO DE LOS HITOS", size=12, font=document_font, bold=True), align='center'))
        document.append(table_hitos)

    document.append(Break())
    document.append(BlockText(""))

    # EMPTY TABLE TO BE FILLED OUT DURING THE MEETING
    border_cell = {'left': {'color': '#000000', 'size': '1pt', 'style': 'solid'},
                    'bottom': {'color': '#000000', 'size': '1pt', 'style': 'solid'},
                    'top': {'color': '#000000', 'size': '1pt', 'style': 'solid'},
                    'right': {'color': '#000000', 'size': '1pt', 'style': 'solid'}}

    table_empty = Table(width="100%", padding='3pt')
    #table_empty.add_row([Cell(Block(InlineText(u'DISCUSION CON EL JEFE DE DIVISION Y UC', font=document_font), align="center"), valign='center', border=border_cell)])
    #table_empty.add_row([Cell(BlockText(""), valign='center', border=border_cell)])

    table_empty.add_row([Cell(Block(InlineText(u'AVANCES PARA EL INFORME TRIMESTRAL', font=document_font), align="center"), valign='center', border=border_cell)])
    table_empty.add_row([Cell(BlockText(""), valign='center', border=border_cell)])

    table_empty.add_row([Cell(Block(InlineText(u'ACUERDOS CON EL JEFE DE DIVISION Y LA UNIDAD COORDINADORA', font=document_font), align="center"), valign='center', border=border_cell)])
    table_empty.add_row([Cell(BlockText(""), valign='center', border=border_cell)])
    document.append(table_empty)


    # Save our document
    path = "{root}/tables/files/{country_slug}_hitos_y_avances.docx".format(country_slug=country_slug, root=root_dir_path)
    document.save(path)

    file_docx = open(path, 'r')
    response = HttpResponse(mimetype='text/html')
    response['Content-Disposition'] = 'attachment; filename={country_slug}_hitos_y_avances.docx'.format(country_slug=country_slug)
    response['Content-Encoding'] = 'UTF-8'
    response['Content-type'] = 'text/html; charset=UTF-8'
    response.write(file_docx.read())
    file_docx.close()
    return response
