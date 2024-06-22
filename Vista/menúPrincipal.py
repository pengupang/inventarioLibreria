import os
from customtkinter import *

# En esta clase Es donde aparecen todos los frames
#Es el contenedor pricipal
class VentanaPrincipal (CTk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Sistema Inventario")
        ancho_pantalla = self.winfo_screenwidth()
        alto_pantalla = self.winfo_screenheight()

        ancho_ventana = 700
        alto_ventana = 600
        posicion_x = (ancho_pantalla - ancho_ventana) // 2 
        posicion_y = (alto_pantalla - alto_ventana) // 2
        self.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")
        self.config(background="#dbdbdb")
        self.main_frame = None

