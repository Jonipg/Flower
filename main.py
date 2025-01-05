import tkinter as tk
from subprocess import Popen
from PIL import ImageTk, Image
import os

def ejecutar_flor2():
    ruta_script = os.path.dirname(os.path.abspath(__file__))
    archivo = os.path.join(ruta_script, 'flor2.py')
    Popen(['python', archivo])

def ejecutar_flor_chida():
    ruta_script = os.path.dirname(os.path.abspath(__file__))
    archivo = os.path.join(ruta_script, 'FlorChida.py')
    Popen(['python', archivo])

root = tk.Tk()
root.title("Flores")
root.geometry("800x400")  # Establece el tamaño de la ventana en 800x600 píxeles

rutaFondo ="D:/Proyectos Python/Flores/Resse1.jpg"
image =Image.open(rutaFondo)
image_tk = ImageTk.PhotoImage(image)

label_fondo = tk.Label(root, image=image_tk)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

boton_flor2 = tk.Button(root, text="Ejecutar Opcion 1", command=ejecutar_flor2, font=("Arial", 14), width=15, height=3)
boton_flor2.pack()

boton_flor_chida = tk.Button(root, text="Ejecutar Opcion 2", command=ejecutar_flor_chida, font=("Arial", 14), width=15, height=3)
boton_flor_chida.pack()

root.mainloop()