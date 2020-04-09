'''Crear un programa que lea un archivo de texto que va a contener datos de una venta y
mostrarlo por pantalla.
El formato será:
Nombre y apellido, monto de la venta, descripción, forma de pago (contado o tarjeta)
El archivo contendrá una línea por cada venta, y podrá contener múltiples ventas.'''

import os

class Ventas:
    def __init__(self, archivo):
        self.archivo = archivo

    def mostrar(self):
        for i in self.archivo.readlines():
            print(i)


def run():
    path = os.path.dirname(os.path.abspath(__file__))
    name = input("Ingrese el nombre del archivo:\n")
    archivo = open(path + os.sep + name + ".txt", "r")
    venta = Ventas(archivo)
    venta.mostrar()
    archivo.close()

if __name__ == "__main__":
    run()