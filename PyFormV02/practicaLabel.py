from tkinter import *

root = Tk()

miFrame = Frame(root, width=500, height=400)
miFrame.pack()

# Crear el Label correctamente
miLabel = Label(miFrame, text="Estoy aprendiendo Python", fg="red", font=("Comic Sans MS", 18))
miLabel.place(x=80, y=150)

# Botón Enviar
botonEnvio = Button(miFrame, text="Enviar")
botonEnvio.place(x=220, y=250)

root.mainloop()
