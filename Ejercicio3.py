class Ejercicio3:

    def __init__(self):
        self.nombres_primaria = set()
        self.nombres_secundiaria = set()

    def ingresarNombres(self):
        self.__agregarNombresPrimaria()
        self.__agregarNombresSecundaria()

    def __agregarNombresPrimaria(self):
        termino = False
        while not termino:
            nombre = input("Ingrese un nombre de un alumno de primaria: ")
            if nombre == "x":
                termino = True
            else:
                self.nombres_primaria.add(nombre)

    def __agregarNombresSecundaria(self):
        termino = False
        while not termino:
            nombre = input("Ingrese un nombre de un alumno de secundaria: ")
            if nombre == "x":
                termino = True
            else:
                self.nombres_secundiaria.add(nombre)

    def listarNombres(self):
        print("Nombres de alumnos de primaria:")
        for nombre in self.nombres_primaria:
            print(nombre)
        print("Nombres de alumnos de secundaria:")
        for nombre in self.nombres_secundiaria:
            print(nombre)

    def getNombresRepetidos(self):
        nombres = []

        for nombre in self.nombres_primaria:
            if nombre in self.nombres_secundiaria:
                nombres.append(nombre)
        print(f"Nombres repetidos en primaria y secundaria:\n {nombres}")

    def getNombresNoRepetidos(self):
        nombres = []
        for nombre in self.nombres_primaria:
            if not nombre in self.nombres_secundiaria:
                nombres.append(nombre)
        for nombre in self.nombres_secundiaria:
            if not nombre in self.nombres_primaria:
                nombres.append(nombre)
        print(f"Nombres no repetidos en primaria y secundaria:\n {nombres}")

if __name__ == "__main__":
    e3 = Ejercicio3()
    e3.ingresarNombres()
    e3.listarNombres()
    e3.getNombresRepetidos()
    e3.getNombresNoRepetidos()

