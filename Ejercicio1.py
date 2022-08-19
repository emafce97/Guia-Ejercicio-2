class Ejercicio1:

    def __init__(self):
        self.numeros = []

    def agregarNumero(self):
        termino = False
        while termino == False:
            numero = int(input("Ingrese un numero: "))
            if numero == 0:
                termino = True
            else:
                self.numeros.append(numero)

    def borrarPrimeraOcurrencia(self):
        numero = int(input("Ingrese un numero a borrar: "))
        try:
            self.numeros.remove(numero)
        except Exception as e:
            print(f"Ocurrio la excepcion: {e}")

    def mostrarElementos(self):
        for numero in self.numeros:
            print(numero,end=" ")

    def getSumatoria(self):
        suma = 0
        for numero in self.numeros:
            suma += numero
        return suma

    def crearListaMenor(self):
        numero = int(input("Ingrese un numero: "))
        lista = []
        for i in self.numeros:
            if i < numero:
                lista.append(i)
        return lista

    def mostrarFrecuencia(self):
        numeros_set = list(set(self.numeros))
        salida = []
        for n in numeros_set:
            contador = 0
            for numero in self.numeros:
                if numero == n:
                    contador += 1
            salida.append((n,contador))
        return salida




if __name__ == "__main__":
   pass

