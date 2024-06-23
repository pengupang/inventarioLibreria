from customtkinter import * 
from Controlador.controladorFunciones import *

# En esta clase se cargan los frames de cada boton dedicados solamente a ingresar datos de la BD
class IngresarFrames ():
    def __init__(self,master) -> None:
         self.master=master

    def IngresarCompras(self):
        label_idtype = CTkLabel(self.master, text="Id del tipo de movimiento:")
        label_fecha = CTkLabel(self.master, text="Fecha:")
        label_total = CTkLabel(self.master, text="Total Movimiento:")
        
        self.entry_idtype = CTkEntry(self.master)
        self.entry_fecha = CTkEntry(self.master)
        self.entry_total = CTkEntry(self.master)
        
        label_idtype.place(x=50, y=80)
        self.entry_idtype.place(x=150, y=80)

        label_fecha.place(x=50, y=110)
        self.entry_fecha.place(x=150, y=110)

        label_total.place(x=50, y=170)
        self.entry_total.place(x=150, y=170)

        self.btn_ingresar = CTkButton(
            self.master,
            text="Ingresar",
            command=lambda:ControladorFunciones.insertar_datos(
                "movimiento",
                ["ID_Tipo_movimiento", "Fecha", "Total_neto"],
                [self.entry_idtype.get(), self.entry_fecha.get(), self.entry_total.get()]
            )
        )
        
        self.btn_ingresar.place(x=55, y=210)
    
    def IngresarEditorial(self):
        label_nombre = CTkLabel(self.master, text="Nombre:")

        self.entry_nombre = CTkEntry(self.master)

        label_nombre.place(x=50, y=80)
        self.entry_nombre.place(x=150, y=80)
        
        self.btn_ingresar = CTkButton(
            self.master,
            text="Ingresar",
            command= lambda:ControladorFunciones.insertar_datos(
                "editorial",
                ["Nombre"],
                [self.entry_nombre.get()]
            )
        )
         
        self.btn_ingresar.place(x=50, y=140)
      
    def IngresarProductos(self):
       
        label_titulo = CTkLabel(self.master, text="Título:")
        label_stock = CTkLabel(self.master, text="Stock:")
        
        self.entry_titulo = CTkEntry(self.master)
        self.entry_stock = CTkEntry(self.master)

      
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
         
        self.btn_ingresar.place(x=50, y=140)

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

        #en la base de datos no hay ventas ni compras, compras fue cambiado a movimiento(ingresarCompras = ingresarMovimiento)
        #Proveedor fue borrado 


      
        