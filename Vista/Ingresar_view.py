from customtkinter import * 
from tkinter import ttk

class IngresarFrames ():
    def __init__(self,master) -> None:
        self.master=master

    def IngresarCompras(self):
        label_id = CTkLabel(self, text="ID:")
        label_titulo = CTkLabel(self, text="Título Libro:")
        label_fecha = CTkLabel(self, text="Fecha:")
        label_cantidad = CTkLabel(self, text="Cantidad Comprada:")
        label_total = CTkLabel(self, text="Total Compra:")
        
        self.entry_id = CTkEntry(self)
        self.entry_titulo = CTkEntry(self)
        self.entry_fecha = CTkEntry(self)
        self.entry_cantidad = CTkEntry(self)
        self.entry_total = CTkEntry(self)
        
        label_id.place(x=50, y=50)
        self.entry_id.place(x=150, y=50)
        
        label_titulo.place(x=50, y=80)
        self.entry_titulo.place(x=150, y=80)
        
        label_fecha.place(x=50, y=110)
        self.entry_fecha.place(x=150, y=110)
        
        label_cantidad.place(x=50, y=140)
        self.entry_cantidad.place(x=150, y=140)
        
        label_total.place(x=50, y=170)
        self.entry_total.place(x=150, y=170)
        
        self.btn_ingresar = CTkButton(self, text="Ingresar", command=None)
        self.btn_ingresar.place(x=50, y=200)
    
    def IngresarEditorial(self):
        label_id = CTkLabel(self, text="ID:")
        label_editorial = CTkLabel(self, text="Editorial:")
        
        self.entry_id = CTkEntry(self)
        self.entry_editorial = CTkEntry(self)
        
        label_id.place(x=50, y=50)
        self.entry_id.place(x=150, y=50)
        
        label_editorial.place(x=50, y=80)
        self.entry_editorial.place(x=150, y=80)
        
        self.btn_ingresar = CTkButton(self, text="Ingresar", command=None)
        self.btn_ingresar.place(x=50, y=100)
      
    def IngresarProductos(self):
        label_id = CTkLabel(self, text="ID:")
        label_titulo = CTkLabel(self, text="Título:")
        label_autor = CTkLabel(self, text="Autor:")
        label_stock = CTkLabel(self, text="Stock:")
        
        self.entry_id = CTkEntry(self)
        self.entry_titulo = CTkEntry(self)
        self.entry_autor = CTkEntry(self)
        self.entry_stock = CTkEntry(self)
        
        label_id.place(x=50, y=50)
        self.entry_id.place(x=150, y=50)
        
        label_titulo.place(x=50, y=80)
        self.entry_titulo.place(x=150, y=80)
        
        label_autor.place(x=50, y=110)
        self.entry_autor.place(x=150, y=110)
        
        label_stock.place(x=50, y=140)
        self.entry_stock.place(x=150, y=140)
        
        
        self.btn_ingresar =CTkButton(self, text="Ingresar", command=None)
        self.btn_ingresar.place(x=50, y=200)

    def IngresarProveedores(self):
        label_id = CTkLabel(self, text="ID:")
        label_proveedor = CTkLabel(self, text="Proveedor:")
        
        self.entry_id = CTkEntry(self)
        self.entry_proveedor = CTkEntry(self)
        
        label_id.place(x=50, y=50)
        self.entry_id.place(x=150, y=50)
        
        label_proveedor.place(x=50, y=80)
        self.entry_proveedor.place(x=150, y=80)
        
        self.btn_ingresar = CTkButton(self, text="Ingresar", command=None)
        self.btn_ingresar.place(x=50, y=100)

    def IngresarVentas(self):
        label_id = CTkLabel(self, text="ID:")
        label_titulo = CTkLabel(self, text="Título Libro:")
        label_fecha = CTkLabel(self, text="Fecha:")
        label_cantidad = CTkLabel(self, text="Cantidad Vendida:")
        label_total = CTkLabel(self, text="Total venta:")
        
        self.entry_id = CTkEntry(self)
        self.entry_titulo = CTkEntry(self)
        self.entry_fecha = CTkEntry(self)
        self.entry_cantidad = CTkEntry(self)
        self.entry_total = CTkEntry(self)
        
        label_id.place(x=50, y=50)
        self.entry_id.place(x=150, y=50)
        
        label_titulo.place(x=50, y=80)
        self.entry_titulo.place(x=150, y=80)
        
        label_fecha.place(x=50, y=110)
        self.entry_fecha.place(x=150, y=110)
        
        label_cantidad.place(x=50, y=140)
        self.entry_cantidad.place(x=150, y=140)
        
        label_total.place(x=50, y=170)
        self.entry_total.place(x=150, y=170)
        
        self.btn_ingresar = CTkButton(self, text="Ingresar", command=None)
        self.btn_ingresar.place(x=50, y=200)
        
        