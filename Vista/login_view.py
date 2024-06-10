import customtkinter 
from tkinter import *
from tkinter import ttk

class LoginView ():
    def __init__(self) -> None:
        pass
    ventana = customtkinter.CTk()
    customtkinter.set_appearance_mode("light")
    customtkinter.set_default_color_theme("blue")        

    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()

    ancho_ventana = 500
    alto_ventana = 400
    posicion_x = (ancho_pantalla - ancho_ventana) // 2 
    posicion_y = (alto_pantalla - alto_ventana) // 2

    lblUsuario = Label(text="Usuario")
    lblUsuario.place(rely=0.45,relx=0.5,anchor=CENTER)

    txtUsuario = ttk.Entry()
    txtUsuario.place(rely=0.5,relx=0.5,anchor=CENTER)

    lblContraseña = Label(text="Contraseña")
    lblContraseña.place(rely=0.55,relx=0.5,anchor=CENTER)

    txtContraseña = ttk.Entry()
    txtContraseña.place(rely=0.6,relx=0.5,anchor=CENTER)

    btnEntrar = customtkinter.CTkButton(ventana,text="Ingresar")
    btnEntrar.place(rely=0.7,relx=0.5,anchor=CENTER)



    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")



    ventana.mainloop()