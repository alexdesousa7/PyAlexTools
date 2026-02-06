from tkinter import *

class Telefono:
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title("Teléfono Retro")
        self.raiz.iconbitmap("alexdesousa_icono.ico")



        self.estado = "reposo"
        self.numero = StringVar()

        self.crear_pantalla()
        self.crear_botones()

    def crear_pantalla(self):
        self.pantalla = Entry(self.raiz, textvariable=self.numero,
                              font=("Comic Sans MS", 20),
                              bg="black", fg="#00FF88",
                              justify="center")
        self.pantalla.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    def marcar(self, digito):
        if self.estado == "reposo":
            self.numero.set(self.numero.get() + digito)

    def borrar(self):
        self.numero.set(self.numero.get()[:-1])

    def llamar(self):
        if self.numero.get():
            self.estado = "llamando"
            self.numero.set(f"Llamando a {self.numero.get()}...")

    def colgar(self):
        self.estado = "reposo"
        self.numero.set("")

    def crear_botones(self):
        botones = [
            ("1", 1, 0), ("2", 1, 1), ("3", 1, 2),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
            ("7", 3, 0), ("8", 3, 1), ("9", 3, 2),
            ("*", 4, 0), ("0", 4, 1), ("#", 4, 2),
        ]

        for (texto, fila, col) in botones:
            Button(self.raiz, text=texto, width=5, height=2,
                   command=lambda t=texto: self.marcar(t)).grid(row=fila, column=col)

        Button(self.raiz, text="Llamar", width=5, height=2,
               command=self.llamar).grid(row=5, column=0)

        Button(self.raiz, text="Colgar", width=5, height=2,
               command=self.colgar).grid(row=5, column=1)

        Button(self.raiz, text="DEL", width=5, height=2,
               command=self.borrar).grid(row=5, column=2)

    def run(self):
        self.raiz.mainloop()

app = Telefono()
app.run()