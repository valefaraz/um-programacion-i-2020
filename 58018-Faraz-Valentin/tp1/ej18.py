import os
import json

class Error(Exception):
    pass


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
            try:
                linea = line.replace("\n", "").split(", ")
                if "" in linea:
                    raise Error
                if c != 0:
                    self.archivo1.write(",\n")
                dic = self.diccionario(linea)
                json.dump(dic, self.archivo1, indent=4)
                c += 1
            except Error:
                print("\nOcurrió un problema con la fuente de los datos\n\n")
                continue
        self.archivo1.write("\n]\n")


def main():
    path = os.path.dirname(os.path.abspath(__file__))
    nombre = input("Ingrese el nombre del archivo: ")
    archivo = open(path + "/" + nombre + ".txt", "r")
    archivo1 = open(path + "/" + nombre + ".json", "a")
    venta = Ventas(archivo, archivo1)
    venta.convertir()
    
if __name__ == "__main__":
    main()