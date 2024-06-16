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
    
    
  
