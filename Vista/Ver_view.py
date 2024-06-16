from customtkinter import * 
from tkinter import ttk

class VerFrames():
    def __init__(self,master) -> None:
        self.master=master
    def verCompras(self):
        tabla = ttk.Treeview(self)
        #crea columnas
        tabla['columns']=("1","2","3","4","5")
        #cambia ancho de columna id
        tabla.column("#0",width=0)
        #agrega texto a los headings de las columnas
        tabla.heading("1",text="ID")
        tabla.heading("2",text="Titulo Libro")
        tabla.heading("3",text="Fecha")
        tabla.heading("4",text="Cantidad Comprada")
        tabla.heading("5",text="Total Compra")
        #acomoda la tabla en la ventana
        tabla.place(x=325,y=300,anchor="center")
    
    def verEditoriales(self):
        tabla = ttk.Treeview(self)
        #crea columnas
        tabla['columns']=("1","2")
        #cambia ancho de columna id
        tabla.column("#0",width=0)
        #agrega texto a los headings de las columnas
        tabla.heading("1",text="ID")
        tabla.heading("2",text="Nombre")
        #acomoda la tabla en la ventana
        tabla.place(x=325,y=300,anchor="center")

    def verProductos(self):
        tabla = ttk.Treeview(self)
        #crea columnas
        tabla['columns']=("1","2","3","4")
        #cambia ancho de columna id
        tabla.column("#0",width=0)
        tabla.column("#1",width=40)
        #agrega texto a los headings de las columnas
        tabla.heading("1",text="ID")
        tabla.heading("2",text="Titulo")
        tabla.heading("3",text="Autor")
        tabla.heading("4",text="Stock")
        #acomoda la tabla en la ventana
        tabla.place(x=325,y=300,anchor="center")

    def verProveedores(self):
        tabla = ttk.Treeview(self)
        #crea columnas
        tabla['columns']=("1","2")
        #cambia ancho de columna id
        tabla.column("#0",width=0)
        tabla.column("#1",width=20)
        #agrega texto a los headings de las columnas
        tabla.heading("1",text="ID")
        tabla.heading("2",text="Nombre")
        #acomoda la tabla en la ventana
        tabla.place(x=325,y=300,anchor="center")
    
    def verVentas(self):
        #crea tabla 
        tabla = ttk.Treeview(self)
        #crea columnas
        tabla['columns']=("1","2","3","4","5")
        #cambia ancho de columna id
        tabla.column("#0",width=0)
        #agrega texto a los headings de las columnas
        tabla.heading("1",text="ID")
        tabla.heading("2",text="Titulo Libro")
        tabla.heading("3",text="Fecha")
        tabla.heading("4",text="Cantidad Vendida")
        tabla.heading("5",text="Total venta")
        #acomoda la tabla en la ventana
        tabla.place(x=325,y=300,anchor="center")