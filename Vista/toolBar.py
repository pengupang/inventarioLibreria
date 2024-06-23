from tkinter import *
import tkinter as tk
# En esta clase se crean los botones y eventos relacionados a estos
#que permiten el movimiento entre los diferentes frames que posee la aplicación
class ToolBar(Frame):
    def __init__(self, master,callback):
        super().__init__(master)
        self.callback = callback
        self.menu_frame= Frame(master,background= "gray")
        self.menu_frame.pack(side="top" , fill="x")
        self.crear_botones()
    
    def crear_botones(self):
        #crea el btn productos
        productos = tk.Menubutton(self.menu_frame,
                                  text="Productos",
                                  background= "gray",
                                  foreground="white",
                                  activeforeground="black",
                                  activebackground="gray52")
       
        
        #crea el menu desplegable de productos
        menu_productos = tk.Menu(productos,tearoff=0)
        menu_productos.add_command(label="Ingresar Producto", command= lambda: self.enviar_señal("Ingresar Producto"))
        menu_productos.add_command(label="Editar Producto", command= lambda: self.enviar_señal("Editar Producto"))
        menu_productos.add_command(label="Ver Productos",command= lambda: self.enviar_señal("Ver Producto"))
        menu_productos.add_command(label="Eliminar Productos",command= lambda: self.enviar_señal("Eliminar Producto"))
    
        

        #crea el btn Editorial
        editorial = tk.Menubutton(self.menu_frame,
                                  text="Editorial",
                                  background= "gray",
                                  foreground="white",
                                  activeforeground="black",
                                  activebackground="gray52")
        
        #crea el menu desplegable de Editoriales
        menu_editoriales = tk.Menu(editorial,tearoff=0)
        menu_editoriales.add_command(label="Ingresar Editorial", command=lambda: self.enviar_señal("Ingresar Editorial"))
        menu_editoriales.add_command(label="Editar Editorial", command=lambda: self.enviar_señal("Editar Editorial"))
        menu_editoriales.add_command(label="Ver Editoriales" , command=lambda: self.enviar_señal("Ver Editorial"))
        menu_editoriales.add_command(label="Eliminar Editoriales" , command=lambda: self.enviar_señal("Eliminar Editorial"))
        

        #crea el btn Proveedores
        proveedores = tk.Menubutton(self.menu_frame,
                                  text="Proveedores",
                                  background= "gray",
                                  foreground="white",
                                  activeforeground="black",
                                  activebackground="gray52")
        
        #crea el menu desplegable de Proveedores
        menu_proveedores = tk.Menu(proveedores,tearoff=0)
        menu_proveedores.add_command(label="Ingresar Proveedor", command=lambda: self.enviar_señal("Ingresar Proveedor"))
        menu_proveedores.add_command(label="Editar Proveedor", command=lambda: self.enviar_señal("Editar Proveedor"))
        menu_proveedores.add_command(label="Ver Proveedores", command=lambda: self.enviar_señal("Ver Proveedor"))
        menu_proveedores.add_command(label="Eliminar Proveedores", command=lambda: self.enviar_señal("Eliminar Proveedor"))


        #crea el btn Ventas
        ventas = tk.Menubutton(self.menu_frame,
                                  text="Ventas",
                                  background= "gray",
                                  foreground="white",
                                  activeforeground="black",
                                  activebackground="gray52")
        
        #crea el menu desplegable de Ventas
        menu_ventas = tk.Menu(ventas,tearoff=0)
        menu_ventas.add_command(label="Ingresar Venta", command=lambda: self.enviar_señal("Ingresar Venta"))
        menu_ventas.add_command(label="Ver Ventas", command=lambda: self.enviar_señal("Ver Venta"))
        menu_ventas.add_command(label="Eliminar Ventas",command=lambda: self.enviar_señal("Eliminar Venta"))


        #crea el btn Compras
        compras = tk.Menubutton(self.menu_frame,
                                  text="Compras",
                                  background= "gray",
                                  foreground="white",
                                  activeforeground="black",
                                  activebackground="gray52")
        
        #crea el menu desplegable de Compras
        menu_compras = tk.Menu(compras,tearoff=0)
        menu_compras.add_command(label="Ingresar Compra", command=lambda: self.enviar_señal("Ingresar Compra"))
        menu_compras.add_command(label="Editar Compra", command=lambda: self.enviar_señal("Editar Compra"))
        menu_compras.add_command(label="Ver Compras",command=lambda: self.enviar_señal("Ver Compra"))
        menu_compras.add_command(label="Eliminar Compras",command=lambda: self.enviar_señal("Eliminar Compra"))
        
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
    
    def enviar_señal(self,y):
        self.callback(y)

      
