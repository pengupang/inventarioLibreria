from customtkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
from Controlador.controladorFunciones import ControladorFunciones

class Movimiento:
    def __init__(self, master):
        self.master = master
        
        # Frame principal para contenidos
        self.main_frame = CTkFrame(self.master)
        self.main_frame.pack(side=RIGHT,fill=BOTH, expand=True)
        
        # Frame para la botonera
        self.botonera_frame = CTkFrame(self.master)
        self.botonera_frame.pack(side=LEFT, fill=Y)

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
        label_proveedor = CTkLabel(self.main_frame, text="Proveedor:")
        
        self.entry_id = CTkEntry(self.main_frame)
        self.entry_proveedor = CTkEntry(self.main_frame)
        
        label_id.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.entry_id.grid(row=0, column=1, padx=10, pady=10)
        
        label_proveedor.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.entry_proveedor.grid(row=1, column=1, padx=10, pady=10)
        
        self.btn_editar = CTkButton(self.main_frame, text="Editar", command=None)
        self.btn_editar.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        
        query = "SELECT * FROM autor"
        self.tabla = ttk.Treeview(self.main_frame)
        self.tabla['columns'] = ("ID", "Editorial")
        self.tabla.column("#0", width=0)
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Editorial", text="Nombre")
        self.tabla.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        self.tabla.bind("<ButtonRelease-1>", self.seleccionar_datos)
        ControladorFunciones.cargarDatos(self, self.tabla, query)

    def IngresarMovimientos(self):
        self.limpiar_main_frame()
        label_idtype = CTkLabel(self.main_frame, text="Id del tipo de movimiento:")
        label_fecha = CTkLabel(self.main_frame, text="Fecha:")
        label_total = CTkLabel(self.main_frame, text="Total Movimiento:")
        
        self.entry_idtype = CTkEntry(self.main_frame)
        self.entry_fecha = CTkEntry(self.main_frame)
        self.entry_total = CTkEntry(self.main_frame)
        
        label_idtype.place(x=50, y=80)
        self.entry_idtype.place(x=150, y=80)

        label_fecha.place(x=50, y=110)
        self.entry_fecha.place(x=150, y=110)

        label_total.place(x=50, y=170)
        self.entry_total.place(x=150, y=170)

        self.btn_ingresar = CTkButton(
            self.main_frame,
            text="Ingresar",
            command=lambda:ControladorFunciones.insertar_datos(
                "movimiento",
                ["ID_Tipo_movimiento", "Fecha", "Total_neto"],
                [self.entry_idtype.get(), self.entry_fecha.get(), self.entry_total.get()]
            )
        )
        

        self.btn_ingresar.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    def VerMovimientos(self):
        self.limpiar_main_frame()

        buscador = CTkEntry(self.main_frame)
        buscador.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        
        boton_bus = CTkButton(self.main_frame, text="Buscar", command=lambda: self.barraBusqueda(self.tabla, buscador, query))
        boton_bus.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        
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
        tabla.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        query = """SELECT movimiento.ID, libro.Titulo, proveedor.Nombre, tipo_movimiento.Tipo, Fecha, Cantidad, Total_neto 
                    FROM movimiento 
                    INNER JOIN libro ON libro.ID = movimiento.ID_Libro 
                    INNER JOIN tipo_movimiento ON tipo_movimiento.ID = movimiento.ID_Tipo_movimiento
                    INNER JOIN proveedor ON proveedor.ID = movimiento.ID_Proveedor;
                    """
        ControladorFunciones.cargarDatos(self, tabla, query)
    
    def seleccionar_datos(self, event):
        try:
            item = self.tabla.selection()
            values = self.tabla.item(item)['values']

            self.entry_id.delete(0, tk.END)
            self.entry_id.insert(0, values[0])
            self.entry_proveedor.delete(0, tk.END)
            self.entry_proveedor.insert(0, values[1])
        except:
            titulo = 'Edición de datos'
            mensaje = 'No ha seleccionado ningún registro'
            messagebox.showerror(titulo, mensaje)

