from Vista.menúPrincipal import VentanaPrincipal
from Controlador.controladorFunciones import ControladorFunciones
from Vista.login_view import LoginView
from Vista.toolBar import ToolBar

class Controlador_vista ():
    def __init__(self) -> None:
        self.ventana = VentanaPrincipal()
        self.controlador_funciones= ControladorFunciones()
        self.mostrar_Login()
    
    def mostrar_Login(self):
        self.login_view = LoginView(self.ventana,self.iniciar_sesion)
        self.login_view.pack()
    
    def iniciar_sesion(self,usuario,contraseña):
        usuario_valido = self.controlador_funciones.validar_usuario(usuario,contraseña)
        if usuario_valido:
            self.login_view.destroy()
            self.mostrar_toolbar()
        else:
           pass

    def mostrar_toolbar(self):
        self.toolbar = ToolBar(self.ventana)
        self.toolbar.pack(fill="both",expand=True)

if __name__ == "__main__":
    app=Controlador_vista()
    app.ventana.mainloop()