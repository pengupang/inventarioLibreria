from tkinter import *
import tkinter as tk
from Vista.VerProductos_view import FrameVerProductos
from Vista.VerEditorial_view import FrameVerEditorial
from Vista.VerProveedores_view import FrameVerProveedores
from Vista.VerVentas_view import FrameVerVentas
from Vista.VerCompras_view import FrameVerCompras
from Vista.VerEditarProductos import FrameVerEditarProductos
from Vista.VerIngresarProductos import FrameVerIngresarProductos
from Vista.VerIngresarEditorial import FrameVerIngresarEditorial
from Vista.VerEditarEditorial import FrameVerEditarEditorial
from Vista.VerIngresarProveedores import FrameVerIngresarProveedores
from Vista.VerEditarProveedores_view import FrameVerEditarProveedores
from Vista.VerIngresarVentas_view import FrameVerIngresarVentas
from Vista.VerIngresarCompras_view import FrameVerIngresarCompras
from Vista.VerEditarCompras_view import FrameVerEditarCompras

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
       
       #define la funcion verProductos que le da el dato de la ventana principal al 
       # frame ver productos para que asi el treeview aparezca
       #esta funcion es para que el boton haga algo
        def verProductos():
            FrameVerProductos(parent)

        def VerEditarProducto():
            FrameVerEditarProductos(parent)

        def VerIngresarProducto():
            FrameVerIngresarProductos(parent)

        #crea el menu desplegable de productos
        menu_productos = tk.Menu(productos,tearoff=0)
        menu_productos.add_command(label="Ingresar Producto", command= VerIngresarProducto)
        menu_productos.add_command(label="Editar Producto", command= VerEditarProducto)
        menu_productos.add_command(label="Ver Productos",command= verProductos)
        
        def verEditorial():
            FrameVerEditorial(parent)

        def verIngresarEditorial():
            FrameVerIngresarEditorial(parent)

        def verEditarEditorial():
            FrameVerEditarEditorial(parent)

        #crea el btn Editorial
        editorial = tk.Menubutton(menu_frame,
                                  text="Editorial",
                                  background= "gray",
                                  foreground="white",
                                  activeforeground="black",
                                  activebackground="gray52")
        
        #crea el menu desplegable de Editoriales
        menu_editoriales = tk.Menu(editorial,tearoff=0)
        menu_editoriales.add_command(label="Ingresar Editorial", command=verIngresarEditorial)
        menu_editoriales.add_command(label="Editar Editorial", command=verEditarEditorial)
        menu_editoriales.add_command(label="Ver Editoriales" , command=verEditorial)
        
        def verProveedores():
            FrameVerProveedores(parent)

        def verIngresarProveedores():
            FrameVerIngresarProveedores(parent)

        def verEditarProveedores():
            FrameVerEditarProveedores(parent)

        #crea el btn Proveedores
        proveedores = tk.Menubutton(menu_frame,
                                  text="Proveedores",
                                  background= "gray",
                                  foreground="white",
                                  activeforeground="black",
                                  activebackground="gray52")
        
        #crea el menu desplegable de Proveedores
        menu_proveedores = tk.Menu(proveedores,tearoff=0)
        menu_proveedores.add_command(label="Ingresar Proveedor", command=verIngresarProveedores)
        menu_proveedores.add_command(label="Editar Proveedor", command=verEditarProveedores)
        menu_proveedores.add_command(label="Ver Proveedores", command=verProveedores)

        def verVentas():
            FrameVerVentas(parent)

        def verIngresarVentas():
            FrameVerIngresarVentas(parent)

        #crea el btn Ventas
        ventas = tk.Menubutton(menu_frame,
                                  text="Ventas",
                                  background= "gray",
                                  foreground="white",
                                  activeforeground="black",
                                  activebackground="gray52")
        
        #crea el menu desplegable de Ventas
        menu_ventas = tk.Menu(ventas,tearoff=0)
        menu_ventas.add_command(label="Ingresar Venta", command=verIngresarVentas)
        menu_ventas.add_command(label="Ver Ventas", command=verVentas)

        def verCompras():
            FrameVerCompras(parent)

        def verIngresarCompras():
            FrameVerIngresarCompras(parent)
            
        def verEditrarCompras():
            FrameVerEditarCompras(parent)

        #crea el btn Compras
        compras = tk.Menubutton(menu_frame,
                                  text="Compras",
                                  background= "gray",
                                  foreground="white",
                                  activeforeground="black",
                                  activebackground="gray52")
        
        #crea el menu desplegable de Compras
        menu_compras = tk.Menu(compras,tearoff=0)
        menu_compras.add_command(label="Ingresar Compra", command=verIngresarCompras)
        menu_compras.add_command(label="Editar Compra", command=verEditrarCompras)
        menu_compras.add_command(label="Ver Compras",command=verCompras)
        
        #acomoda los btns de la toolbar
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
      
