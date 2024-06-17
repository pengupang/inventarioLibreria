#Controlador encargado de realizar funciones que necesiten pasar por la base de datos
# y realizar un retorno de datos 

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
            print("contraseñas mal puestas") 
    
    
    def cargarDatos(self,tabla,query):
        resultados= conexion.ejecutar_consulta(query)
        print(resultados)
        if resultados:
                for row in resultados:
                    tabla.insert("", "end", values=row)
        else:
                print("No se encontraron registros")

    def guardar_datos(self):
        id_value = self.entry_id.get()
        titulo_value = self.entry_titulo.get()
        autor_value = self.entry_autor.get()
        stock_value = self.entry_stock.get()

        sql = "INSERT INTO nombre_de_la_tabla (ID, Titulo, Autor, Stock) VALUES (%s, %s, %s, %s)"
        val = (id_value, titulo_value, autor_value, stock_value)

        # Ejecutar la consulta SQL
        self.cursor.execute(sql, val)

        # Confirmar la transacción
        self.conexion.commit()

        