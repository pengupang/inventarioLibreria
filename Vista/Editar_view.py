from customtkinter import * 
from tkinter import ttk
# En esta clase se cargan los frames de cada boton dedicados solamente a la edición de datos de la BD
class EditarFrames():
    def __init__(self,master) -> None:
        super().__init__(master)
    
    #modulo de view editar compras
    def EditarCompras(self):
        #genera los label
        label_id = CTkLabel(self, text="ID:")
        label_titulo = CTkLabel(self, text="Título Libro:")
        label_fecha = CTkLabel(self, text="Fecha:")
        label_cantidad = CTkLabel(self, text="Cantidad Comprada:")
        label_total = CTkLabel(self, text="Total Compra:")
        
        #genera las cajas de texto
        self.entry_id = CTkEntry(self)
        self.entry_titulo = CTkEntry(self)
        self.entry_fecha = CTkEntry(self)
        self.entry_cantidad = CTkEntry(self)
        self.entry_total = CTkEntry(self)
        
        label_id.place(x=50, y=50)
        self.entry_id.place(x=180, y=50)
        
        label_titulo.place(x=50, y=80)
        self.entry_titulo.place(x=180, y=80)
        
        label_fecha.place(x=50, y=110)
        self.entry_fecha.place(x=180, y=110)
        
        label_cantidad.place(x=50, y=140)
        self.entry_cantidad.place(x=180, y=140)
        
        label_total.place(x=50, y=170)
        self.entry_total.place(x=180, y=170)
        
        #genera botones
        self.btn_ingresar = CTkButton(self, text="Ingresar", command=None)
        self.btn_ingresar.place(x=50, y=190)
        
        self.btn_editar = CTkButton(self, text="Editar", command=None)
        self.btn_editar.place(x=150, y=200)
        
        # Crear tabla
        self.tabla = ttk.Treeview(self)
        self.tabla['columns'] = ("ID", "Titulo Libro", "Fecha", "Cantidad Comprada", "Total Compra")

        #acomoda las columnas de la tabla
        self.tabla.column("#0", width=0)
        self.tabla.column("ID",width=20)
        self.tabla.column("Titulo Libro",width=170)
        self.tabla.column("Fecha",width=170)
        self.tabla.column("Cantidad Comprada",width=170)
        self.tabla.column("Total Compra",width=170)

        #le da el texto de titulos a la tabla
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Titulo Libro", text="Titulo Libro")
        self.tabla.heading("Fecha", text="Fecha")
        self.tabla.heading("Cantidad Comprada", text="Cantidad Comprada")
        self.tabla.heading("Total Compra", text="Total Compra")
        self.tabla.place(relx=0.5, rely=0.6,anchor=CENTER)

    def EditarEditoriales(self):
        label_id = CTkLabel(self, text="ID:")
        label_editorial = CTkLabel(self, text="Editorial:")
        
        self.entry_id = CTkEntry(self)
        self.entry_editorial = CTkEntry(self)
        
        label_id.place(x=50, y=50)
        self.entry_id.place(x=180, y=50)
        
        label_editorial.place(x=50, y=80)
        self.entry_editorial.place(x=180, y=80)
        
        self.btn_ingresar = CTkButton(self, text="Ingresar", command=None)
        self.btn_ingresar.place(x=50, y=110)
        
        self.btn_editar = CTkButton(self, text="Editar", command=None)
        self.btn_editar.place(x=150, y=110)

        self.tabla = ttk.Treeview(self)
        self.tabla['columns'] = ("ID", "Editorial")
        self.tabla.column("#0", width=0)
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Editorial", text="Nombre")
        self.tabla.place(relx=0.5, rely=0.6,anchor=CENTER)

    def EditarProductos(self):
        label_id = CTkLabel(self, text="ID:")
        label_titulo = CTkLabel(self, text="Título:")
        label_autor = CTkLabel(self, text="Autor:")
        label_stock = CTkLabel(self, text="Stock:")
        
        self.entry_id = CTkEntry(self)
        self.entry_titulo = CTkEntry(self)
        self.entry_autor = CTkEntry(self)
        self.entry_stock = CTkEntry(self)

        
        label_id.place(x=50, y=50)
        self.entry_id.place(x=180, y=50)
        
        label_titulo.place(x=50, y=80)
        self.entry_titulo.place(x=180, y=80)
        
        label_autor.place(x=50, y=110)
        self.entry_autor.place(x=180, y=110)
        
        label_stock.place(x=50, y=140)
        self.entry_stock.place(x=180, y=140)

        
        self.btn_ingresar = CTkButton(self, text="Ingresar", command=None)
        self.btn_ingresar.place(x=50, y=200)
        
        self.btn_editar = CTkButton(self, text="Editar", command=None)
        self.btn_editar.place(x=150, y=200)
        
        # Crear tabla
        self.tabla = ttk.Treeview(self)
        self.tabla['columns'] = ("ID", "Titulo", "Autor", "Stock")
        self.tabla.column("#0", width=0)
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Titulo", text="Titulo")
        self.tabla.heading("Autor", text="Autor")
        self.tabla.heading("Stock", text="Stock")
        self.tabla.place(relx=0.5, rely=0.6,anchor=CENTER)

    def EditarProveedores(self):
        label_id = CTkLabel(self, text="ID:")
        label_proveedor = CTkLabel(self, text="Proveedor:")
        
        self.entry_id = CTkEntry(self)
        self.entry_proveedor = CTkEntry(self)
        
        label_id.place(x=50, y=50)
        self.entry_id.place(x=180, y=50)
        
        label_proveedor.place(x=50, y=80)
        self.entry_proveedor.place(x=180, y=80)
        
        self.btn_ingresar = CTkButton(self, text="Ingresar", command=None)
        self.btn_ingresar.place(x=50, y=110)
        
        self.btn_editar = CTkButton(self, text="Editar", command=None)
        self.btn_editar.place(x=150, y=110)

        self.tabla = ttk.Treeview(self)
        self.tabla['columns'] = ("ID", "Editorial")
        self.tabla.column("#0", width=0)
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Editorial", text="Nombre")
        self.tabla.place(relx=0.5, rely=0.6,anchor=CENTER)