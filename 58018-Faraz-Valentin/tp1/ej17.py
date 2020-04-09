'''Crear un programa que lea el archivo del ejercicio 15 y lo convierta a formato JSON con el
siguiente formato:
{"nombre":"xxxxxxxxx",''monto":xxxx.xx, "descripcion":"xxxxxxxx", "formapago":"xxxx"}
Debemos mostrarlo por pantalla y crear un archivo llamado ARCHIVO_ORIGINAL.json
donde guardaremos los objetos JSON convertidos
El nombre ARCHIVO_ORIGINAL debe ser el que se definió para el archivo de datos.'''

import os
import json

class Ventas:

    def __init__(self, archivo, archivo1):
        self.archivo = archivo
        self.archivo1 = archivo1

    def diccionario(self, linea):
        dic = {
               "nombre": linea[0],
               "monto": round(float(linea[1]), 2),
               "descripcion": linea[2],
               "formapago": linea[3]
              }
        return dic

    def convertir(self):
        self.archivo1.write("[\n")
        c = 0
        for line in self.archivo.readlines():
            if c != 0:
                self.archivo1.write(",\n")
            linea = line.replace("\n", "").split(", ")
            dic = self.diccionario(linea)
            json.dump(dic, self.archivo1, indent=4)
            c += 1
        self.archivo1.write("\n]\n")


def run():
    path = os.path.dirname(os.path.abspath(__file__))
    nombre = input("Ingrese el nombre del archivo: ")
    archivo = open(path + "/" + nombre + ".txt", "r")
    archivo1 = open(path + "/" + nombre + ".json", "a")
    venta = Ventas(archivo, archivo1)
    venta.convertir()


if __name__ == "__main__":
    run()