from tkinter import *

root = Tk()

varOpcion = IntVar()

def imprimir():

    print(varOpcion.get())    # para que imprima la seleccion en consola

    if varOpcion.get == 1:

        etiqueta.config(text="Has Elegido Masculino")

    elif varOpcion.get() == 2:

        etiqueta.config(text="Has Elegido Femenino")

    elif varOpcion.get() == 3:

        etiqueta.config(text="Has Elegido Gato")

    else:

        etiqueta.config(text="Has Elegido Perro")

Label(root, text="Selecciona Genero:").pack()

Radiobutton(root, text="Masculino", variable=varOpcion, value=1, command=imprimir).pack()

Radiobutton(root, text="Famenino", variable=varOpcion, value=2, command=imprimir).pack()

Radiobutton(root, text="Gato", variable=varOpcion, value=3, command=imprimir).pack()

Radiobutton(root, text="Perro", variable=varOpcion, value=4, command=imprimir).pack()

etiqueta = Label(root)
etiqueta.pack()

root.mainloop()