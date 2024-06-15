import customtkinter as cTK
import tkinter as tk
from tkinter import ttk

class FrameVerEditarEditorial():
    def __init__(self,ventana) -> None:
        self.ventana = ventana

        label_id = tk.Label(ventana, text="ID:")
        label_editorial = tk.Label(ventana, text="Editorial:")
        
        self.entry_id = tk.Entry(ventana)
        self.entry_editorial = tk.Entry(ventana)
        
        label_id.place(x=50, y=50)
        self.entry_id.place(x=180, y=50)
        
        label_editorial.place(x=50, y=80)
        self.entry_editorial.place(x=180, y=80)
        
        self.btn_ingresar = tk.Button(ventana, text="Ingresar", command=self.guardar_datos)
        self.btn_ingresar.place(x=50, y=110)
        
        self.btn_editar = tk.Button(ventana, text="Editar", command=self.editar_datos)
        self.btn_editar.place(x=150, y=110)

        self.tabla = ttk.Treeview(ventana)
        self.tabla['columns'] = ("ID", "Editorial")
        self.tabla.column("#0", width=0)
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Editorial", text="Nombre")
        self.tabla.place(x=325, y=50)
        
        self.tabla.bind("<ButtonRelease-1>", self.cargar_datos_seleccionados)
        
    def guardar_datos(self):
        id_value = self.entry_id.get()
        editorial_value = self.entry_editorial.get()
        
        self.tabla.insert("", "end", values=(id_value, editorial_value))
        
        self.entry_id.delete(0, tk.END)
        self.entry_editorial.delete(0, tk.END)

    def cargar_datos_seleccionados(self, event):
        item = self.tabla.selection()
        if item:
            values = self.tabla.item(item)['values']

            self.entry_id.delete(0, tk.END)
            self.entry_id.insert(0, values[0])
            self.entry_editorial.delete(0, tk.END)
            self.entry_editorial.insert(0, values[1])
    
    def editar_datos(self):

        item = self.tabla.selection()
        if item:

            id_value = self.entry_id.get()
            editorial_value = self.entry_editorial.get()

            self.tabla.item(item, values=(id_value, editorial_value))
            
            self.entry_id.delete(0, tk.END)
            self.entry_editorial.delete(0, tk.END)
