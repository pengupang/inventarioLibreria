from customtkinter import *
from tkinter import ttk
from tkinter import messagebox as mb

class EliminarFrames():
    def __init__(self,master,callback,barraBusqueda,eliminarEle):
        self.master = master
        self.callback = callback
        self.barraBusqueda = barraBusqueda
        self.eliminarEle = eliminarEle

    def setup_pack(self, tabla,buscador,boton_bus,boton_eli):
        buscador.pack(padx=10, pady=5, side=TOP, fill=X)
        boton_bus.pack(padx=10, pady=5, side=TOP, fill=X)
        tabla.pack(padx=10, pady=10, expand=True, fill=BOTH)
        boton_eli.pack(padx=10, pady=10)


    def eliminarCompras(self):
        buscador = CTkEntry(self.master)
        tabla = ttk.Treeview(self.master)
        boton_bus = CTkButton(self.master, text="Buscar", command=lambda: self.barraBusqueda(tabla, buscador, query))
        self.boton_eli = CTkButton(self.master, text="Eliminar",state="disabled", command=lambda: self.eliminarEle(tabla))
        query = """SELECT detalle_movimiento.ID, libro.Titulo, movimiento.Fecha, 
                   detalle_movimiento.Cantidad, movimiento.Total_neto 
                   FROM detalle_movimiento 
                   INNER JOIN movimiento ON movimiento.ID = detalle_movimiento.ID_Movimiento 
                   INNER JOIN libro ON libro.ID = detalle_movimiento.ID_Libro 
                   WHERE movimiento.ID_Tipo_movimiento = 2;"""
        tabla['columns'] = ("1", "2", "3", "4", "5")
        tabla.column("#0", width=0, stretch=False)
        tabla.column("#1", width=65, stretch=False)
        tabla.heading("1", text="ID")
        tabla.heading("2", text="Titulo Libro")
        tabla.heading("3", text="Fecha")
        tabla.heading("4", text="Cantidad Comprada")
        tabla.heading("5", text="Total Compra")
        self.setup_pack(tabla,buscador,boton_bus,self.boton_eli)
        self.callback(tabla,query)
        tabla.bind("<<TreeviewSelect>>", self.cambiar_boton)

    def eliminarEditoriales(self):
        buscador = CTkEntry(self.master)
        tabla = ttk.Treeview(self.master)
        query = "SELECT * FROM editorial;"
        boton_bus = CTkButton(self.master, text="Buscar", command=lambda: self.barraBusqueda(tabla, buscador, query))
        self.boton_eli = CTkButton(self.master, text="Eliminar",state="disabled", command=lambda: self.eliminarEle(tabla))
        tabla['columns'] = ("1", "2")
        tabla.column("#0", width=0, stretch=False)
        tabla.heading("1", text="ID")
        tabla.heading("2", text="Nombre")
        self.setup_pack(tabla, buscador, boton_bus,self.boton_eli)
        self.callback(tabla, query)
        tabla.bind("<<TreeviewSelect>>", self.cambiar_boton)

    def eliminarProductos(self):
        buscador = CTkEntry(self.master)
        tabla = ttk.Treeview(self.master)
        query = """SELECT libro.ID, Titulo, Autor.nombre, Stock 
                   FROM libro 
                   INNER JOIN autor_libro ON libro.ID = autor_libro.ID_Libro
                   INNER JOIN autor ON autor.ID = autor_libro.ID_Autor"""
        boton_bus = CTkButton(self.master, text="Buscar", command=lambda: self.barraBusqueda(tabla, buscador, query))
        self.boton_eli = CTkButton(self.master, text="Eliminar",state="disabled", command=lambda: self.eliminarEle(tabla))
        tabla['columns'] = ("1", "2", "3", "4")
        tabla.column("#0", width=0, stretch=False)
        tabla.column("#1", width=40, stretch=False)
        tabla.heading("1", text="ID")
        tabla.heading("2", text="Titulo")
        tabla.heading("3", text="Autor")
        tabla.heading("4", text="Stock")
        self.setup_pack(tabla, buscador, boton_bus,self.boton_eli)
        self.callback(tabla, query)
        tabla.bind("<<TreeviewSelect>>", self.cambiar_boton)

    def eliminarProveedores(self):
        buscador = CTkEntry(self.master)
        tabla = ttk.Treeview(self.master)
        query = "SELECT * FROM proveedor;"
        boton_bus = CTkButton(self.master, text="Buscar", command=lambda: self.barraBusqueda(tabla, buscador, query))
        self.boton_eli = CTkButton(self.master, text="Eliminar",state="disabled", command=lambda: self.eliminarEle(tabla))
        tabla['columns'] = ("1", "2")
        tabla.column("#0", width=0, stretch=False)
        tabla.column("#1", width=20, stretch=False)
        tabla.heading("1", text="ID")
        tabla.heading("2", text="Nombre")
        self.setup_pack(tabla, buscador, boton_bus,self.boton_eli)
        self.callback(tabla, query)
        tabla.bind("<<TreeviewSelect>>", self.cambiar_boton)

    def eliminarVentas(self):
        buscador = CTkEntry(self.master)
        query = """SELECT detalle_movimiento.ID, libro.Titulo, movimiento.Fecha, 
                   detalle_movimiento.Cantidad, movimiento.Total_neto 
                   FROM detalle_movimiento 
                   INNER JOIN movimiento ON movimiento.ID = detalle_movimiento.ID_Movimiento 
                   INNER JOIN libro ON libro.ID = detalle_movimiento.ID_Libro 
                   WHERE movimiento.ID_Tipo_movimiento = 1;"""
        tabla = ttk.Treeview(self.master)
        boton_bus = CTkButton(self.master, text="Buscar", command=lambda: self.barraBusqueda(tabla, buscador, query))
        self.boton_eli = CTkButton(self.master, text="Eliminar",state="disabled", command=lambda: self.eliminarEle(tabla))
        tabla['columns'] = ("1", "2", "3", "4", "5")
        tabla.column("#0", width=0, stretch=False)
        tabla.heading("1", text="ID")
        tabla.heading("2", text="Titulo Libro")
        tabla.heading("3", text="Fecha")
        tabla.heading("4", text="Cantidad Vendida")
        tabla.heading("5", text="Total venta")
        self.setup_pack(tabla, buscador, boton_bus,self.boton_eli)
        self.callback(tabla, query)
        tabla.bind("<<TreeviewSelect>>", self.cambiar_boton)
    
    def cambiar_boton(self,event):
        self.boton_eli.configure(state="normal")   
