'''Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un
número primo o no.'''
import math


class Numero():

    def primo(self,numero):
        if (numero<=1):
            return False
        for i in range(2, math.ceil(math.sqrt(numero))+1):
            if(numero%i==0 and i!=numero):
                return False
        return True

    def mostrar(self):
        while True:
                try:
                    numero = int(input("inserta un numero para ver si es primo (0 para salir)\n"))
                    if numero == 0:
                        break
                    if self.primo(numero):
                        print ("\nEl numero",numero, "SI es primo")
                    else:
                        print ("\nEl numero",numero, "NO es primo")
                except:
                    print ("\nEl numero tiene que ser entero")

if __name__ == "__main__":
    num = Numero()
    num.mostrar()