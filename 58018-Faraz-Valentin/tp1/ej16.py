'''Modificar el ejercicio 15 y hacer que los datos se muestren con una etiqueta por delante, algo
así como:
Nombre: xxxxxxxxx, monto: xxxx.xx, descripción: xxxxxxxxxx, forma de pago: xxxxxxxx'''

import os
class Ventas:

    def __init__(self, archivo):
        self.archivo = archivo

    def mostrar(self):
        for line in self.archivo.readlines():
            linea = line.split(",")
            print("Nombre: {}, monto: {},".format(linea[0], linea[1],) +
                  "descripcion: {},".format(linea[2]) +
                  " forma de pago: {}".format(linea[3]))

def run():
    path = os.path.dirname(os.path.abspath(__file__))
    nombre = input("Ingrese el nombre del archivo:\n")
    archivo = open(path + os.sep + nombre + ".txt", "r")
    x = Ventas(archivo)
    x.mostrar()
if __name__ == "__main__":
    run()
