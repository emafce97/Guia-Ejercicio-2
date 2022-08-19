class Viajero:

    def __init__(self,nombre,dni,destino):
        self.nombre = nombre
        self.dni = dni
        self.destino = destino

    def getDni(self):
        return self.dni

    def getDestino(self):
        return self.destino

    def __str__(self):
        return f"{self.nombre} tiene el DNI {self.dni} y viaja a {self.destino}"

class Ejercicio2:

    def __init__(self):
        self.viajeros = []
        self.ciudades = {}

    def run(self):
        opcion = None
        while opcion != 8:
            print("---Ejercicio 2---"
                  "\nOpciones disponibles:"
                  "\n1-Agregar pasajero"
                  "\n2-Agregar ciudad"
                  "\n3-Buscar ciudad segun DNI"
                  "\n4-Mostrar cant de personas en ciudad"
                  "\n5-Mostrar a que pais viaja segun DNI"
                  "\n6-Mostrar cant pasajeros que viajan a un pais"
                  "\n7-Listar viajeros"
                  "\n8-Salir")
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1:
                self.agregarViajero()
            elif opcion == 2:
                self.agregarCiudad()
            elif opcion == 3:
                self.buscarCiudadPorPasajero()
            elif opcion == 4:
                self.getCantViajerosEnCiudad()
            elif opcion == 5:
                self.buscarPaisPorViajero()
            elif opcion == 6:
                self.getCantViajerosEnPais()
            elif opcion == 7:
                self.listarViajeros()

    def agregarViajero(self):
        """Se agrega un viajero a la lista de viajeros"""
        datos = input("Ingrese los datos [Nombre,DNI,Destino]: ").split(",")
        self.viajeros.append(Viajero(datos[0],int(datos[1]),datos[2]))
        print("-- OK --")

    def agregarCiudad(self):
        """Se agrega una ciudad al diccionario de ciudades"""
        datos = input("Ingrese el nombre y pais de la ciudad: ").split(",")
        self.ciudades[datos[0]] = datos[1]
        print("-- OK --")

    def buscarCiudadPorPasajero(self):
        """Busca una ciudad segun el DNI de un viajero"""
        dni = int(input("Ingrese el DNI del pasajero: "))
        for viajero in self.viajeros:
            if viajero.getDni() == dni:
                print(f"El viajero se encuentra en {viajero.getDestino()}")
        print("No se encuentra")

    def getCantViajerosEnCiudad(self):
        """Retorna la cantidad de viajeros en una ciudad"""
        ciudad = input("Ingrese el nombre de la ciudad: ")
        contador = 0
        for viajero in self.viajeros:
            if viajero.getDestino() == ciudad:
                contador += 1
        print(f"Hay {contador} viajero/s en {ciudad}")

    def buscarPaisPorViajero(self):
        """Retorna el pais en que se encuentra un viajero"""
        dni = int(input("Ingrese el DNI del pasajero: "))
        destino = None
        for viajero in self.viajeros:
            if viajero.getDni() == dni:
                destino = viajero.getDestino()
        print(f"El viajero se encuentra en {self.ciudades[destino]}")

    def getCantViajerosEnPais(self):
        """Retorna la cantidad de viajeros en un pais"""
        pais = input("Ingrese el nombre del pais: ")
        ciudad_es = []
        for ciudad in self.ciudades.keys():
            if self.ciudades[ciudad] == pais:
                ciudad_es.append(ciudad)
        contador = 0
        for viajero in self.viajeros:
            if viajero.getDestino() in ciudad_es:
                contador += 1
        print(f"Hay {contador} en {pais}")

    def listarViajeros(self):
        """Lista los viajeros cargados"""
        for viajero in self.viajeros:
            print(viajero)

if __name__ == "__main__":
    e2 = Ejercicio2()
    e2.run()