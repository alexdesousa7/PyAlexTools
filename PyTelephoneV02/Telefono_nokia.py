from tkinter import *

class Nokia3310:
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title("Nokia 3310")
        self.raiz.iconbitmap("alexdesousa_icono.ico")

        self.raiz.config(bg="#1F3A5F")  # color de fondo general

        # Estado del teléfono
        self.estado = "reposo"  # reposo, marcando, llamando
        self.numero = StringVar()

        # Marco que simula el cuerpo del móvil
        self.cuerpo = Frame(self.raiz, bg="#2C4C7A", bd=10, relief="ridge")
        self.cuerpo.pack(padx=20, pady=20)

        self.crear_pantalla()
        self.crear_teclas()

    def crear_pantalla(self):
        # Marco de la pantalla
        marco_pantalla = Frame(self.cuerpo, bg="#1A2E45", bd=5, relief="sunken")
        marco_pantalla.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Pantalla tipo Nokia (fondo verdoso)
        self.lbl_pantalla = Label(
            marco_pantalla,
            textvariable=self.numero,
            font=("Comic Sans MS", 16),
            bg="#C7E5B4",
            fg="#000000",
            width=18,
            height=2,
            anchor="center",
            bd=2,
            relief="flat"
        )
        self.lbl_pantalla.pack()

        # Texto inicial
        self.numero.set("Nokia 3310")

    def crear_teclas(self):
        # Estilo general de teclas
        estilo_tecla = {
            "font": ("Comic Sans MS", 12),
            "bg": "#E0E4EC",
            "fg": "#000000",
            "width": 4,
            "height": 2,
            "bd": 1,
            "relief": "raised",
            "activebackground": "#B0B6C4",
            "activeforeground": "#000000"
        }

        # Fila de control (Arriba, Llamar, Colgar)
        Button(self.cuerpo, text="↑", command=self.nav_arriba, **estilo_tecla).grid(row=1, column=1, pady=(0, 5))

        Button(self.cuerpo, text="Llamar", command=self.llamar,
               bg="#4CAF50", fg="white",
               activebackground="#45A049", width=6, height=2,
               font=("Comic Sans MS", 10)).grid(row=1, column=0, padx=5)

        Button(self.cuerpo, text="Colgar", command=self.colgar,
               bg="#F44336", fg="white",
               activebackground="#D32F2F", width=6, height=2,
               font=("Comic Sans MS", 10)).grid(row=1, column=2, padx=5)

        # Teclado numérico
        teclas = [
            ("1", 2, 0), ("2", 2, 1), ("3", 2, 2),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2),
            ("7", 4, 0), ("8", 4, 1), ("9", 4, 2),
            ("*", 5, 0), ("0", 5, 1), ("#", 5, 2),
        ]

        for (texto, fila, col) in teclas:
            Button(
                self.cuerpo,
                text=texto,
                command=lambda t=texto: self.marcar(t),
                **estilo_tecla
            ).grid(row=fila, column=col, padx=3, pady=3)

        # Fila inferior: borrar
        Button(self.cuerpo, text="Borrar", command=self.borrar,
               bg="#FF9800", fg="white",
               activebackground="#FB8C00",
               width=8, height=2,
               font=("Comic Sans MS", 10)).grid(row=6, column=1, pady=(5, 0))

    # ---------------- Lógica del teléfono ----------------

    def marcar(self, digito):
        if self.estado in ("reposo", "marcando"):
            if self.numero.get() in ("Nokia 3310", "Llamando...", "Llamada finalizada"):
                self.numero.set("")
            self.estado = "marcando"
            self.numero.set(self.numero.get() + digito)

    def borrar(self):
        if self.estado == "marcando":
            actual = self.numero.get()
            self.numero.set(actual[:-1])
            if self.numero.get() == "":
                self.estado = "reposo"
                self.numero.set("Nokia 3310")

    def llamar(self):
        if self.estado == "marcando" and self.numero.get():
            self.estado = "llamando"
            num = self.numero.get()
            self.numero.set(f"Llamando a\n{num}")
        elif self.estado == "reposo":
            self.numero.set("Ningún número")
        elif self.estado == "llamando":
            self.numero.set("Ya estás en llamada")

    def colgar(self):
        if self.estado == "llamando":
            self.estado = "reposo"
            self.numero.set("Llamada finalizada")
        else:
            self.estado = "reposo"
            self.numero.set("Nokia 3310")

    def nav_arriba(self):
        # Aquí podrías simular un menú en el futuro
        if self.estado == "reposo":
            self.numero.set("Menú\n(placeholder)")
        elif self.estado == "marcando":
            pass  # podrías ignorar o hacer algo
        elif self.estado == "llamando":
            self.numero.set("En llamada...")

    def run(self):
        self.raiz.mainloop()


if __name__ == "__main__":
    app = Nokia3310()
    app.run()