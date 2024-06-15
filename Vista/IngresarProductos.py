import customtkinter as cTK
import tkinter as tk
from tkinter import ttk

class FrameVerIngresarProductos():
    def __init__(self,ventana) -> None:
        
        self.ventana = ventana

        label_id = tk.Label(ventana, text="ID:")
        label_titulo = tk.Label(ventana, text="Título:")
        label_autor = tk.Label(ventana, text="Autor:")
        label_stock = tk.Label(ventana, text="Stock:")
        
        self.entry_id = tk.Entry(ventana)
        self.entry_titulo = tk.Entry(ventana)
        self.entry_autor = tk.Entry(ventana)
        self.entry_stock = tk.Entry(ventana)
        
        label_id.place(x=50, y=50)
        self.entry_id.place(x=150, y=50)
        
        label_titulo.place(x=50, y=80)
        self.entry_titulo.place(x=150, y=80)
        
        label_autor.place(x=50, y=110)
        self.entry_autor.place(x=150, y=110)
        
        label_stock.place(x=50, y=140)
        self.entry_stock.place(x=150, y=140)
        
        
        self.btn_ingresar = tk.Button(ventana, text="Ingresar", command=self.guardar_datos)
        self.btn_ingresar.place(x=50, y=200)
        
        self.tabla = ttk.Treeview(ventana)
        self.tabla['columns'] = ("ID", "Titulo Libro", "Fecha", "Autor", "Stock")
        self.tabla.column("#0", width=0)
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Titulo Libro", text="Titulo Libro")
        self.tabla.heading("Autor", text="Autor")
        self.tabla.heading("Stock", text="Stock")
        self.tabla.place(x=325, y=50)
        
    def guardar_datos(self):

        id_value = self.entry_id.get()
        titulo_value = self.entry_titulo.get()
        autor_value = self.entry_autor.get()
        stock_value = self.entry_cantidad.get()
        

        self.tabla.insert("", "end", values=(id_value, titulo_value, autor_value, stock_value))
        
        self.entry_id.delete(0, tk.END)
        self.entry_titulo.delete(0, tk.END)
        self.entry_autor.delete(0, tk.END)
        self.entry_stock.delete(0, tk.END)