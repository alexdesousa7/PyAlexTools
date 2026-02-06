from tkinter import *
import math

class CalculadoraCientifica:
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title("Calculadora Científica")
        self.raiz.iconbitmap("alexdesousa_icono.ico")


        self.frame = Frame(self.raiz, bg="#222831")
        self.frame.pack(padx=20, pady=20)

        self.expresion = StringVar()

        self.crear_pantalla()
        self.crear_botones()

    def crear_pantalla(self):
        self.pantalla = Entry(
            self.frame,
            textvariable=self.expresion,
            font=("Comic Sans MS", 22),
            bd=12,
            background="#000000",
            fg="#00FF88",
            justify="right"
        )
        self.pantalla.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

    def agregar(self, valor):
        self.expresion.set(self.expresion.get() + valor)

    def borrar_uno(self):
        self.expresion.set(self.expresion.get()[:-1])

    def borrar_todo(self):
        self.expresion.set("")

    def calcular(self):
        try:
            expr = self.expresion.get()

            funciones = {
                "sin": math.sin,
                "cos": math.cos,
                "tan": math.tan,
                "sqrt": math.sqrt,
                "log": math.log,
                "pi": math.pi,
                "e": math.e,
                "pow": pow,
                "factorial": math.factorial
            }

            resultado = eval(expr, {"__builtins__": None}, funciones)
            self.expresion.set(str(resultado))

        except Exception:
            self.expresion.set("Error")

    def crear_botones(self):
        estilo = {
            "bg": "#393E46",
            "fg": "#EEEEEE",
            "activebackground": "#00ADB5",
            "activeforeground": "#FFFFFF",
            "font": ("Comic Sans MS", 14),
            "width": 5,
            "height": 1,
            "bd": 0
        }

        # Botones especiales
        Button(self.frame, text="AC", bg="#D32F2F", fg="white",
               font=("Comic Sans MS", 14),
               command=self.borrar_todo).grid(row=1, column=0)

        Button(self.frame, text="DEL", bg="#FF5722", fg="white",
               font=("Comic Sans MS", 14),
               command=self.borrar_uno).grid(row=1, column=1)

        Button(self.frame, text="(", command=lambda:self.agregar("("), **estilo).grid(row=1, column=2)
        Button(self.frame, text=")", command=lambda:self.agregar(")"), **estilo).grid(row=1, column=3)
        Button(self.frame, text="^", command=lambda:self.agregar("**"), **estilo).grid(row=1, column=4)
        Button(self.frame, text="√", command=lambda:self.agregar("sqrt("), **estilo).grid(row=1, column=5)

        # Fila 2
        Button(self.frame, text="7", command=lambda:self.agregar("7"), **estilo).grid(row=2, column=0)
        Button(self.frame, text="8", command=lambda:self.agregar("8"), **estilo).grid(row=2, column=1)
        Button(self.frame, text="9", command=lambda:self.agregar("9"), **estilo).grid(row=2, column=2)
        Button(self.frame, text="/", command=lambda:self.agregar("/"), **estilo).grid(row=2, column=3)
        Button(self.frame, text="sin", command=lambda:self.agregar("sin("), **estilo).grid(row=2, column=4)
        Button(self.frame, text="cos", command=lambda:self.agregar("cos("), **estilo).grid(row=2, column=5)

        # Fila 3
        Button(self.frame, text="4", command=lambda:self.agregar("4"), **estilo).grid(row=3, column=0)
        Button(self.frame, text="5", command=lambda:self.agregar("5"), **estilo).grid(row=3, column=1)
        Button(self.frame, text="6", command=lambda:self.agregar("6"), **estilo).grid(row=3, column=2)
        Button(self.frame, text="*", command=lambda:self.agregar("*"), **estilo).grid(row=3, column=3)
        Button(self.frame, text="tan", command=lambda:self.agregar("tan("), **estilo).grid(row=3, column=4)
        Button(self.frame, text="log", command=lambda:self.agregar("log("), **estilo).grid(row=3, column=5)

        # Fila 4
        Button(self.frame, text="1", command=lambda:self.agregar("1"), **estilo).grid(row=4, column=0)
        Button(self.frame, text="2", command=lambda:self.agregar("2"), **estilo).grid(row=4, column=1)
        Button(self.frame, text="3", command=lambda:self.agregar("3"), **estilo).grid(row=4, column=2)
        Button(self.frame, text="-", command=lambda:self.agregar("-"), **estilo).grid(row=4, column=3)
        Button(self.frame, text="π", command=lambda:self.agregar("pi"), **estilo).grid(row=4, column=4)
        Button(self.frame, text="e", command=lambda:self.agregar("e"), **estilo).grid(row=4, column=5)

        # Fila 5
        Button(self.frame, text="0", command=lambda:self.agregar("0"), **estilo).grid(row=5, column=0)
        Button(self.frame, text=".", command=lambda:self.agregar("."), **estilo).grid(row=5, column=1)
        Button(self.frame, text="=", command=self.calcular, **estilo).grid(row=5, column=2)
        Button(self.frame, text="+", command=lambda:self.agregar("+"), **estilo).grid(row=5, column=3)
        Button(self.frame, text="x!", command=lambda:self.agregar("factorial("), **estilo).grid(row=5, column=4)
        Button(self.frame, text="pow", command=lambda:self.agregar("pow("), **estilo).grid(row=5, column=5)

    def run(self):
        self.raiz.mainloop()


# Ejecutar

app = CalculadoraCientifica()
app.run()