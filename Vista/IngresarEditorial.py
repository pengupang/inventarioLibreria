import customtkinter as cTK
import tkinter as tk
from tkinter import ttk

class FrameVerIngresarEditorial():
    def __init__(self,ventana) -> None:
        self.ventana = ventana

        label_id = tk.Label(ventana, text="ID:")
        label_editorial = tk.Label(ventana, text="Editorial:")
        
        self.entry_id = tk.Entry(ventana)
        self.entry_editorial = tk.Entry(ventana)
        
        label_id.place(x=50, y=50)
        self.entry_id.place(x=150, y=50)
        
        label_editorial.place(x=50, y=80)
        self.entry_editorial.place(x=150, y=80)
        
        self.btn_ingresar = tk.Button(ventana, text="Ingresar", command=self.guardar_datos)
        self.btn_ingresar.place(x=50, y=100)
        
        self.tabla = ttk.Treeview(ventana)
        self.tabla['columns'] = ("ID", "Nombre")
        self.tabla.column("#0", width=0)
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.place(x=325, y=50)
        
    def guardar_datos(self):

        id_value = self.entry_id.get()
        label_editorial = self.entry_editorial.get()

        self.tabla.insert("", "end", values=(id_value, label_editorial))
        
        self.entry_id.delete(0, tk.END)
        self.entry_editorial.delete(0, tk.END)
