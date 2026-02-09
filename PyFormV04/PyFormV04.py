from tkinter import *
import pickle
from tkinter import messagebox


# ::::::::::::::::::::::::ARCHIVO DONDE SE GUARDAN LOS DATOS ::::::::::::::::::::::::

FICHERO = "datos.dat"

# :::::::::::::::::::::::: FUNCIONES ::::::::::::::::::::::::

def guardar_datos():
    if aceptar_condiciones.get() == 0:
        messagebox.showwarning("Aviso", "Debes aceptar las condiciones para continuar")
        return

    nombre = cuadroNombre.get()
    apellido = cuadroApellido.get()
    edad = cuadroEdad.get()
    correo = cuadroCorreo.get()
    usuario = cuadroUsuario.get()
    password = cuadroPassword.get()
    genero = varGenero.get()

    if genero == 1:
        genero_texto = "Masculino"
    elif genero == 2:
        genero_texto = "Femenino"
    else:
        genero_texto = "Otro"

    datos_persona = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "correo": correo,
        "usuario": usuario,
        "password": password,
        "genero": genero_texto
    }

    try:
        with open(FICHERO, "rb") as f:
            lista = pickle.load(f)
    except:
        lista = []

    lista.append(datos_persona)

    with open(FICHERO, "wb") as f:
        pickle.dump(lista, f)

    messagebox.showinfo("Éxito", "Datos guardados correctamente")

    limpiar_campos()


def limpiar_campos():
    cuadroNombre.delete(0, END)
    cuadroApellido.delete(0, END)
    cuadroEdad.delete(0, END)
    cuadroCorreo.delete(0, END)
    cuadroUsuario.delete(0, END)
    cuadroPassword.delete(0, END)
    varGenero.set(0)
    aceptar_condiciones.set(0)



# :::::::::::::::::::::::: INTERFAZ GRÁFICA ::::::::::::::::::::::::

raiz = Tk()
raiz.title("PyFormV03")
raiz.iconbitmap("alexdesousa_icono.ico")

miFrame = Frame(raiz, width=400, height=400)
miFrame.pack(padx=20, pady=20)

# Entradas
Label(miFrame, text="Nombre:").grid(row=0, column=0, sticky="e", padx=10, pady=5)
cuadroNombre = Entry(miFrame)
cuadroNombre.grid(row=0, column=1)

Label(miFrame, text="Apellido:").grid(row=1, column=0, sticky="e", padx=10, pady=5)
cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=1, column=1)

Label(miFrame, text="Edad:").grid(row=2, column=0, sticky="e", padx=10, pady=5)
cuadroEdad = Entry(miFrame)
cuadroEdad.grid(row=2, column=1)

Label(miFrame, text="Correo:").grid(row=3, column=0, sticky="e", padx=10, pady=5)
cuadroCorreo = Entry(miFrame)
cuadroCorreo.grid(row=3, column=1)

Label(miFrame, text="Usuario:").grid(row=4, column=0, sticky="e", padx=10, pady=5)
cuadroUsuario = Entry(miFrame)
cuadroUsuario.grid(row=4, column=1)

Label(miFrame, text="Password:").grid(row=5, column=0, sticky="e", padx=10, pady=5)
cuadroPassword = Entry(miFrame, show="*")
cuadroPassword.grid(row=5, column=1)

# Género (Radio Buttons)
Label(miFrame, text="Género:").grid(row=6, column=0, sticky="e", padx=10, pady=5)

varGenero = IntVar()
Radiobutton(miFrame, text="Masculino", variable=varGenero, value=1).grid(row=6, column=1, sticky="w")
Radiobutton(miFrame, text="Femenino", variable=varGenero, value=2).grid(row=7, column=1, sticky="w")
Radiobutton(miFrame, text="Otro", variable=varGenero, value=3).grid(row=8, column=1, sticky="w")

# Check de aceptación
aceptar_condiciones = IntVar()
Checkbutton(miFrame, text="Acepto que mis datos sean almacenados", variable=aceptar_condiciones).grid(row=9, column=1, pady=10)

# Botón enviar
botonEnvio = Button(raiz, text="Enviar", command=guardar_datos)
botonEnvio.pack(pady=10)

raiz.mainloop()