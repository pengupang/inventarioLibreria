from reportlab.lib import colors
from reportlab.lib.pagesizes import letter 
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate
import os
from Modelo.conexion import ejecutar_consulta

def generarPdf(query,columnas,nombre):
    rows = ejecutar_consulta(query)
    data = []; data.append(columnas)
    for row in rows:
        data.append(row)

    elementos = []
    directorio = os.path.abspath(os.path.join(os.getcwd(),"pdfs/{}.pdf".format(nombre)))
    doc = SimpleDocTemplate(directorio)
    lista = Table(data)
    lista.setStyle(TableStyle([
        ('INNERGRID',(0,0),(-1,-1), 0.35, colors.grey),
        ('BACKGROUND',(-1,0),(-1,-1), colors.grey)
        ]))

    elementos.append(lista)
    doc.build(elementos)
