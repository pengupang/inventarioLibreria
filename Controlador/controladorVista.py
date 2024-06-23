#imports de clases
from Controlador.controladorFunciones import ControladorFunciones
from Vista.Editar_view import EditarFrames
from Vista.Ingresar_view import IngresarFrames
from Vista.menúPrincipal import VentanaPrincipal
from Vista.login_view import LoginView
from Vista.Ver_view import VerFrames
from Vista.toolBar import ToolBar


#Controlador encargado de realizar los cambios de frames dentro de la ventana principal
class Controlador_vista ():
    def __init__(self) -> None:
        #define la ventana y el controlador de funciones
        self.ventana = VentanaPrincipal()
        self.controlador_funciones= ControladorFunciones()
        self.frame_actual = None
        #llama a la funcion que muestra el login al iniciar el programa
        self.mostrar_Login()

        #funcion que muestra la interfaz de login 
    def mostrar_Login(self):
        self.login_view = LoginView(self.ventana,self.iniciar_sesion)
        self.login_view.pack()

        #funcion para poder iniciar sesion
    def iniciar_sesion(self,usuario,contraseña):
        #recibe datos desde el login para validar el inicio de sesion
        #esta validacion se hace en el controlador funciones
        usuario_valido = self.controlador_funciones.validar_usuario(usuario,contraseña)
        #en caso de que el usuario sea valido 
        if usuario_valido:
            #destruye la view del login
            self.login_view.destroy()
            #y llama a la funcion que muestra el toolBar en la ventana principal
            self.mostrar_toolbar()
        else:
           #por ahora no hace nada al ingresar datos erroneos
           pass
        #funcion que muestra la toolbar en la ventana principal
    def mostrar_toolbar(self):
        self.toolbar = ToolBar(self.ventana, self.cambiarFrame)
        self.toolbar.pack(fill="x")
    
    def cambiarFrame(self,texto):
        for widget in self.ventana.winfo_children():
            widget.destroy()

 
        self.mostrar_toolbar()

