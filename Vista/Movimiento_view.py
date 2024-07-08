from customtkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
from PIL import Image
from Controlador.controladorFunciones import ControladorFunciones

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

        label_id = CTkLabel(self.main_frame, text="ID:")
        label_Movimiento= CTkLabel(self.main_frame, text="Proveedor:")
        
        self.entry_id = CTkEntry(self.main_frame, state=DISABLED)
        self.entry_Movimiento= CTkEntry(self.main_frame)
        
        label_id.place(relx=0.3, y=50)
        self.entry_id.place(relx=0.4, y=50)
        
        label_Movimiento.place(relx=0.3, y=80)
        self.entry_Movimiento.place(relx=0.4, y=80)
        
        self.btn_editar = CTkButton(self.main_frame, text="Editar", 
        command=lambda: self.controladorFun.editar_datos(
            "movimiento",
            ["Nombre"],
            [self.entry_id.get(),
            self.entry_Movimiento.get()]
        ))

        self.btn_editar.place(relx=0.4, y=110)
        
        
        query = "SELECT * FROM autor"
        self.tabla = ttk.Treeview(self.main_frame)
        self.tabla['columns'] = ("ID", "Editorial")
        self.tabla.column("#0", width=0)
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Editorial", text="Nombre")
        self.tabla.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.35)
        self.tabla.bind("<ButtonRelease-1>", self.seleccionar_datos)
        self.controladorFun.cargarDatos(self.tabla, query)

    def IngresarMovimientos(self):
        self.limpiar_main_frame()
        label_idtype = CTkLabel(self.main_frame, text="Id del tipo de movimiento:")
        label_fecha = CTkLabel(self.main_frame, text="Fecha:")
        label_total = CTkLabel(self.main_frame, text="Total Movimiento:")
        
        self.entry_idtype = CTkEntry(self.main_frame)
        self.entry_fecha = CTkEntry(self.main_frame)
        self.entry_total = CTkEntry(self.main_frame)
        
        label_idtype.pack(padx=10, pady=10)
        self.entry_idtype.pack(padx=10, pady=10)

        label_fecha.pack(padx=10, pady=10)
        self.entry_fecha.pack(padx=10, pady=10)

        label_total.pack(padx=10, pady=10)
        self.entry_total.pack(padx=10, pady=10)

        self.btn_ingresar = CTkButton(
            self.main_frame,
            text="Ingresar",
            command=lambda: self.controladorFun.insertar_datos(
                "movimiento",
                ["ID_Tipo_movimiento", "Fecha", "Total_neto"],
                [self.entry_idtype.get(), self.entry_fecha.get(), self.entry_total.get()]
            )
        )
        

        self.btn_ingresar.pack(padx=10, pady=10)

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

            self.entry_id.configure(state=NORMAL)
            self.entry_id.delete(0, tk.END)
            self.entry_id.insert(0, values[0])
            self.entry_id.configure(state=DISABLED)
            self.entry_Movimiento.delete(0, tk.END)
            self.entry_Movimiento.insert(0, values[1])
        except:
            titulo = 'Edición de datos'
            mensaje = 'No ha seleccionado ningún registro'
            messagebox.showerror(titulo, mensaje)

