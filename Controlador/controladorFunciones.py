class ControladorFunciones:
    def __init__(self):
        # Usuarios de prueba para ingresar
        self.usuarios_validos = {
            "q": "a",
            "user2": "password2"
        }

    def validar_usuario(self, usuario, contraseña):
        return self.usuarios_validos.get(usuario) == contraseña
