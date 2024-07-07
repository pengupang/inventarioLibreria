from customtkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
from PIL import Image
from Controlador.controladorFunciones import ControladorFunciones

class Autores:
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
        boton_ingresar = CTkButton(self.botonera_frame, text="Ingresar", command=self.IngresarAutor)
        boton_ingresar.pack(pady=10, padx=10, fill=X)

        boton_editar = CTkButton(self.botonera_frame, text="Editar", command=self.EditarAutores)
        boton_editar.pack(pady=10, padx=10, fill=X)

        boton_ver = CTkButton(self.botonera_frame, text="Ver", command=self.VerAutores)
        boton_ver.pack(pady=10, padx=10, fill=X)
    
    def limpiar_main_frame(self):
        # Limpiar el frame principal antes de añadir nuevos widgets
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def EditarAutores(self):
        self.limpiar_main_frame()

        label_id = CTkLabel(self.main_frame, text="ID:")
        label_autor = CTkLabel(self.main_frame, text="Autor:")
        
        self.entry_id = CTkEntry(self.main_frame,state=DISABLED)
        self.entry_autor = CTkEntry(self.main_frame)
        
        label_id.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.entry_id.grid(row=0, column=1, padx=10, pady=10)
        
        label_autor.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.entry_autor.grid(row=1, column=1, padx=10, pady=10)
        
        self.btn_editar = CTkButton(self.main_frame, text="Editar", state=DISABLED,
        command=lambda: self.controladorFun.editar_datos(
            "autor",
            ["Nombre"],
            [self.entry_id.get(),
            self.entry_autor.get()]
        ))

        self.btn_editar.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        
        query = "SELECT * FROM autor"
        self.tabla = ttk.Treeview(self.main_frame)
        self.tabla['columns'] = ("ID", "Autor")
        self.tabla.column("#0", width=0)
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Autor", text="Nombre")
        self.tabla.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        self.tabla.bind("<ButtonRelease-1>", self.seleccionar_datos)
        self.controladorFun.cargarDatos(self.tabla, query)

    def IngresarAutor(self):
        self.limpiar_main_frame()

        label_nombre = CTkLabel(self.main_frame, text="Nombre:")
        self.entry_nombre = CTkEntry(self.main_frame)
        
        label_nombre.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)
        
        self.btn_ingresar = CTkButton(
            self.main_frame,
            text="Ingresar",
            command=lambda: self.controladorFun.insertar_datos(
                "autor",
                ["Nombre"],
                [self.entry_nombre.get()]
            )
        )
        self.btn_ingresar.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    def VerAutores(self):
        self.limpiar_main_frame()

        buscador = CTkEntry(self.main_frame)
        buscador.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        
        boton_bus = CTkButton(self.main_frame, text="Buscar", command=lambda: self.controladorFun._buscarElemento(self.tabla, buscador, query))
        boton_bus.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        
        tabla = ttk.Treeview(self.main_frame)
        tabla['columns'] = ("1", "2")
        tabla.column("#0", width=0, stretch=False)
        tabla.heading("1", text="ID")
        tabla.heading("2", text="Nombre")
        tabla.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        botonEliminar = CTkButton(self.main_frame, text="Eliminar",
                                command=lambda: self.controladorFun.eliminar_elemento(tabla,"autor"))
        botonEliminar.grid(row=2,column=0,padx=10,pady=10)

        query = "SELECT * FROM autor;"
        self.controladorFun.cargarDatos(tabla, query)
    
    def seleccionar_datos(self, event):
        try:
            item = self.tabla.focus()
            values = self.tabla.item(item)['values']

            self.entry_id.configure(state=NORMAL)
            self.entry_id.delete(0, tk.END)
            self.entry_id.insert(0, values[0])
            self.entry_id.configure(state=DISABLED)
            self.entry_autor.delete(0, tk.END)
            self.entry_autor.insert(0, values[1])
            self.btn_editar.configure(state=NORMAL)
        except:
            titulo = 'Edición de datos'
            mensaje = 'No ha seleccionado ningún registro'
            messagebox.showerror(titulo, mensaje)

