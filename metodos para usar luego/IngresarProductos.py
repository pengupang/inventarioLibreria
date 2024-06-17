import customtkinter as cTK
import tkinter as tk
from tkinter import ttk

class FrameVerIngresarProductos(cTK.CTkFrame):
    def __init__(self,master) -> None:
        super().__init__(master)
        self.mostrarIngresarProductos()

    def mostrarIngresarProductos(self):
        label_id = cTK.CTkLabel(self, text="ID:")
        label_titulo = cTK.CTkLabel(self, text="Título:")
        label_stock = cTK.CTkLabel(self, text="Stock:")
        
        self.entry_id = cTK.CTkEntry(self)
        self.entry_titulo = cTK.CTkEntry(self)
        self.entry_stock = cTK.CTkEntry(self)
        
        label_id.place(x=50, y=50)
        self.entry_id.place(x=150, y=50)
        
        label_titulo.place(x=50, y=80)
        self.entry_titulo.place(x=150, y=80)
  
        label_stock.place(x=50, y=140)
        self.entry_stock.place(x=150, y=140)
        
        
        self.btn_ingresar =cTK.CTkButton(self, text="Ingresar", command=self.guardar_datos)
        self.btn_ingresar.place(x=50, y=200)
        
        self.tabla = ttk.Treeview(self)
        self.tabla['columns'] = ("ID", "Titulo Libro", "Fecha", "Stock")
        self.tabla.column("#0", width=0)
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Titulo Libro", text="Titulo Libro")
        self.tabla.heading("Stock", text="Stock")
        self.tabla.place(x=325, y=50)


    def guardar_datos(self):
        id_value = self.entry_id.get()
        titulo_value = self.entry_titulo.get()
        stock_value = self.entry_stock.get()

        # Preparar la consulta SQL para insertar los datos
        sql = "INSERT INTO libro (ID, Titulo, Stock) VALUES (%s, %s, %s)"
        val = (id_value, titulo_value, stock_value)

        # Ejecutar la consulta SQL
        self.cursor.execute(sql, val)

        # Confirmar la transacción
        self.conexion.commit()

        # Limpiar los campos de entrada después de la inserción
        self.entry_id.delete(0, tk.END)
        self.entry_titulo.delete(0, tk.END)
        self.entry_stock.delete(0, tk.END)