from tkinter import *
import math

class Calculadora:
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title("Calculadora OOP V005")
        self.raiz.iconbitmap("alexdesousa_icono.ico")


        self.operacion = ""
        self.reset_pantalla = False
        self.resultado = 0

        self.frame = Frame(self.raiz, bg="#222831")
        self.frame.pack(padx=20, pady=20)

        self.numeroPantalla = StringVar()

        self.crear_pantalla()
        self.crear_botones()

    def crear_pantalla(self):
        self.pantalla = Entry(self.frame, textvariable=self.numeroPantalla,
                              font=("Comic Sans MS", 22), bd=12,
                              background="#000000", fg="#00FF88",
                              justify="right")
        self.pantalla.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

    def crear_botones(self):
        estilo = {
            "bg": "#393E46",
            "fg": "#EEEEEE",
            "activebackground": "#00ADB5",
            "activeforeground": "#FFFFFF",
            "font": ("Comic Sans MS", 16),
            "width": 4,
            "height": 1,
            "bd": 0
        }

        # Botones CE y C
        Button(self.frame, text="CE", bg="#FF5722", fg="white",
               font=("Comic Sans MS", 16),
               command=self.borrar_entrada).grid(row=1, column=0)

        Button(self.frame, text="C", bg="#D32F2F", fg="white",
               font=("Comic Sans MS", 16),
               command=self.borrar_todo).grid(row=1, column=1)

        # Números y operaciones
        botones = [
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("X", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3),
            ("0", 5, 0), (".", 5, 1), ("=", 5, 2), ("+", 5, 3)
        ]

        for (texto, fila, col) in botones:
            if texto.isdigit() or texto == ".":
                cmd = lambda t=texto: self.numero_pulsado(t)
            elif texto == "=":
                cmd = self.el_resultado
            elif texto == "+":
                cmd = lambda: self.suma(self.numeroPantalla.get())
            elif texto == "-":
                cmd = lambda: self.resta(self.numeroPantalla.get())
            elif texto == "X":
                cmd = lambda: self.multiplica(self.numeroPantalla.get())
            elif texto == "/":
                cmd = lambda: self.divide(self.numeroPantalla.get())

            Button(self.frame, text=texto, command=cmd, **estilo).grid(row=fila, column=col)

    # ------------------ Lógica ------------------

    def numero_pulsado(self, num):
        if self.reset_pantalla:
            self.numeroPantalla.set(num)
            self.reset_pantalla = False
        else:
            self.numeroPantalla.set(self.numeroPantalla.get() + num)

    def borrar_entrada(self):
        self.numeroPantalla.set("")

    def borrar_todo(self):
        self.operacion = ""
        self.resultado = 0
        self.reset_pantalla = False
        self.numeroPantalla.set("")

    def suma(self, num):
        self.resultado += int(num)
        self.operacion = "suma"
        self.reset_pantalla = True
        self.numeroPantalla.set(self.resultado)

    def resta(self, num):
        if self.operacion != "resta":
            self.resultado = int(num)
        else:
            self.resultado -= int(num)

        self.operacion = "resta"
        self.reset_pantalla = True
        self.numeroPantalla.set(self.resultado)

    def multiplica(self, num):
        if self.operacion != "multiplicacion":
            self.resultado = int(num)
        else:
            self.resultado *= int(num)

        self.operacion = "multiplicacion"
        self.reset_pantalla = True
        self.numeroPantalla.set(self.resultado)

    def divide(self, num):
        if self.operacion != "division":
            self.resultado = float(num)
        else:
            self.resultado /= float(num)

        self.operacion = "division"
        self.reset_pantalla = True
        self.numeroPantalla.set(self.resultado)

    def el_resultado(self):
        num = self.numeroPantalla.get()

        if self.operacion == "suma":
            self.numeroPantalla.set(self.resultado + int(num))

        elif self.operacion == "resta":
            self.numeroPantalla.set(self.resultado - int(num))

        elif self.operacion == "multiplicacion":
            self.numeroPantalla.set(self.resultado * int(num))

        elif self.operacion == "division":
            self.numeroPantalla.set(self.resultado / float(num))

        self.operacion = ""
        self.resultado = 0

    def run(self):
        self.raiz.mainloop()


# Ejecutar

app = Calculadora()
app.run()