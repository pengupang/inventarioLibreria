import customtkinter as cTK
import tkinter as tk
from tkinter import ttk

class FrameVerIngresarProductos():
    def __init__(self,ventana) -> None:
        #crea tabla 
        tabla = ttk.Treeview(ventana,)
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
