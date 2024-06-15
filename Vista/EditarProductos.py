import customtkinter as cTK
import tkinter as tk
from tkinter import ttk

class FrameVerEditarProductos():
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
        self.entry_id.place(x=180, y=50)
        
        label_titulo.place(x=50, y=80)
        self.entry_titulo.place(x=180, y=80)
        
        label_autor.place(x=50, y=110)
        self.entry_autor.place(x=180, y=110)
        
        label_stock.place(x=50, y=140)
        self.entry_stock.place(x=180, y=140)

        
        self.btn_ingresar = tk.Button(ventana, text="Ingresar", command=self.guardar_datos)
        self.btn_ingresar.place(x=50, y=200)
        
        self.btn_editar = tk.Button(ventana, text="Editar", command=self.editar_datos)
        self.btn_editar.place(x=150, y=200)
        
        # Crear tabla
        self.tabla = ttk.Treeview(ventana)
        self.tabla['columns'] = ("ID", "Titulo", "Autor", "Stock")
        self.tabla.column("#0", width=0)
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Titulo", text="Titulo")
        self.tabla.heading("Autor", text="Autor")
        self.tabla.heading("Stock", text="Stock")
        self.tabla.place(x=325, y=50)
        
        self.tabla.bind("<ButtonRelease-1>", self.cargar_datos_seleccionados)
        
    def guardar_datos(self):
        # Obtener datos de los Entries
        id_value = self.entry_id.get()
        titulo_value = self.entry_titulo.get()
        label_autor = self.entry_autor.get()
        label_stock = self.entry_stock.get()

        
        # Insertar datos en la tabla (Treeview)
        self.tabla.insert("", "end", values=(id_value, titulo_value, label_autor, label_stock))
        
        # Limpiar campos después de ingresar datos
        self.entry_id.delete(0, tk.END)
        self.entry_titulo.delete(0, tk.END)
        self.entry_autor.delete(0, tk.END)
        self.entry_stock.delete(0, tk.END)

    
    def cargar_datos_seleccionados(self, event):
        item = self.tabla.selection()
        if item:
            values = self.tabla.item(item)['values']

            self.entry_id.delete(0, tk.END)
            self.entry_id.insert(0, values[0])
            self.entry_titulo.delete(0, tk.END)
            self.entry_titulo.insert(0, values[1])
            self.entry_autor.delete(0, tk.END)
            self.entry_autor.insert(0, values[2])
            self.entry_stock.delete(0, tk.END)
            self.entry_stock.insert(0, values[3])

    
    def editar_datos(self):

        item = self.tabla.selection()
        if item:

            id_value = self.entry_id.get()
            titulo_value = self.entry_titulo.get()
            label_autor = self.entry_autor.get()
            label_stock = self.entry_stock.get()

            
            self.tabla.item(item, values=(id_value, titulo_value, label_autor, label_stock))
            
            self.entry_id.delete(0, tk.END)
            self.entry_titulo.delete(0, tk.END)
            self.entry_autor.delete(0, tk.END)
            self.entry_stock.delete(0, tk.END)

