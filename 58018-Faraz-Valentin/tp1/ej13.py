'''Generar 10 números aleatorios, mostrarlos por pantalla y mostrar
el promedio.'''
import random


class Numeros():

    def __init__(self):
        self.a = 0

    def promedio(self):
        n = []
        for i in range(10):
            n.append(random.randrange(500))
            self.a += n[i]

        prom = self.a/10
        return(n, prom)

    def mostrar(self, n, prom):
        print("Los numeros son: ", n,"\n")
        print("El promedio de los numeros es : ", prom)


if __name__ == "__main__":
    u = Numeros()
    x, y = u.promedio()
    u.mostrar(x, y)