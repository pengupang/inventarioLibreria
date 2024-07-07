
from customtkinter import *
from tkinter import messagebox

# En esta clase Es donde aparecen todos los frames
#Es el contenedor pricipal
class VentanaPrincipal (CTk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Sistema Inventario")
        
        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))
        self.bind("<Escape>", self.exit_maximize)
       
        self.config(background="#dbdbdb")
        self.main_frame = None

        self.protocol("WM_DELETE_WINDOW",self.cerrarVentana)
        

    def cerrarVentana(self):
        cerrar= messagebox.askyesno(message="Está seguro que quiere cerrar la aplicación?", title= "Confirmar cierre")

        if cerrar:
            self.destroy()
    
    def exit_maximize(self, event=None):
        self.state('normal')

