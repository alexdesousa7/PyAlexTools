from tkinter import *

root = Tk()

root.title("Ejemplo")

playa = IntVar()
montagna = IntVar()
ciudad = IntVar()
barrio = IntVar()
carcel = IntVar()

def opcionesViaje():
    opcionEscogida = ""

    if(playa.get()==1):
        opcionEscogida += " Playa Estrella Panama"

    if(montagna.get()==1):
        opcionEscogida += " Montaña Big Bear"

    if(ciudad.get()==1):
        opcionEscogida += " Ciudad Las Vegas"

    if(barrio.get()==1):
        opcionEscogida += " Petare y Chueca"

    if(carcel.get()==1):
        opcionEscogida += " Alcatraz e Isla Muerte"

    textoFinal.config(text=opcionEscogida)

# foto = PhotoImage(file="avion.png")
# Label(root, image=foto).pack()

frame = Frame(root)
frame.pack()

Label(frame, text="Elige un Destino...", width=50).pack()

Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Montaña", variable=montagna, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Ciudad", variable=ciudad, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Barrio", variable=barrio, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Carcel", variable=carcel, onvalue=1, offvalue=0, command=opcionesViaje).pack()

textoFinal=Label(frame)
textoFinal.pack()

root.mainloop()