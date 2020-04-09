'''Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por
pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre
del mes.'''

class Fecha():
    def pedir_fecha(self):
        while True:
                ingreso = input("Ingrese una fecha en formato dd/mm/aaaa\n")
                self.ingreso = ingreso.split("/")
                if (len(self.ingreso) == 3 and len(self.ingreso[2]) == 4):
                    break
                else:
                    print("Formato incorrecto")
    def mostrar(self,meses):
        self.meses = meses
        for x in range(12):
            if x == int(self.ingreso[1]):
                nombre_mes = self.meses[x-1]
                print("", self.ingreso[0], "de", nombre_mes, "de", self.ingreso[2] ) 


if __name__ == "__main__":
    meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", 
            "setptiembre", "octubre", "noviembre", "diciembre"]
    z = Fecha()
    z.pedir_fecha()
    z.mostrar(meses)
