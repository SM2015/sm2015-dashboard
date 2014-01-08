# coding: utf-8
from docx import *

class ExportDocx(object):
    def _get_header(self, body):
        body.append(heading("Welcome to Python's docx module", 1))
        return body

    def export(self):
        relationships = relationshiplist()
        document = newdocument()
        body = document.xpath('/w:document/w:body', namespaces=nsprefixes)[0]
        
        body = self._get_header(body=body)

        tbl_rows = [ [u'AVANCE FISICO Y FINANCIERO']
                   , [u'¿Cuándo fue la última vez que actualizó los datos?', 
                      u'Avances Fiscos Planificados (Meta Ejecución)',
                      u'Avances Físicos reales (Avance en la ejecución real)',
                      u'Avances financieros  planificados (Ejecución financiera planificados)',
                      u'Avances financieros actuales (Ejecución financiera real)',
                      u'Monto Desembolsado'
                    ]
                   , [u'11/27/2013', u'95%', u'77%', u'33.8%', u'23%', u'$3,143,054']
        ]
        tabela = table(tbl_rows, heading=True)
        body.append(tabela)

        # Create our properties, contenttypes, and other support files
        title    = u'SM2015 Dashboard'
        subject  = u'SM2015 Dashboard'
        creator  = u'Sm2015'
        keywords = [u'sm2015']

        coreprops = coreproperties(title=title, subject=subject, creator=creator,
                                   keywords=keywords)
        appprops = appproperties()
        contenttypes_return = contenttypes()
        websettings_return = websettings()
        wordrelationships_return = wordrelationships(relationships)

        # Save our document
        savedocx(document, coreprops, appprops, contenttypes_return, websettings_return,
                 wordrelationships_return, '/tmp/sm2015.docx')

        return '/tmp/sm2015.docx'
