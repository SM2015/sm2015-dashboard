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
    root_dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    hitos = Hito.objects.filter(country__slug=country_slug)
    estados_actuais = EstadoActual.objects.all()
    country = Country.objects.get(slug=country_slug)
    options_estados_actuais = {}
    triangle_path, triangle_file_name = TriangleGraph.export_graph(country=country)
    operation = Operation.objects.get(country=country)
    for estado in estados_actuais:
        options_estados_actuais.update({
            "{id}".format(id=estado.id): str(estado.name)
        })

    avances = AvanceFisicoFinanciero.objects.filter(country=country)

    # DOCX
    document = Docx()
    logo_salud = Image("{root}/tables/files/logo_saludmesoam.png".format(root=root_dir_path))
    logo_bid = Image("{root}/tables/files/logo-del-BID.jpg".format(root=root_dir_path))
    document.append(logo_bid)
    document.append(logo_salud)

    # Heading
    date_today_str = date.today().strftime("%d de {MONTH} de %Y").lstrip("0")
    month_translated = _(date.today().strftime("%B"))
    date_today_str = date_today_str.replace("{MONTH}", month_translated)
    heading = Block([InlineText(u"División de Protección Social y Salud, SCL/SPH", bold=True), Break(),
                     InlineText(u"Iniciativa Salud Mesoamérica 2015, SM2015", bold=True), Break(),
                     InlineText(u"Conclusiones de la reunión realizada el: {0}".format(date_today_str), bold=True), Break(),
                     Break(),
                     InlineText(u"Operación: ", bold=True), InlineText(operation.name), Break(),
                     InlineText(u"Tipo de Reunión: ", bold=True), InlineText(u"Seguimiento Mensual de la Ejecución"), Break(),
                     InlineText(u"Participantes: ", bold=True), InlineText(u"{0}, Ferdinando Regalia, Emma Iriarte".format(context.get('user').get_full_name()))])
    document.append(heading)

    document.append(Break())

    # Avances
    if avances:
        avance = avances[0]
        document.append(Block(InlineText("AVANCE FISICO Y FINANCIERO", size=12, font='Times New Roman', bold=True), align='center'))

        if avance.fecha_de_actualizacion:
            fecha_de_actualization_str = avance.fecha_de_actualizacion.strftime("%d de {MONTH} de %Y").lstrip("0")
            month_translated = _(avance.fecha_de_actualizacion.strftime("%B"))
            fecha_de_actualization_str = fecha_de_actualization_str.replace("{MONTH}", month_translated)
        else:
            fecha_de_actualization_str = ''

        row1 = [Cell(BlockText(u'¿Cuándo fue la última vez que actualizó los datos?', bold=True, font='Times New Roman', size=10)),
                Cell(BlockText(u'Avances Fisicos Planificados (Meta Ejecución)', bold=True, font='Times New Roman', size=10)),
                Cell(BlockText(u'Avances Físicos Reales (Avance en la ejecución real)', bold=True, font='Times New Roman', size=10)),
                Cell(BlockText(u'Avances Financieros Planificados (Ejecución financiera planificados)', bold=True, font='Times New Roman', size=10)),
                Cell(BlockText(u'Avances Financieros Actuales (Ejecución financiera real)', bold=True, font='Times New Roman', size=10)),
                Cell(BlockText(u'Monto Desembolsado', bold=True, font='Times New Roman', size=10))]

        row2 = [Cell(BlockText(fecha_de_actualization_str, size=10)),
                Cell(BlockText("{0}%".format(avance.avance_fisico_planificado), size=10)),
                Cell(BlockText("{0}%".format(avance.avance_fisico_real), size=10)),
                Cell(BlockText("{0}%".format(avance.avance_financiero_planificado), size=10)),
                Cell(BlockText("{0}%".format(avance.avance_financiero_actual), size=10)),
                Cell(BlockText(avance.monto_desembolsado, size=10))]

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
    document.append(Block(InlineText(u"Gráficos del Tablero de Control", size=12, font='Times New Roman', bold=True), align='center'))
    document.append(Image("{0}".format(triangle_path), align='center'))

    document.append(Break())

    # HITOS
    is_avaliable_hito = False
    table_hitos = Table(width="100%", padding='3pt')
    table_hitos.add_row([Cell(Block(InlineText(u'Indicador de Pago', bold=True, font='Times New Roman', size=10), align='center')),
                         Cell(Block(InlineText(u'Hito', bold=True, font='Times New Roman', size=10), align='center')),
                         Cell(Block(InlineText(u'Trimestre', bold=True, font='Times New Roman', size=10), align='center')),
                         Cell(Block(InlineText(u'Audiencia', bold=True, font='Times New Roman', size=10), align='center')),
                         Cell(Block(InlineText(u'Estado Actual', bold=True, font='Times New Roman', size=10), align='center')),
                         Cell(Block(InlineText(u'Alerta/Notas', bold=True, font='Times New Roman', size=10), align='center')),
                         Cell(Block(InlineText(u'Recomendación', bold=True, font='Times New Roman', size=10), align='center')),
                         Cell(Block(InlineText(u'Acuerdo', bold=True, font='Times New Roman', size=10), align='center'))])

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
                Cell(BlockText(hito.indicador_de_pago, font='Times New Roman', size=10)),
                Cell(BlockText(hito.hito, font='Times New Roman', size=10)),
                Cell(BlockText(hito.quarter.name, font='Times New Roman', size=10)),
                Cell(BlockText(", ".join(audiencias), font='Times New Roman', size=10)),
                Cell(BlockText(estado_actual_name, font='Times New Roman', size=10), bgcolor=bg_estado),
                Cell(BlockText(hito.alerta_notas or '', font='Times New Roman', size=10)),
                Cell(BlockText(hito.recomendacion or '', font='Times New Roman', size=10)),
                Cell(BlockText(hito.acuerdo or '', font='Times New Roman', size=10))
            ])

    if is_avaliable_hito:
        document.append(Block(InlineText(u"ALERTAS TEMPRANAS Y ESTADO DE LOS HITOS", size=12, font='Times New Roman', bold=True), align='center'))
        document.append(table_hitos)

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
