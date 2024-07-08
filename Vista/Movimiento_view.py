from customtkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
from PIL import Image
from Controlador.controladorFunciones import ControladorFunciones
from Modelo.conexion import obtenerProveedores, obtenerLibro

class Movimiento:
    def __init__(self, master):
        self.master = master
        self.controladorFun = ControladorFunciones()
        
        # Frame principal para contenidos
        self.main_frame = CTkFrame(self.master)
        self.main_frame.pack(side=RIGHT,fill=BOTH, expand=True)
        
        # Frame para la botonera
        self.botonera_frame = CTkFrame(self.master)
        self.botonera_frame.pack(side=LEFT, fill=Y)
        my_image = CTkImage(light_image=Image.open("Vista/img/libreria.png"),
                                  size=(160,160))
        CTkLabel(self.main_frame, image=my_image, text="").place(relx=0.5, rely=0.5, anchor=CENTER)
        self.Botonera_place()
    
    def Botonera_place(self):
        # Botones en la botonera
        boton_ingresar = CTkButton(self.botonera_frame, text="Ingresar", command=self.IngresarMovimientos)
        boton_ingresar.pack(pady=10, padx=10, fill=X)

        boton_editar = CTkButton(self.botonera_frame, text="Editar", command=self.EditarMovimientos)
        boton_editar.pack(pady=10, padx=10, fill=X)

        boton_ver = CTkButton(self.botonera_frame, text="Ver", command=self.VerMovimientos)
        boton_ver.pack(pady=10, padx=10, fill=X)
    
    def limpiar_main_frame(self):
        # Limpiar el frame principal antes de añadir nuevos widgets
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def EditarMovimientos(self):
        self.limpiar_main_frame()

        label_id= CTkLabel(self.main_frame,text="ID:")
        label_titulo= CTkLabel(self.main_frame, text="Titulo:")
        label_proveedor= CTkLabel(self.main_frame, text="Proveedor:")
        label_tipo= CTkLabel(self.main_frame, text="Tipo-movimiento:")
        label_fecha = CTkLabel(self.main_frame, text="Fecha:")
        label_cantidad= CTkLabel(self.main_frame, text="Cantidad:")
        label_total= CTkLabel(self.main_frame, text="Total:")
        
        self.entry_id= CTkEntry(self.main_frame,state=DISABLED)
        self.combo_titulo= CTkComboBox(self.main_frame,state="readonly",values=obtenerLibro())
        self.combo_proveedor= CTkComboBox(self.main_frame, state="readonly",values=obtenerProveedores())
        self.combo_tipo = CTkComboBox(self.main_frame, state="readonly",values=["Venta", "Compra"])
        self.entry_fecha = CTkEntry(self.main_frame)
        self.entry_cantidad= CTkEntry(self.main_frame)
        self.entry_total = CTkEntry(self.main_frame)
       
        label_id.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.entry_id.grid(row=0, column=1, padx=10, pady=10)
        
        label_titulo.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.combo_titulo.grid(row=1, column=1, padx=10, pady=10)
        
        label_proveedor.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.combo_proveedor.grid(row=2, column=1, padx=10, pady=10)

        label_tipo.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.combo_tipo.grid(row=3, column=1, padx=10, pady=10)

        label_fecha.grid(row=4, column=0, padx=10, pady=10, sticky="e")
        self.entry_fecha.grid(row=4, column=1, padx=10, pady=10)

        label_cantidad.grid(row=5, column=0, padx=10, pady=10, sticky="e")
        self.entry_cantidad.grid(row=5, column=1, padx=10, pady=10)

        label_total.grid(row=6, column=0, padx=10, pady=10, sticky="e")
        self.entry_total.grid(row=6, column=1, padx=10, pady=10)

        self.btn_editar = CTkButton(self.main_frame, text="Editar", state=DISABLED, 
        command=lambda: self.controladorFun.editar_datos(
            "movimiento",
            ["ID_Libro","ID_Proveedor","ID_Tipo_movimiento","Fecha","Cantidad","Total_neto"],
            [self.entry_id.get(),
            self.controladorFun.obtenerID("libro",self.combo_titulo.get()),
            self.controladorFun.obtenerID("proveedor",self.combo_proveedor.get()),
            self.controladorFun.obtenerID("tipo_movimiento",self.combo_tipo.get()),
            self.entry_fecha.get(),
            self.entry_cantidad.get(),
            self.entry_total.get()]
        ))

        self.btn_editar.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        query = """SELECT movimiento.ID, libro.Titulo, proveedor.Nombre, tipo_movimiento.Tipo, Fecha, Cantidad, Total_neto 
                    FROM movimiento 
                    INNER JOIN libro ON libro.ID = movimiento.ID_Libro 
                    INNER JOIN tipo_movimiento ON tipo_movimiento.ID = movimiento.ID_Tipo_movimiento
                    INNER JOIN proveedor ON proveedor.ID = movimiento.ID_Proveedor;
                    """
       
        self.tabla = ttk.Treeview(self.main_frame)
        self.tabla['columns'] = ("1", "2","3","4","5","6","7")
        self.tabla.column("#0", width=0, stretch=False)
        self.tabla.heading("1", text="ID")
        self.tabla.heading("2", text="Titulo")
        self.tabla.heading("3", text="Proveedor")
        self.tabla.heading("4", text="Movimiento")
        self.tabla.heading("5", text="Fecha")
        self.tabla.heading("6", text="Cantidad")
        self.tabla.heading("7", text="Total Neto")
        self.tabla.grid(row=9, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        self.tabla.bind("<ButtonRelease-1>", self.seleccionar_datos)
        self.controladorFun.cargarDatos(self.tabla, query)

    def IngresarMovimientos(self):
        self.limpiar_main_frame()

        label_titulo= CTkLabel(self.main_frame, text="Titulo:")
        label_proveedor= CTkLabel(self.main_frame, text="Proveedor:")
        label_tipo= CTkLabel(self.main_frame, text="Tipo-movimiento:")
        label_fecha = CTkLabel(self.main_frame, text="Fecha:")
        label_cantidad= CTkLabel(self.main_frame, text="Cantidad:")
        label_total= CTkLabel(self.main_frame, text="Total:")
        
        self.combo_titulo= CTkComboBox(self.main_frame,state="readonly",values=obtenerLibro())
        self.combo_proveedor= CTkComboBox(self.main_frame, state="readonly",values=obtenerProveedores())
        self.combo_tipo = CTkComboBox(self.main_frame, state="readonly",values=["Venta", "Compra"])
        self.entry_fecha = CTkEntry(self.main_frame)
        self.entry_cantidad= CTkEntry(self.main_frame)
        self.entry_total = CTkEntry(self.main_frame)
        
        label_titulo.place(x=50, y=40)
        self.combo_titulo.place(x=150, y=40)

        label_proveedor.place(x=50, y=110)
        self.combo_proveedor.place(x=150, y=110)

        label_tipo.place(x=50, y=180)
        self.combo_tipo.place(x=150, y=180)

        label_fecha.place(x=50, y=250)
        self.entry_fecha.place(x=150, y=250)

        label_cantidad.place(x=50, y=320)
        self.entry_cantidad.place(x=150, y=320)

        label_total.place(x=50, y=390)
        self.entry_total.place(x=150, y=390)

        self.btn_ingresar = CTkButton(
            self.main_frame,
            text="Ingresar",
            command=lambda: self.controladorFun.insertar_datos(
                "movimiento",
                ["ID_Tipo_movimiento", "Fecha", "Total_neto"],
                [self.controladorFun.obtenerID("libro",self.combo_titulo.get()),
                self.controladorFun.obtenerID("proveedor",self.combo_proveedor.get()),
                self.controladorFun.obtenerID("tipo_movimiento",self.combo_tipo.get()),
                self.entry_fecha.get(), 
                self.entry_cantidad.get(), 
                self.entry_total.get()]
            )
        )

        self.btn_ingresar.place(x=100, y=460)

    def VerMovimientos(self):
        self.limpiar_main_frame()

        buscador = CTkEntry(self.main_frame)
        buscador.pack(padx=10, pady=5, side=TOP, fill=X)

        boton_bus = CTkButton(self.main_frame, text="Buscar", command=lambda: self.controladorFun._buscarElemento(self.tabla, buscador, query))
        boton_bus.pack(padx=10, pady=5, side=TOP, fill=X)

        tabla = ttk.Treeview(self.main_frame)
        tabla['columns'] = ("1", "2","3","4","5","6","7")
        tabla.column("#0", width=0, stretch=False)
        tabla.heading("1", text="ID")
        tabla.heading("2", text="Titulo")
        tabla.heading("3", text="Proveedor")
        tabla.heading("4", text="Movimiento")
        tabla.heading("5", text="Fecha")
        tabla.heading("6", text="Cantidad")
        tabla.heading("7", text="Total Neto")
        tabla.pack(padx=10, pady=10, expand=True, fill=BOTH)

        botonLisCompra = CTkButton(self.main_frame, text="Imprimir Compras", command=lambda: self.controladorFun._generarPdf('compras'))
        botonLisCompra.pack(padx=10, pady=10, side=RIGHT, fill=BOTH)

        botonLisCompra = CTkButton(self.main_frame, text="Imprimir Ventas", command=lambda: self.controladorFun._generarPdf('ventas'))
        botonLisCompra.pack(padx=10, pady=10, side=RIGHT, fill=BOTH)

        botonEliminar = CTkButton(self.main_frame, text="Eliminar",
                                command=lambda: self.controladorFun.eliminar_elemento(tabla,"movimiento"))
        botonEliminar.pack(padx=10, pady=10, side=LEFT, fill=BOTH)

        query = """SELECT movimiento.ID, libro.Titulo, proveedor.Nombre, tipo_movimiento.Tipo, Fecha, Cantidad, Total_neto 
                    FROM movimiento 
                    INNER JOIN libro ON libro.ID = movimiento.ID_Libro 
                    INNER JOIN tipo_movimiento ON tipo_movimiento.ID = movimiento.ID_Tipo_movimiento
                    INNER JOIN proveedor ON proveedor.ID = movimiento.ID_Proveedor;
                    """
        
        self.controladorFun.cargarDatos(tabla, query)
    
    def seleccionar_datos(self, event):
        try:
            item = self.tabla.focus()
            values = self.tabla.item(item)['values']
            print(values)

            self.entry_id.configure(state=NORMAL)
            self.entry_id.delete(0, tk.END)
            self.entry_id.insert(0, values[0])
            self.entry_id.configure(state=DISABLED)
            self.combo_titulo.set(values[1])
            self.combo_proveedor.set(values[2])
            self.combo_tipo.set(values[3])
            self.entry_fecha.delete(0, tk.END)
            self.entry_fecha.insert(0, values[4])
            self.entry_cantidad.delete(0, tk.END)
            self.entry_cantidad.insert(0, values[5])
            self.entry_total.delete(0, tk.END)
            self.entry_total.insert(0, values[6])
            self.btn_editar.configure(state=NORMAL)

        except:
            titulo = 'Edición de datos'
            mensaje = 'No ha seleccionado ningún registro'
            messagebox.showerror(titulo, mensaje)

