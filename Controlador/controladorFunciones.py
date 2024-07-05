#Controlador encargado de realizar funciones que necesiten pasar por la base de datos
# y realizar un retorno de datos 
from tkinter import messagebox
from Modelo import conexion
from Modelo import listaImpresa
from Modelo import impresora

class ControladorFunciones:

    #Valida los datos ingresados en login con los almacenados en la base de datos
    def validar_usuario(self, usuario, contraseña):
        query = "SELECT * FROM usuario WHERE Nombre = %s AND Password = %s;"
        params = (usuario, contraseña)
        resultados = conexion.ejecutar_consulta(query, params)
        
        if resultados:
            return True  
        else:
            #en caso de que los datos ingresados sean incorrectos muestra un warning avisando
            #el error
            messagebox.showwarning(title=None, message="Datos introducidos incorrectos")
            print("Datos mal puestos") 
    
    # Carga los datos a las tablas 
    def cargarDatos(self,tabla,query):
        resultados= conexion.ejecutar_consulta(query)
        if resultados:
                for row in resultados:
                    tabla.insert("", "end", values=row)
        else:  #En caso de estar la tabla vacia en la BD muestra un alert de informacion
                messagebox.showinfo(title= None, message="No se encontraron registros")
                print("No se encontraron registros")



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
            self.cargarDatos(tabla,query)

    def insertar_datos(tabla, campos, valores):
        campos_str = ", ".join(campos)
        placeholders = ", ".join(["%s"] * len(valores))
        query = f"INSERT INTO {tabla} ({campos_str}) VALUES ({placeholders});"

        resultado = conexion.ejecutar_comando(query, valores)

        if resultado:
            messagebox.showinfo(title="Exito",message=f"Datos insertados correctamente en la tabla {tabla}")
            print(f"Datos insertados correctamente en la tabla {tabla}.")
        else:
            messagebox.showerror(title="Error",message=f"Error al insertar datos en la tabla {tabla}.")
            print(f"Error al insertar datos en la tabla {tabla}.")

    def seleccionar_datos(self, event):
        try:
            item = self.tabla.selection()
            values = self.tabla.item(item)['values']
            
            self.entry_id.insert(0, values[0])
            self.entry_editorial.insert(0, values[1])
        except:
                titulo = 'Edicion de datos'
                mensaje = 'No ha seleccionado ningun registro'
                messagebox.showerror(titulo, mensaje)
                
    def eliminar_elemento(self,tabla):
        itemseleccionado = tabla.focus()
        datos = tabla.item(itemseleccionado).get('values')[1]
        if messagebox.askyesno("¿Deseas eliminar?","¿Deseas eliminar el elemento \"{}?\"".format(datos)):
            # aqui se eliminar el elemento de la base de datos
            tabla.delete(itemseleccionado)
            messagebox.showinfo("Eliminado","El elemento fue eliminado")
        else:
            pass

    # solo genera pdfs y los guarda en otra carpeta
    def _generarPdf(self,opc):
        match opc:
            case 'libro':
                tablaLibro ="""
                        SELECT libro.ID, Titulo, autor.Nombre, editorial.Nombre, stock FROM libro
                        INNER JOIN autor ON libro.ID_Autor = autor.ID
                        INNER JOIN editorial ON libro.ID_Editorial = editorial.ID;
                        """
                ColumnasLibro = ["ID","Titulo","Autor","Editorial", "Stock"]
                nombre = 'lista_de_libros'
                listaImpresa.generarPdf(tablaLibro,ColumnasLibro,nombre)
                impresora.imprimirPDF(nombre)
            case 'compras':
                tablaCompras= """
                        SELECT movimiento.ID, libro.Titulo, proveedor.Nombre AS Proveedor, 
                        Fecha, Cantidad, Total_neto FROM movimiento
                        INNER JOIN libro On movimiento.ID_Libro = libro.ID
                        INNER JOIN proveedor On movimiento.ID_Proveedor = proveedor.ID;
                        """

                ColumnasCompras= ["ID","Titulo","Proveedor","Fecha","Cantidad", "Total neto"]
                nombre = 'lista_de_compras'
                listaImpresa.generarPdf(tablaCompras,ColumnasCompras,nombre)
                impresora.imprimirPDF(nombre)
            case 'ventas':
                tablaVentas= """
                        SELECT movimiento.ID, libro.Titulo, Fecha, Cantidad, Total_neto FROM movimiento
                        INNER JOIN libro ON movimiento.ID_Libro = libro.ID
                        WHERE movimiento.ID_Tipo_movimiento = 1;
                        """

                ColumnasVentas= ["ID","Titulo","Fecha","Cantidad", "Total neto"]
                nombre = 'lista_de_ventas'
                listaImpresa.generarPdf(tablaVentas,ColumnasVentas,nombre)
                impresora.imprimirPDF(nombre)
            case _:
                pass
