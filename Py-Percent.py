from tkinter import *
# como base usare el py-calculator para poder hacer el py-porcentaje
# comentare algunas lineas del codigo original para poder realizar el calculo en %

#def sumar():
#    r.set( float(n1.get()) + float(n2.get()) )
#    borrar()

#def resta():
#    r.set( float(n1.get()) - float(n2.get()) )
#    borrar()

def multiplicar():
    r.set( float(n1.get()) % float(n2.get()) )
    borrar()


#def dividir():
#    r.set(float(n1.get()) / float(n2.get()))
#    borrar()

def borrar():
    n1.set("")
    n2.set("")

# Configuración de la raíz
root = Tk()
root.title("Bienvenidos a Py-Percent")
root.resizable(1, 1)
#root = Frame(root, width=480, height=320)
#root.config(cursor="arrow")
root.config(cursor="pirate")
root.config(bg="lightgreen")
root.config(relief="ridge")
root.config(bd=15)

n1 = StringVar()
n2 = StringVar()
r = StringVar()

Label(root, text="Número 1").pack()
Entry(root, justify="center", textvariable=n1).pack()

Label(root, text="Número 2").pack()
Entry(root, justify="center", textvariable=n2).pack()

Label(root, text="Resultado").pack()
Entry(root, justify="center", textvariable=r, state="disabled").pack()

Label(root, text="").pack()  # Separador

#Button(root, justify="center", text="Sumar", font=("Comic Sans MS", 10), command=sumar).pack(side="left")
#Button(root, justify="center", text="Resta", font=("Comic Sans MS", 10), command=resta).pack(side="left")
Button(root, justify="center", text="Porcentaje", font=("Comic Sans MS", 10), command=multiplicar).pack(side="left")
#Button(root, justify="center", text="Dividir", font=("Comic Sans MS", 10), command=dividir).pack(side="left")

# Finalmente bucle de la aplicación
root.mainloop()
