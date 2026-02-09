import pickle
1
# 
# :::::::::::::::::::::::::: CLASE PERSONA ::::::::::::::::::::::::::
# 

class Persona:

    def __init__(self, nombre, apellido, genero, edad, telefono, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.genero = genero
        self.edad = edad
        self.telefono = telefono
        self.direccion = direccion

    def __str__(self):
        return f"{self.nombre} {self.apellido} | {self.genero} | {self.edad} años | Tel: {self.telefono} | Dir: {self.direccion}"


# 
# :::::::::::::::::::::::::: CLASE GESTOR DE PERSONAS ::::::::::::::::::::::::::
# 

class GestorPersonas:

    def __init__(self):
        self.personas = []
        self.fichero = "personas.dat"

        try:
            with open(self.fichero, "rb") as f:
                self.personas = pickle.load(f)
                print(f"Se cargaron {len(self.personas)} personas del fichero externo")
        except:
            print("El fichero está vacío o no existe")

    def guardar(self):
        with open(self.fichero, "wb") as f:
            pickle.dump(self.personas, f)

    def agregar(self, persona):
        self.personas.append(persona)
        self.guardar()

    def mostrar(self):
        if not self.personas:
            print("No hay personas registradas")
        else:
            print("\n--- LISTA DE PERSONAS ---")
            for p in self.personas:
                print(p)



# :::::::::::::::::::::::::: MENÚ INTERACTIVO ::::::::::::::::::::::::::


def menu():
    gestor = GestorPersonas()

    while True:
        print("\n--- MENÚ ---")
        print("1. Añadir persona")
        print("2. Mostrar personas")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            genero = input("Género: ")
            edad = input("Edad: ")
            telefono = input("Teléfono: ")
            direccion = input("Dirección: ")

            persona = Persona(nombre, apellido, genero, edad, telefono, direccion)
            gestor.agregar(persona)

        elif opcion == "2":
            gestor.mostrar()

        elif opcion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida")



# :::::::::::::::::::::::::: EJECUCIÓN DEL PROGRAMA ::::::::::::::::::::::::::

menu()