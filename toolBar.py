from tkinter import *
import tkinter as tk


class ToolBar(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        menu_frame= tk.Frame(parent,background= "gray")
        menu_frame.pack(side="top" , fill="x")
        #crea el btn productos
        productos = tk.Menubutton(menu_frame,
                                  text="Productos",
                                  background= "gray",
                                  foreground="white",
                                  activeforeground="black",
                                  activebackground="gray52")
        #crea el menu desplegable de 
        menu_productos = tk.Menu(productos,tearoff=0)
        menu_productos.add_command(label="Ingresar Producto")
        menu_productos.add_command(label="Editar Producto")
        menu_productos.add_command(label="Ver Productos")
        
        editorial = tk.Menubutton(menu_frame,
                                  text="Editorial",
                                  background= "gray",
                                  foreground="white",
                                  activeforeground="black",
                                  activebackground="gray52")
        
        menu_editoriales = tk.Menu(editorial,tearoff=0)
        menu_editoriales.add_command(label="Ingresar Editorial")
        menu_editoriales.add_command(label="Editar Editorial")
        menu_editoriales.add_command(label="Ver Editoriales")
        
        proveedores = tk.Menubutton(menu_frame,
                                  text="Proveedores",
                                  background= "gray",
                                  foreground="white",
                                  activeforeground="black",
                                  activebackground="gray52")
        
        menu_proveedores = tk.Menu(proveedores,tearoff=0)
        menu_proveedores.add_command(label="Ingresar Proveedor")
        menu_proveedores.add_command(label="Editar Proveedor")
        menu_proveedores.add_command(label="Ver Proveedores")

        ventas = tk.Menubutton(menu_frame,
                                  text="Ventas",
                                  background= "gray",
                                  foreground="white",
                                  activeforeground="black",
                                  activebackground="gray52")
        
        menu_ventas = tk.Menu(ventas,tearoff=0)
        menu_ventas.add_command(label="Ingresar Venta")
        menu_ventas.add_command(label="Ver Ventas")

        
        compras = tk.Menubutton(menu_frame,
                                  text="Compras",
                                  background= "gray",
                                  foreground="white",
                                  activeforeground="black",
                                  activebackground="gray52")
        
        menu_compras = tk.Menu(compras,tearoff=0)
        menu_compras.add_command(label="Ingresar Compra")
        menu_compras.add_command(label="Editar Compra")
        menu_compras.add_command(label="Ver Compras")
        
        productos.config(menu=menu_productos)
        productos.pack(side="left")

        editorial.config(menu=menu_editoriales)
        editorial.pack(side="left")

        proveedores.config(menu=menu_proveedores)
        proveedores.pack(side="left")

        ventas.config(menu=menu_ventas)
        ventas.pack(side="left")

        compras.config(menu=menu_compras)
        compras.pack(side="left")
      
