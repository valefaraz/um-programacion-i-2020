#!/usr/bin/python3

'''Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla
todos los números impares desde 1 hasta ese número separados por comas.'''
class Numero():

    def ingreso(self):
        num = int(input("ingrese un numero\n"))
        print("los numero impares son:")
        for i in range(num):
            if i % 2 == 0:
                print(i+1)

if __name__ == "__main__":
    numero = Numero()
    numero.ingreso()
