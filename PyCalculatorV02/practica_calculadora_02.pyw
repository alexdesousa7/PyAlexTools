from tkinter import *

raiz = Tk()

raiz.title("Calculadora Básica v2")
raiz.iconbitmap("alexdesousa_icono.ico")

miFrame = Frame(raiz)
miFrame.pack()

operacion = ""
reset_pantalla = False
resultado = 0

# :::::::::::::::::: Pantalla :::::::::::::::::::::::::::::

numeroPantalla = StringVar()

pantalla = Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")


# ::::::::::::::::::::: Pulsaciones Teclado :::::::::::::::::::::

def numeroPulsado(num):
    global operacion, reset_pantalla

    if reset_pantalla:
        numeroPantalla.set(num)
        reset_pantalla = False
    else:
        numeroPantalla.set(numeroPantalla.get() + num)


# :::::::::::::::::::: funcion sumar :::::::::::::::::::::::::::

def suma(num):
    global operacion, resultado, reset_pantalla
    resultado += int(num)
    operacion = "suma"
    reset_pantalla = True
    numeroPantalla.set(resultado)


# :::::::::::::::::::: funcion resta :::::::::::::::::::::::::::

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


# :::::::::::::::::::: funcion multiplicacion :::::::::::::::::::

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


# :::::::::::::::::::: funcion division :::::::::::::::::::::::::

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


# :::::::::::::::::::::: funcion el resultado :::::::::::::::::::::::

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


# :::::::::::::::::::::: Botones :::::::::::::::::::::::::::::::::

# Fila 1
Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9")).grid(row=2, column=3)
Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8")).grid(row=2, column=2)
Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7")).grid(row=2, column=1)
Button(miFrame, text="/", width=3, command=lambda:divide(numeroPantalla.get())).grid(row=2, column=4)

# Fila 2
Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6")).grid(row=3, column=3)
Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5")).grid(row=3, column=2)
Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4")).grid(row=3, column=1)
Button(miFrame, text="X", width=3, command=lambda:multiplica(numeroPantalla.get())).grid(row=3, column=4)

# Fila 3
Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3")).grid(row=4, column=3)
Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2")).grid(row=4, column=2)
Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1")).grid(row=4, column=1)
Button(miFrame, text="-", width=3, command=lambda:resta(numeroPantalla.get())).grid(row=4, column=4)

# Fila 4
Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0")).grid(row=5, column=3)
Button(miFrame, text=",", width=3, command=lambda:numeroPulsado(".")).grid(row=5, column=2)
Button(miFrame, text="=", width=3, command=el_resultado).grid(row=5, column=1)
Button(miFrame, text="+", width=3, command=lambda:suma(numeroPantalla.get())).grid(row=5, column=4)

raiz.mainloop()