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
path_imagen = "D:\escritorio\Taller Desarrollo aplicaciones\inventarioLibreria\img\libro-abierto.png"
imagen= PhotoImage(file=path_imagen)

iLabel= tk.Label(ventana, image=imagen)
iLabel.place(relx=0.5 , rely=0.5,anchor=CENTER)
ToolBar(ventana)

ventana.mainloop()