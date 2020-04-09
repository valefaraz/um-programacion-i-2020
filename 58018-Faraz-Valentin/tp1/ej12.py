'''Generar números aleatorios del 1 al 10 y guardar el resultado en un
diccionario. Al finalizar mostrar el resultado del diccionario ordenado
de mayor a menor.'''

import random

class Numeros():

    def __init__(self):

        self.dic = {}
        self.orden = []

    def generar(self):

        for i in range(15):
            self.dic[i] = random.randrange(1, 10)
        self.orden = sorted(self.dic.values(), reverse=True)

    def mostrar(self):

        self.generar()
        print("los numeros son :\n", list(self.dic.values()))
        print("Ordenados de manera descendente: \n", self.orden)


if __name__ == "__main__":
    N = Numeros()
    N.mostrar()