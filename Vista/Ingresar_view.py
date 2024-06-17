from customtkinter import * 
# En esta clase se cargan los frames de cada boton dedicados solamente a ingresar datos de la BD
class IngresarFrames ():
    def __init__(self,master) -> None:
         self.master=master

    def IngresarCompras(self):
        label_id = CTkLabel(self.master, text="ID:")
        label_titulo = CTkLabel(self.master, text="Título Libro:")
        label_fecha = CTkLabel(self.master, text="Fecha:")
        label_cantidad = CTkLabel(self.master, text="Cantidad Comprada:")
        label_total = CTkLabel(self.master, text="Total Compra:")
        
        self.entry_id = CTkEntry(self.master)
        self.entry_titulo = CTkEntry(self.master)
        self.entry_fecha = CTkEntry(self.master)
        self.entry_cantidad = CTkEntry(self.master)
        self.entry_total = CTkEntry(self.master)
        
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
        
        self.btn_ingresar = CTkButton(self.master, text="Ingresar", command=None)
        self.btn_ingresar.place(x=55, y=210)
    
    def IngresarEditorial(self):
        label_id = CTkLabel(self.master, text="ID:")
        label_editorial = CTkLabel(self, text="Editorial:")
        
        self.entry_id = CTkEntry(self.master)
        self.entry_editorial = CTkEntry(self.master)
        
        label_id.place(x=50, y=50)
        self.entry_id.place(x=150, y=50)
        
        label_editorial.place(x=50, y=80)
        self.entry_editorial.place(x=150, y=80)
        
        self.btn_ingresar = CTkButton(self.master, text="Ingresar", command=None)
        self.btn_ingresar.place(x=50, y=100)
      
    def IngresarProductos(self):
        label_id = CTkLabel(self.master, text="ID:")
        label_titulo = CTkLabel(self.master, text="Título:")
        label_autor = CTkLabel(self.master, text="Autor:")
        label_stock = CTkLabel(self.master, text="Stock:")
        
        self.entry_id = CTkEntry(self.master)
        self.entry_titulo = CTkEntry(self.master)
        self.entry_autor = CTkEntry(self.master)
        self.entry_stock = CTkEntry(self.master)
        
        label_id.place(x=50, y=50)
        self.entry_id.place(x=150, y=50)
        
        label_titulo.place(x=50, y=80)
        self.entry_titulo.place(x=150, y=80)
        
        label_autor.place(x=50, y=110)
        self.entry_autor.place(x=150, y=110)
        
        label_stock.place(x=50, y=140)
        self.entry_stock.place(x=150, y=140)
        
        
        self.btn_ingresar =CTkButton(self.master, text="Ingresar", command=None)
        self.btn_ingresar.place(x=50, y=200)

        

    def IngresarProveedores(self):
        label_id = CTkLabel(self.master, text="ID:")
        label_proveedor = CTkLabel(self.master, text="Proveedor:")
        
        self.entry_id = CTkEntry(self.master)
        self.entry_proveedor = CTkEntry(self.master)
        
        label_id.place(x=50, y=50)
        self.entry_id.place(x=150, y=50)
        
        label_proveedor.place(x=50, y=80)
        self.entry_proveedor.place(x=150, y=80)
        
        self.btn_ingresar = CTkButton(self.master, text="Ingresar", command=None)
        self.btn_ingresar.place(x=50, y=100)

    def IngresarVentas(self):
        label_id = CTkLabel(self.master, text="ID:")
        label_titulo = CTkLabel(self.master, text="Título Libro:")
        label_fecha = CTkLabel(self.master, text="Fecha:")
        label_cantidad = CTkLabel(self.master, text="Cantidad Vendida:")
        label_total = CTkLabel(self.master, text="Total venta:")
        
        self.entry_id = CTkEntry(self.master)
        self.entry_titulo = CTkEntry(self.master)
        self.entry_fecha = CTkEntry(self.master)
        self.entry_cantidad = CTkEntry(self.master)
        self.entry_total = CTkEntry(self.master)
        
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
        
        self.btn_ingresar = CTkButton(self.master, text="Ingresar", command=None)
        self.btn_ingresar.place(x=50, y=200)

        
        