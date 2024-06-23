from customtkinter import * 
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from Controlador.controladorFunciones import ControladorFunciones
from Modelo.conexion import editar
# En esta clase se cargan los frames de cada boton dedicados solamente a la edición de datos de la BD
class EditarFrames():
    def __init__(self,master, callback) -> None:
        self.master = master
        self.callback = callback
        self.controlador_funciones = ControladorFunciones()
    #modulo de view editar compras
    def EditarCompras(self):
        #genera los label
        label_id = CTkLabel(self.master, text="ID:")
        label_titulo = CTkLabel(self.master, text="Título Libro:")
        label_fecha = CTkLabel(self.master, text="Fecha:")
        label_cantidad = CTkLabel(self.master, text="Cantidad Comprada:")
        label_total = CTkLabel(self.master, text="Total Compra:")

        tabla = ttk.Treeview(self.master)
        
        #genera las cajas de texto
        self.entry_id = CTkEntry(self.master)
        self.entry_titulo = CTkEntry(self.master)
        self.entry_fecha = CTkEntry(self.master)
        self.entry_cantidad = CTkEntry(self.master)
        self.entry_total = CTkEntry(self.master)
        
        label_id.place(x=50, y=50)
        self.entry_id.place(x=180, y=50)
        
        label_titulo.place(x=50, y=80)
        self.entry_titulo.place(x=180, y=80)
        
        label_fecha.place(x=50, y=110)
        self.entry_fecha.place(x=180, y=110)
        
        label_cantidad.place(x=50, y=140)
        self.entry_cantidad.place(x=180, y=140)
        
        label_total.place(x=50, y=170)
        self.entry_total.place(x=180, y=170)
           
        self.btn_editar = CTkButton(self.master, text="Editar", command=None)
        self.btn_editar.place(x=150, y=200)
        
        query = """SELECT detalle_movimiento.ID, libro.Titulo, movimiento.Fecha, 
                   detalle_movimiento.Cantidad, movimiento.Total_neto 
                   FROM detalle_movimiento 
                   INNER JOIN movimiento ON movimiento.ID = detalle_movimiento.ID_Movimiento 
                   INNER JOIN libro ON libro.ID = detalle_movimiento.ID_Libro 
                   WHERE movimiento.ID_Tipo_movimiento = 2;"""
        # Crear tabla
        self.tabla = ttk.Treeview(self.master)
        self.tabla['columns'] = ("ID", "Titulo Libro", "Fecha", "Cantidad Comprada", "Total Compra")

        #acomoda las columnas de la tabla
        self.tabla.column("#0", width=0)
        self.tabla.column("ID",width=20)
        self.tabla.column("Titulo Libro",width=170)
        self.tabla.column("Fecha",width=170)
        self.tabla.column("Cantidad Comprada",width=170)
        self.tabla.column("Total Compra",width=170)

        #le da el texto de titulos a la tabla
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Titulo Libro", text="Titulo Libro")
        self.tabla.heading("Fecha", text="Fecha")
        self.tabla.heading("Cantidad Comprada", text="Cantidad Comprada")
        self.tabla.heading("Total Compra", text="Total Compra")
        self.tabla.place(relx=0.5, rely=0.6,anchor=CENTER)

        self.callback(tabla, query)

    def EditarEditoriales(self):
        self.tabla = ttk.Treeview(self.master)
        query = "SELECT * FROM editorial;"

        label_id = tk.Label(self.master, text="ID:")
        label_editorial = tk.Label(self.master, text="Editorial:")
        
        self.entry_id = tk.Entry(self.master)
        self.entry_editorial = tk.Entry(self.master)
        
        label_id.place(x=50, y=50)
        self.entry_id.place(x=180, y=50)
        
        label_editorial.place(x=50, y=80)
        self.entry_editorial.place(x=180, y=80)
           
        self.btn_editar = CTkButton(self.master, text="Editar", command=editar)
        self.btn_editar.place(x=150, y=110)

        self.tabla['columns'] = ("1", "2")
        self.tabla.column("#0", width=0)
        self.tabla.heading("1", text="ID")
        self.tabla.heading("2", text="Nombre")
        self.tabla.place(relx=0.5, rely=0.6,anchor=CENTER)

        self.tabla.bind("<ButtonRelease-1>", self.seleccionar_datos)
        
        self.callback(self.tabla, query)

    def EditarProductos(self):
        label_id = CTkLabel(self.master, text="ID:")
        label_titulo = CTkLabel(self.master, text="Título:")
        label_autor = CTkLabel(self.master, text="Autor:")
        label_stock = CTkLabel(self.master, text="Stock:")
        
        self.entry_id = CTkEntry(self.master)
        self.entry_titulo = CTkEntry(self.master)
        self.entry_autor = CTkEntry(self.master)
        self.entry_stock = CTkEntry(self.master)

        
        label_id.place(x=50, y=50)
        self.entry_id.place(x=180, y=50)
        
        label_titulo.place(x=50, y=80)
        self.entry_titulo.place(x=180, y=80)
        
        label_autor.place(x=50, y=110)
        self.entry_autor.place(x=180, y=110)
        
        label_stock.place(x=50, y=140)
        self.entry_stock.place(x=180, y=140)
        
        self.btn_editar = CTkButton(self.master, text="Editar", command=None)
        self.btn_editar.place(x=150, y=200)
        
        # Crear tabla
        self.tabla = ttk.Treeview(self.master)
        self.tabla['columns'] = ("ID", "Titulo", "Autor", "Stock")
        self.tabla.column("#0", width=0)
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Titulo", text="Titulo")
        self.tabla.heading("Autor", text="Autor")
        self.tabla.heading("Stock", text="Stock")
        self.tabla.place(relx=0.5, rely=0.6,anchor=CENTER)

    def EditarProveedores(self):
        label_id = CTkLabel(self.master, text="ID:")
        label_proveedor = CTkLabel(self.master, text="Proveedor:")
        
        self.entry_id = CTkEntry(self.master)
        self.entry_proveedor = CTkEntry(self.master)
        
        label_id.place(x=50, y=50)
        self.entry_id.place(x=180, y=50)
        
        label_proveedor.place(x=50, y=80)
        self.entry_proveedor.place(x=180, y=80)
        
        self.btn_editar = CTkButton(self.master, text="Editar", command=None)
        self.btn_editar.place(x=150, y=110)

        self.tabla = ttk.Treeview(self.master)
        self.tabla['columns'] = ("ID", "Editorial")
        self.tabla.column("#0", width=0)
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Editorial", text="Nombre")
        self.tabla.place(relx=0.5, rely=0.6,anchor=CENTER)


    
    def seleccionar_datos(self, event):
        try:
            item = self.tabla.selection()
            values = self.tabla.item(item)['values']

            self.entry_id.delete(0, tk.END)
            self.entry_id.insert(0, values[0])
            self.entry_editorial.delete(0, tk.END)
            self.entry_editorial.insert(0, values[1])
        except:
                titulo = 'Edicion de datos'
                mensaje = 'No ha seleccionado ningun registro'
                messagebox.showerror(titulo, mensaje)
    

     
                
                
    
