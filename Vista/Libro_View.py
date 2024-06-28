from customtkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
from Controlador.controladorFunciones import ControladorFunciones

class Libro:
    def __init__(self, master):
        self.master = master
        self.controladorFun = ControladorFunciones()
        
        # Frame principal para contenidos
        self.main_frame = CTkFrame(self.master)
        self.main_frame.pack(side=RIGHT,fill=BOTH, expand=True)
        
        # Frame para la botonera
        self.botonera_frame = CTkFrame(self.master)
        self.botonera_frame.pack(side=LEFT, fill=Y)

        self.Botonera_place()
    
    def Botonera_place(self):
        # Botones en la botonera
        boton_ingresar = CTkButton(self.botonera_frame, text="Ingresar", command=self.IngresarLibro)
        boton_ingresar.pack(pady=10, padx=10, fill=X)

        boton_editar = CTkButton(self.botonera_frame, text="Editar", command=self.EditarLibro)
        boton_editar.pack(pady=10, padx=10, fill=X)

        boton_ver = CTkButton(self.botonera_frame, text="Ver", command=self.VerLibros)
        boton_ver.pack(pady=10, padx=10, fill=X)
    
    def limpiar_main_frame(self):
        # Limpiar el frame principal antes de añadir nuevos widgets
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def EditarLibro(self):
        self.limpiar_main_frame()
        label_id = CTkLabel(self.main_frame, text="ID:")
        label_titulo = CTkLabel(self.main_frame, text="Título:")
        label_autor = CTkLabel(self.main_frame, text="Autor:")
        label_stock = CTkLabel(self.main_frame, text="Stock:")
        
        self.entry_id = CTkEntry(self.main_frame)
        self.entry_titulo = CTkEntry(self.main_frame)
        self.entry_autor = CTkEntry(self.main_frame)
        self.entry_stock = CTkEntry(self.main_frame)

        
        label_id.place(x=50, y=50)
        self.entry_id.place(x=180, y=50)
        
        label_titulo.place(x=50, y=80)
        self.entry_titulo.place(x=180, y=80)
        
        label_autor.place(x=50, y=110)
        self.entry_autor.place(x=180, y=110)
        
        label_stock.place(x=50, y=140)
        self.entry_stock.place(x=180, y=140)
        
        self.btn_editar = CTkButton(self.main_frame, text="Editar", command=None)
        self.btn_editar.place(x=150, y=200)
        
        query = "SELECT * FROM libro;"
        # Crear tabla
        self.tabla = ttk.Treeview(self.main_frame)
        self.tabla['columns'] = ("ID", "Titulo", "Autor", "Stock")
        self.tabla.column("#0", width=0)
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Titulo", text="Titulo")
        self.tabla.heading("Autor", text="Autor")
        self.tabla.heading("Stock", text="Stock")
        self.tabla.place(relx=0.5, rely=0.6,anchor=CENTER)
        self.tabla.bind("<ButtonRelease-1>", self.seleccionar_datos)
        self.controladorFun.cargarDatos(self.tabla, query)

    def IngresarLibro(self):
        self.limpiar_main_frame()
        label_titulo = CTkLabel(self.main_frame, text="Título:")
        label_stock = CTkLabel(self.main_frame, text="Stock:")
        
        self.entry_titulo = CTkEntry(self.main_frame)
        self.entry_stock = CTkEntry(self.main_frame)

      
        label_titulo.place(x=50, y=80)
        self.entry_titulo.place(x=150, y=80)
        
        label_stock.place(x=50, y=110)
        self.entry_stock.place(x=150, y=110)
        
        self.btn_ingresar = CTkButton(
            self.master,
            text="Ingresar",
            command=lambda:ControladorFunciones.insertar_datos(
                "libro",
                ["titulo", "stock"],
                [self.entry_titulo.get(), self.entry_stock.get()]
            )
        )
        self.btn_ingresar.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    def VerLibros(self):
        self.limpiar_main_frame()

        buscador = CTkEntry(self.main_frame)
        tabla = ttk.Treeview(self.main_frame)
        # Se realiza un query especifico para la tabla de productos
        # esta debe mostrar titulo,autor,stock del libro
        query = "SELECT * FROM libro;"
        boton_bus = CTkButton(self.main_frame, text="Buscar", command=lambda: self.controladorFun._buscarElemento(tabla, buscador, query))
        # crea columnas
        tabla['columns'] = ("1", "2", "3", "4")
        # cambia ancho de columna id
        tabla.column("#0", width=0, stretch=False)
        tabla.column("#1", width=40, stretch=False)
        # agrega texto a los headings de las columnas
        tabla.heading("1", text="ID")
        tabla.heading("2", text="Titulo")
        tabla.heading("3", text="Autor")
        tabla.heading("4", text="Stock")

        buscador.pack(padx=10, pady=5, side=TOP, fill=X)
        boton_bus.pack(padx=10, pady=5, side=TOP, fill=X)
        tabla.pack(padx=10, pady=10, expand=True, fill=BOTH)
        
        self.controladorFun.cargarDatos(tabla, query)
    
    def seleccionar_datos(self, event):
        try:
            item = self.tabla.focus()
            values = self.tabla.item(item)['values']
            print(values)

            self.entry_id.delete(0, tk.END)
            self.entry_id.insert(0, values[0])
            self.entry_titulo.delete(0, tk.END)
            self.entry_titulo.insert(0, values[1])
        except:
            titulo = 'Edición de datos'
            mensaje = 'No ha seleccionado ningún registro'
            messagebox.showerror(titulo, mensaje)

