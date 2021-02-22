from tkinter import *
from tkinter import filedialog as FileDialog
from io import open

ruta = "" # La utilizaremos para almacenar la ruta del fichero predeterminada

def nuevo():
    global ruta
    mensaje.set("Archivo Nuevo")
    ruta = ""
    texto.delete(1.0, "end")
    root.title("Py-Note V.1.0")

def abrir():
    global ruta
    mensaje.set("Abrir Archivo")
    ruta = FileDialog.askopenfilename(
        initialdir='.', 
        filetypes=(("Ficheros de texto", "*.txt"),), # De Momento solo se abriran archivos txt
        title="Abrir un archivo de texto")

    if ruta != "":
        fichero = open(ruta, 'r')
        contenido = fichero.read()
        texto.delete(1.0,'end')
        texto.insert('insert', contenido)
        fichero.close()
        root.title(ruta + " - Py-Note")

def guardar():
    mensaje.set("Guardar archivo")
    if ruta != "":
        contenido = texto.get(1.0,'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Archivo guardado correctamente")
    else:
        guardar_como()

def guardar_como():
    global ruta
    mensaje.set("Guardar archivo como")

    fichero = FileDialog.asksaveasfile(title="Guardar archivo", 
        mode="w", defaultextension=".txt") # Mencionado arriba solo puede guardar de momento archivos txt

    if fichero is not None:
        ruta = fichero.name
        contenido = texto.get(1.0,'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Archivo guardado correctamente")
    else:
        mensaje.set("Guardado cancelado")
        ruta = ""


# Configuración de la raíz
root = Tk()
root.title("Py-Note V.1.0")

# Menú superior
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", font=("Comic Sans MS", 10), command=nuevo)
filemenu.add_command(label="Abrir", font=("Comic Sans MS", 10), command=abrir)
filemenu.add_command(label="Guardar", font=("Comic Sans MS", 10), command=guardar)
filemenu.add_command(label="Guardar como", font=("Comic Sans MS", 10), command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Salir", font=("Comic Sans MS", 10), command=root.quit)
menubar.add_cascade(menu=filemenu, label="Archivo")

# Caja de texto central
texto = Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0, padx=6, pady=4, font=("Comic Sans MS", 10))

# Monitor inferior
mensaje = StringVar()
mensaje.set("Bienvenido al Py-Note V.1.0")
monitor = Label(root, textvar=mensaje, font=("Comic Sans MS", 10), justify='left')
monitor.pack(side="left")

root.config(menu=menubar)
# Finalmente bucle de la apliación
root.mainloop()
