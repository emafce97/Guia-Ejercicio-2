class Ejercicio4:

    def __init__(self):
        self.domicilios = set()

    def cargar_domicilios(self,tuplas_ventas):
        for venta in tuplas_ventas:
            self.domicilios.add(venta[3])

    def mostrar_domicilios(self):
        for domicilio in self.domicilios:
            print(domicilio)

if __name__ == "__main__":
    e4 = Ejercicio4()
    lista = [("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), ("Jorge Russo", 7, 699, "Mirasol 218"), ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), ("Jorge Russo", 15, 958, "Mirasol 218")]
    e4.cargar_domicilios(lista)
    e4.mostrar_domicilios()
