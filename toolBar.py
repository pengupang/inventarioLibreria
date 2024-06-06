from tkinter import *


class ToolBar(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        menuBar = Menu(parent)
        parent.config(menu=menuBar)

        productosMenu=Menu(menuBar,tearoff=0)
        productosMenu.add_command(label="Ingresar producto")
        productosMenu.add_command(label="Editar producto")
        productosMenu.add_command(label="Ver productos")
        
        editorialMenu=Menu(menuBar,tearoff=0)
        editorialMenu.add_command(label="Ingresar Editorial")
        editorialMenu.add_command(label="Editar Editorial")
        editorialMenu.add_command(label="Ver Editoriales")
        
        proveedorMenu=Menu(menuBar,tearoff=0)
        proveedorMenu.add_command(label="Ingresar Proveedor")
        proveedorMenu.add_command(label="Editar Proveedor")
        proveedorMenu.add_command(label="Ver Proveedores")
        
        ventaMenu=Menu(menuBar,tearoff=0)
        ventaMenu.add_command(label="Ingresar Venta")
        ventaMenu.add_command(label="Ver Ventas")
     
        compraMenu=Menu(menuBar,tearoff=0)
        compraMenu.add_command(label="Ingresar Compra")
        compraMenu.add_command(label="Editar Compra")
        compraMenu.add_command(label="Ver Compras")
       

        menuBar.add_cascade(label="Productos",menu=productosMenu)
        menuBar.add_cascade(label="Editorial",menu=editorialMenu)
        menuBar.add_cascade(label="Proveedores",menu=proveedorMenu)
        menuBar.add_cascade(label="Ventas",menu=ventaMenu)
        menuBar.add_cascade(label="Compras",menu=compraMenu)
      
