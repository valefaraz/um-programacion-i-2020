'''Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo
guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene
<edad> años, vive en <dirección> y su número de teléfono es
<teléfono>.''' 
class DatosPersonales():

    def __init__(self,info):
        self.datos = {}
        self.info = info
    def pedir_datos(self):
        print("Por favor ingrese los siguientes datos")
        for x in self.info:
            dato = input(str(x)+":")
            self.datos[x] = dato
            print(self.datos[x])
    def mostrar(self):
            print(str(self.datos["nombre"]) + " tiene " 
                + str(self.datos["edad"]) + " años, vive en " 
                + str(self.datos["direccion"]) + " y su numero de telefono es " 
                + str(self.datos["telefono"]))
    
if __name__ == "__main__":
    lista = ["nombre", "edad", "direccion", "telefono"]
    u = DatosPersonales(lista)
    u.pedir_datos()
    u.mostrar()
