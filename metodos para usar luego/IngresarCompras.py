import customtkinter as cTK
import tkinter as tk
from tkinter import ttk

class FrameVerIngresarCompras():
    def __init__(self,ventana) -> None:
        
        self.ventana = ventana

        label_id = tk.Label(ventana, text="ID:")
        label_titulo = tk.Label(ventana, text="Título Libro:")
        label_fecha = tk.Label(ventana, text="Fecha:")
        label_cantidad = tk.Label(ventana, text="Cantidad Comprada:")
        label_total = tk.Label(ventana, text="Total Compra:")
        
        self.entry_id = tk.Entry(ventana)
        self.entry_titulo = tk.Entry(ventana)
        self.entry_fecha = tk.Entry(ventana)
        self.entry_cantidad = tk.Entry(ventana)
        self.entry_total = tk.Entry(ventana)
        
        label_id.place(x=50, y=50)
        self.entry_id.place(x=150, y=50)
        
        label_titulo.place(x=50, y=80)
        self.entry_titulo.place(x=150, y=80)
        
        label_fecha.place(x=50, y=110)
        self.entry_fecha.place(x=150, y=110)
        
        label_cantidad.place(x=50, y=140)
        self.entry_cantidad.place(x=150, y=140)
        
        label_total.place(x=50, y=170)
        self.entry_total.place(x=150, y=170)
        
        self.btn_ingresar = tk.Button(ventana, text="Ingresar", command=self.guardar_datos)
        self.btn_ingresar.place(x=50, y=200)
        
        self.tabla = ttk.Treeview(ventana)
        self.tabla['columns'] = ("ID", "Titulo Libro", "Fecha", "Cantidad Comprada", "Total Compra")
        self.tabla.column("#0", width=0)
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Titulo Libro", text="Titulo Libro")
        self.tabla.heading("Fecha", text="Fecha")
        self.tabla.heading("Cantidad Comprada", text="Cantidad Comprada")
        self.tabla.heading("Total Compra", text="Total Compra")
        self.tabla.place(x=325, y=50)
        
    def guardar_datos(self):

        id_value = self.entry_id.get()
        titulo_value = self.entry_titulo.get()
        fecha_value = self.entry_fecha.get()
        cantidad_value = self.entry_cantidad.get()
        total_value = self.entry_total.get()
        

        self.tabla.insert("", "end", values=(id_value, titulo_value, fecha_value, cantidad_value, total_value))
        
        self.entry_id.delete(0, tk.END)
        self.entry_titulo.delete(0, tk.END)
        self.entry_fecha.delete(0, tk.END)
        self.entry_cantidad.delete(0, tk.END)
        self.entry_total.delete(0, tk.END)
