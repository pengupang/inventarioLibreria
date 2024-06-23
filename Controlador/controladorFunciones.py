#Controlador encargado de realizar funciones que necesiten pasar por la base de datos
# y realizar un retorno de datos 
from tkinter import messagebox
from Modelo import conexion
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

        