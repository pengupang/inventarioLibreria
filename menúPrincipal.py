import os
from tkinter import *
import tkinter as tk
from toolBar import ToolBar
import customtkinter 


ventana = customtkinter.CTk()

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

ancho_ventana = 700
alto_ventana = 600
posicion_x = (ancho_pantalla - ancho_ventana) // 2 
posicion_y = (alto_pantalla - alto_ventana) // 2

ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")

#obtiene dir actual
path_actual = os.getcwd()
#obtiene el dir de las imagenes en este caso utiliza el path del dir actual
#ya que las imagenes estan en un dir dentro
folder_imagen = os.path.join(path_actual,"img")
#con ambos path juntos busca la imagen
path_imagen = os.path.join(folder_imagen,"libro-abierto.png")
#la imagen se agrega a u label para ser mostrada
imagen= PhotoImage(file=path_imagen)
iLabel= tk.Label(ventana, image=imagen)
#se acomoda la imagen 
iLabel.place(relx=0.5 , rely=0.5,anchor=CENTER)
ToolBar(ventana)

ventana.mainloop()