from Controlador.controladorVista import Controlador_vista
import customtkinter

if __name__ == "__main__":
    customtkinter.set_appearance_mode("light")
    controlador = Controlador_vista()
    controlador.ventana.mainloop()
