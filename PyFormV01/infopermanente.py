import pickle

class Persona:

    def __init__(self, nombre, apellido, genero, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.genero = genero
        self.edad = edad
        print("Se ha creado una persona nueva con el nombre de ", self.nombre)

    def __str__(self):
        return "{} {} {} {}".format(self.nombre, self.apellido, self.genero, self.edad)

class ListaPersonas:

    personas=[]

    def __init__(self):

        listaDePersonas=open("ficheroexterno", "ab+")
# con el parametro ab+ le indicamos que es un archivo de tipo binario

        listaDePersonas.seek(0)
# con el parametro seek(0) le indicamos que mueva el curso al inicio de la lista
        try:
            self.personas=pickle.load(listaDePersonas)
            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))

        except:
            print("El fichero esta vacio")

        finally:
            listaDePersonas.close()
            del(listaDePersonas)

    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersonasEnFicheroExterno()

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)
    
    def guardarPersonasEnFicheroExterno(self):
        listaDePersonas=open("ficheroexterno", "wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)

    def mostrarInformacionFicheroExterno(self):
        print("La informacion del fichero externo es la siguiente:")
        for p in self.personas:
            print(p) 


milista=ListaPersonas()
persona = Persona("Beto", "Benitez", "Masculino", 38)
milista.agregarPersonas(persona)
milista.mostrarInformacionFicheroExterno()




# ("Sandra", "Del Castillo", "Feminista", 39)
#p=Persona("Paco", "Guzman", "Masculino", 45)
#miLista=agregarpersona(p)
#p=Persona("Beto", "Benitez", "Masculino", 38)
#miLista=agregarpersona(p)
#p=Persona("Beatriz", "Orteza", "Feminino", 29)
#miLista=agregarpersona(p)

#milista=mostrarPersonas()
