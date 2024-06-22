from customtkinter import * 
from tkinter import ttk

class EditarFrames(CTkFrame):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    def EditarProductos(self):
        # Crear un frame para los labels y entries
        frame_form = CTkFrame(self)
        frame_form.pack(side=TOP, fill=X, pady=10)

        # Generar los labels y entries
        label_id = CTkLabel(frame_form, text="ID:")
        self.entry_id = CTkEntry(frame_form)

        label_titulo = CTkLabel(frame_form, text="Título:")
        self.entry_titulo = CTkEntry(frame_form)

        label_autor = CTkLabel(frame_form, text="Autor:")
        self.entry_autor = CTkEntry(frame_form)

        label_stock = CTkLabel(frame_form, text="Stock:")
        self.entry_stock = CTkEntry(frame_form)

        # Ubicar los widgets en una cuadrícula
        label_id.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_id.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        label_titulo.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_titulo.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        label_autor.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_autor.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        label_stock.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.entry_stock.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        # Crear un frame para los botones
        frame_buttons = CTkFrame(self)
        frame_buttons.pack(side=TOP, fill=X, pady=10)

        # Generar botones
        self.btn_ingresar = CTkButton(frame_buttons, text="Ingresar", command=None)
        self.btn_ingresar.pack(side=LEFT, padx=5, pady=5)

        self.btn_editar = CTkButton(frame_buttons, text="Editar", command=None)
        self.btn_editar.pack(side=LEFT, padx=5, pady=5)

        # Crear tabla
        self.tabla = ttk.Treeview(self)
        self.tabla['columns'] = ("ID", "Titulo", "Autor", "Stock")
        self.tabla.column("#0", width=0)
        self.tabla.column("ID", width=20)
        self.tabla.column("Titulo", width=170)
        self.tabla.column("Autor", width=170)
        self.tabla.column("Stock", width=170)

        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Titulo", text="Titulo")
        self.tabla.heading("Autor", text="Autor")
        self.tabla.heading("Stock", text="Stock")
        self.tabla.pack(fill=BOTH, expand=True, padx=10, pady=10)