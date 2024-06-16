#Controlador encargado de realizar funciones que necesiten pasar por la base de datos
# y realizar un retorno de datos 

class ControladorFunciones:
    def __init__(self):
        # Usuarios de prueba para ingresar
        self.usuarios_validos = {
            "q": "a",
            "user2": "password2"
        }
# funcion que verifica que el ususario se encuentra en la BD
# por ahora posee datos fijos dentro de la clase
    def validar_usuario(self, usuario, contraseña):
        return self.usuarios_validos.get(usuario) == contraseña
