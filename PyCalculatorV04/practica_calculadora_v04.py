from tkinter import *

raiz = Tk()

raiz.title("Calculadora V4")
raiz.iconbitmap("alexdesousa_icono.ico")

miFrame = Frame(raiz, bg="#222831")
miFrame.pack(padx=20, pady=20)

operacion = ""
reset_pantalla = False
resultado = 0

# :::::::::::::::::: Pantalla :::::::::::::::::::::::::::::

numeroPantalla = StringVar()

pantalla = Entry(miFrame, textvariable=numeroPantalla, font=("Comic Sans MS", 22))
pantalla.grid(row=0, column=0, padx=10, pady=10, columnspan=5)
pantalla.config(background="#000000", fg="#00FF88", justify="right", bd=12)


# :::::::::::::::::: Funciones :::::::::::::::::::::::::::::

def numeroPulsado(num):
    global operacion, reset_pantalla

    if reset_pantalla:
        numeroPantalla.set(num)
        reset_pantalla = False
    else:
        numeroPantalla.set(numeroPantalla.get() + num)


def borrar_entrada():
    numeroPantalla.set("")


def borrar_todo():
    global resultado, operacion, reset_pantalla
    resultado = 0
    operacion = ""
    reset_pantalla = False
    numeroPantalla.set("")


def suma(num):
    global operacion, resultado, reset_pantalla
    resultado += int(num)
    operacion = "suma"
    reset_pantalla = True
    numeroPantalla.set(resultado)


num1 = 0
contador_resta = 0

def resta(num):
    global operacion, resultado, num1, contador_resta, reset_pantalla

    if contador_resta == 0:
        num1 = int(num)
        resultado = num1
    else:
        resultado = int(resultado) - int(num)

    numeroPantalla.set(resultado)
    contador_resta += 1
    operacion = "resta"
    reset_pantalla = True


contador_multi = 0

def multiplica(num):
    global operacion, resultado, num1, contador_multi, reset_pantalla

    if contador_multi == 0:
        num1 = int(num)
        resultado = num1
    else:
        resultado = int(resultado) * int(num)

    numeroPantalla.set(resultado)
    contador_multi += 1
    operacion = "multiplicacion"
    reset_pantalla = True


contador_divi = 0

def divide(num):
    global operacion, resultado, num1, contador_divi, reset_pantalla

    if contador_divi == 0:
        num1 = float(num)
        resultado = num1
    else:
        resultado = float(resultado) / float(num)

    numeroPantalla.set(resultado)
    contador_divi += 1
    operacion = "division"
    reset_pantalla = True


def el_resultado():
    global resultado, operacion
    global contador_resta, contador_multi, contador_divi

    if operacion == "suma":
        numeroPantalla.set(resultado + int(numeroPantalla.get()))
        resultado = 0

    elif operacion == "resta":
        numeroPantalla.set(int(resultado) - int(numeroPantalla.get()))
        resultado = 0
        contador_resta = 0

    elif operacion == "multiplicacion":
        numeroPantalla.set(int(resultado) * int(numeroPantalla.get()))
        resultado = 0
        contador_multi = 0

    elif operacion == "division":
        numeroPantalla.set(float(resultado) / float(numeroPantalla.get()))
        resultado = 0
        contador_divi = 0


# :::::::::::::::::: Estilo de botones :::::::::::::::::::::::::::::

estilo_boton = {
    "bg": "#393E46",
    "fg": "#EEEEEE",
    "activebackground": "#00ADB5",
    "activeforeground": "#FFFFFF",
    "font": ("Comic Sans MS", 16),
    "width": 4,
    "height": 1,
    "bd": 0
}

# :::::::::::::::::: Botones :::::::::::::::::::::::::::::

# Fila CE / C

boton_CE = Button(miFrame, text="CE", bg="#FF5722", fg="white", font=("Comic Sans MS", 16), command=borrar_entrada)
boton_CE.grid(row=1, column=0)

boton_C = Button(miFrame, text="C", bg="#D32F2F", fg="white", font=("Comic Sans MS", 16), command=borrar_todo)
boton_C.grid(row=1, column=1)

# Fila 1

Button(miFrame, text="7", command=lambda:numeroPulsado("7"), **estilo_boton).grid(row=2, column=0)
Button(miFrame, text="8", command=lambda:numeroPulsado("8"), **estilo_boton).grid(row=2, column=1)
Button(miFrame, text="9", command=lambda:numeroPulsado("9"), **estilo_boton).grid(row=2, column=2)
Button(miFrame, text="/", command=lambda:divide(numeroPantalla.get()), **estilo_boton).grid(row=2, column=3)

# Fila 2

Button(miFrame, text="4", command=lambda:numeroPulsado("4"), **estilo_boton).grid(row=3, column=0)
Button(miFrame, text="5", command=lambda:numeroPulsado("5"), **estilo_boton).grid(row=3, column=1)
Button(miFrame, text="6", command=lambda:numeroPulsado("6"), **estilo_boton).grid(row=3, column=2)
Button(miFrame, text="X", command=lambda:multiplica(numeroPantalla.get()), **estilo_boton).grid(row=3, column=3)

# Fila 3

Button(miFrame, text="1", command=lambda:numeroPulsado("1"), **estilo_boton).grid(row=4, column=0)
Button(miFrame, text="2", command=lambda:numeroPulsado("2"), **estilo_boton).grid(row=4, column=1)
Button(miFrame, text="3", command=lambda:numeroPulsado("3"), **estilo_boton).grid(row=4, column=2)
Button(miFrame, text="-", command=lambda:resta(numeroPantalla.get()), **estilo_boton).grid(row=4, column=3)

# Fila 4

Button(miFrame, text="0", command=lambda:numeroPulsado("0"), **estilo_boton).grid(row=5, column=0)
Button(miFrame, text=".", command=lambda:numeroPulsado("."), **estilo_boton).grid(row=5, column=1)
Button(miFrame, text="=", command=el_resultado, **estilo_boton).grid(row=5, column=2)
Button(miFrame, text="+", command=lambda:suma(numeroPantalla.get()), **estilo_boton).grid(row=5, column=3)

raiz.mainloop()