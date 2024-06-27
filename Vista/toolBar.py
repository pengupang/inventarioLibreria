import tkinter as tk
from tkinter import Frame

class ToolBar(Frame):
    def __init__(self, master, callback):
        super().__init__(master)
        self.callback = callback
        self.menu_frame = Frame(master, background="gray")
        self.menu_frame.pack(side="top", fill="x")
        self.crear_botones()

    def crear_botones(self):
        # Crear el botón Autores
        autores = tk.Button(self.menu_frame, text="Autores", background="gray", foreground="white",
                            activeforeground="black", activebackground="gray52", command=lambda: self.enviar_senal("VistaAutores"))
        autores.pack(side="left", padx=2, pady=2)

          # Crear el botón Editorial
        editorial = tk.Button(self.menu_frame, text="Editorial", background="gray", foreground="white",
                               activeforeground="black", activebackground="gray52", command=lambda: self.enviar_senal("VistaEditorial"))
        editorial.pack(side="left", padx=2, pady=2)

        # Crear el botón Movimientos
        Movimientos = tk.Button(self.menu_frame, text="Movimientos", background="gray", foreground="white",
                           activeforeground="black", activebackground="gray52", command=lambda: self.enviar_senal("VistaMovimientos"))
        Movimientos.pack(side="left", padx=2, pady=2)

        # Crear el botón Productos
        productos = tk.Button(self.menu_frame, text="Productos", background="gray", foreground="white",
                              activeforeground="black", activebackground="gray52", command=lambda: self.enviar_senal("VistaProductos"))
        productos.pack(side="left", padx=2, pady=2)

        # Crear el botón Proveedores
        proveedores = tk.Button(self.menu_frame, text="Proveedores", background="gray", foreground="white",
                                activeforeground="black", activebackground="gray52", command=lambda: self.enviar_senal("VistaProveedores"))
        proveedores.pack(side="left", padx=2, pady=2)

        

        

    def enviar_senal(self, senal):
        self.callback(senal)
