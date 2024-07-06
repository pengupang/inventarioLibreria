from customtkinter import *
from PIL import Image


# En esta clase se carga Exclusivamente el frame de login 
#Ademas se envian datos desde los cuadros de texto a la determinada funcion que 
#realiza la verificación de usuario
class LoginView (CTkFrame):
    def __init__(self,master,callback) -> None:
        super().__init__(master)
        self.callback= callback
        self.mostrar_Login()
        
    
    def mostrar_Login(self):
        my_image = CTkImage(light_image=Image.open("Vista/img/acceso.png"),
                                  size=(120,120))
        CTkLabel(self, image=my_image, text="").place(relx=0.5, rely=0.28, anchor=CENTER)

        self.configure(width=700,height=600)
        self.pack_propagate(False)

        self.lblUsuario = CTkLabel(self,text="Usuario")
        self.lblUsuario.place(rely=0.45,relx=0.5,anchor=CENTER)

        self.txtUsuario = CTkEntry(self)
        self.txtUsuario.place(rely=0.5,relx=0.5,anchor=CENTER)

        self.lblContraseña = CTkLabel(self,text="Contraseña")
        self.lblContraseña.place(rely=0.55,relx=0.5,anchor=CENTER)

        self.txtContraseña = CTkEntry(self,show="*")
        self.txtContraseña.place(rely=0.6,relx=0.5,anchor=CENTER)

        btnEntrar = CTkButton(self,text="Ingresar")
        btnEntrar.configure(command=self.login)
        btnEntrar.place(rely=0.7, relx=0.5, anchor=CENTER) 

    def login(self):
        usuario= self.txtUsuario.get()
        contraseña = self.txtContraseña.get()
        self.callback(usuario,contraseña)