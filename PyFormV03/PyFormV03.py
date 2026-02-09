from tkinter import *

raiz = Tk()
raiz.iconbitmap("alexdesousa_icono.ico")

miFrame = Frame(raiz, width=1200, height=600)
miFrame.pack()

cuadroNombre = Entry(miFrame)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="right")

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=1, column=1, padx=10, pady=10)

cuadroPass = Entry(miFrame)
cuadroPass.grid(row=2, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

cuadroCorreo = Entry(miFrame)
cuadroCorreo.grid(row=3, column=1, padx=10, pady=10)



nombreLabel = Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

ApellidoLabel = Label(miFrame, text="Apellido:")
ApellidoLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

passLabel = Label(miFrame, text="Passowrd:")
passLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

CorreoLabel = Label(miFrame, text="Correo:")
CorreoLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)



varOpcion = IntVar()

def imprimir():

    print(varOpcion.get())    # para que imprima la seleccion en consola

    if varOpcion.get == 1:

        etiqueta.config(text="Has Elegido Masculino")

    else:

        etiqueta.config(text="Has Elegido Femenino")

Label(raiz, text="Selecciona Genero:").pack()

Radiobutton(raiz, text="Masculino", variable=varOpcion, value=1, command=imprimir).pack()

Radiobutton(raiz, text="Famenino", variable=varOpcion, value=2, command=imprimir).pack()

etiqueta = Label(raiz)
etiqueta.pack()



Terminos = IntVar()


def AceptarTerminos():
    opcionEscogida = ""

    if(Terminos.get()==1):
        opcionEscogida += " Acepta los Terminos"

varOpcion = IntVar()

frame = Frame(raiz)
frame.pack()

Label(frame, text="Acepta Los Terminos", width=50).pack()

Checkbutton(frame, text="Aceptar", variable=Terminos, onvalue=1, offvalue=0, command=AceptarTerminos).pack()

textoFinal=Label(frame)
textoFinal.pack()




botonEnvio = Button(raiz, text="Enviar")
botonEnvio.pack()

raiz.mainloop()

