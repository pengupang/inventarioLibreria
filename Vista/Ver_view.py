from customtkinter import * 
from tkinter import ttk
# En esta clase se cargan los frames de cada boton dedicados solamente a la Visualzación de datos de la BD
class VerFrames():
    def __init__(self,master,callback,barraBusqueda) -> None:
        self.callback=callback
        self.master=master
        self.barraBusqueda = barraBusqueda

    def verCompras(self):
        buscador = CTkEntry(self.master)
        tabla = ttk.Treeview(self.master)
        query="SELECT * FROM compras"
        boton_bus = CTkButton(self.master, text="Buscar",command=lambda: self.barraBusqueda(tabla,buscador,query))
        #crea columnas
        tabla['columns']=("1","2","3","4","5")
        #cambia ancho de columna id
        tabla.column("#0",width=0)
        #agrega texto a los headings de las columnas
        tabla.heading("1",text="ID")
        tabla.heading("2",text="Titulo Libro")
        tabla.heading("3",text="Fecha")
        tabla.heading("4",text="Cantidad Comprada")
        tabla.heading("5",text="Total Compra")
        #acomoda la tabla en la ventana
        tabla.place(x=325,y=300,anchor="center")
        buscador.place(x=75,y=130,anchor="center")
        boton_bus.place(x=220,y=130,anchor="center")
        self.callback(tabla,query)
        
    
    def verEditoriales(self):
        buscador = CTkEntry(self.master)
        tabla = ttk.Treeview(self.master)
        query="SELECT * FROM editorial;"
        boton_bus = CTkButton(self.master, text="Buscar",command=lambda: self.barraBusqueda(tabla,buscador,query))
        #crea columnas
        tabla['columns']=("1","2")
        #cambia ancho de columna id
        tabla.column("#0",width=0)
        #agrega texto a los headings de las columnas
        tabla.heading("1",text="ID")
        tabla.heading("2",text="Nombre")
        #acomoda la tabla en la ventana
        tabla.place(x=325,y=300,anchor="center")
        buscador.place(x=75,y=130,anchor="center")
        boton_bus.place(x=220,y=130,anchor="center")
        self.callback(tabla,query)

    def verProductos(self):

        buscador = CTkEntry(self.master)
        tabla = ttk.Treeview(self.master)
        query="SELECT * FROM libro"
        boton_bus = CTkButton(self.master, text="Buscar",command=lambda: self.barraBusqueda(tabla,buscador,query))
        #crea columnas
        tabla['columns']=("1","2","3","4")
        #cambia ancho de columna id
        tabla.column("#0",width=0)
        tabla.column("#1",width=40)
        #agrega texto a los headings de las columnas
        tabla.heading("1",text="ID")
        tabla.heading("2",text="Titulo")
        tabla.heading("3",text="Autor")
        tabla.heading("4",text="Stock")
        #acomoda la tabla en la ventana
        tabla.place(x=325,y=300,anchor="center")
        buscador.place(x=75,y=130,anchor="center")
        boton_bus.place(x=220,y=130,anchor="center")
        self.callback(tabla,query)

    def verProveedores(self):
        buscador = CTkEntry(self.master)
        tabla = ttk.Treeview(self.master)
        query="SELECT * FROM proveedor;"
        boton_bus = CTkButton(self.master, text="Buscar",command=lambda: self.barraBusqueda(tabla,buscador,query))
        #crea columnas
        tabla['columns']=("1","2")
        #cambia ancho de columna id
        tabla.column("#0",width=0)
        tabla.column("#1",width=20)
        #agrega texto a los headings de las columnas
        tabla.heading("1",text="ID")
        tabla.heading("2",text="Nombre")
        #acomoda la tabla en la ventana
        tabla.place(x=325,y=300,anchor="center")
        buscador.place(x=75,y=130,anchor="center")
        boton_bus.place(x=220,y=130,anchor="center")
        self.callback(tabla,query)
    
    def verVentas(self):
        buscador = CTkEntry(self.master)
        query="SELECT * FROM ventas;"
        #crea tabla 
        tabla = ttk.Treeview(self.master)
        boton_bus = CTkButton(self.master, text="Buscar",command=lambda: self.barraBusqueda(tabla,buscador,query))
        #crea columnas
        tabla['columns']=("1","2","3","4","5")
        #cambia ancho de columna id
        tabla.column("#0",width=0)
        #agrega texto a los headings de las columnas
        tabla.heading("1",text="ID")
        tabla.heading("2",text="Titulo Libro")
        tabla.heading("3",text="Fecha")
        tabla.heading("4",text="Cantidad Vendida")
        tabla.heading("5",text="Total venta")
        #acomoda la tabla en la ventana
        tabla.place(x=325,y=300,anchor="center")
        buscador.place(x=75,y=130,anchor="center")
        boton_bus.place(x=220,y=130,anchor="center")
<<<<<<< HEAD
        self.evento_querys(tabla,query)

    def evento_querys(self,tabla,query):
        print(query)
        self.callback(tabla,query)
=======
        self.callback(tabla,query)

    
        

    def buscarElemento(self,tabla,entry):
        resultados = []
        for x in tabla.get_children():
            print("fila a comparar: ", tabla.item(x)['values'][1].lower())
            if entry.get().lower() == tabla.item(x)['values'][1].lower():
                resultados.append(x)
                print("resultado: ",resultados)
        if len(resultados) > 0:
            print("se encontraron:",len(resultados)," resultado/s.")
            tabla.selection_set(resultados)
            tabla.see(resultados[0])
        

    def _buscarElemento(self,tabla,entry,query):
        busqueda = entry.get()
        if len(busqueda) > 0:
            print("busqueda: ",busqueda.lower())
            self.buscarElemento(tabla,entry)
        else:
            tabla.delete(*tabla.get_children())
            self.callback(tabla,query)
        
            
>>>>>>> 9010d6e2fbc1daf963e2c72f350d7e4c96ed3bb0
