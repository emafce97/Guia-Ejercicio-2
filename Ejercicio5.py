class Ejercicio5:

    def ingresar_cadenas(self):
        lista_cadenas = []
        while not len(lista_cadenas) == 3:
            cadena = input("Ingrese una cadena de texto: ")
            cadena_sin_espacios = cadena.replace(" ", "")
            lista_cadenas.append(cadena_sin_espacios)
        return lista_cadenas

    def get_frecuencia(self, cadenas):
        mapa = {}
        for cadena in cadenas:
            for letra in cadena:
                if letra not in mapa.keys():
                    mapa[letra] = 1
                else:
                    cant = mapa[letra]
                    mapa[letra] = cant + 1
        return mapa

    def imprimir_mapa(self, mapa):
        for i in mapa.keys():
            if not i == " ":
                print(f"{i}-{mapa[i]}")


if __name__ == "__main__":
    e5 = Ejercicio5()
    print(e5.get_frecuencia(e5.ingresar_cadenas()))
