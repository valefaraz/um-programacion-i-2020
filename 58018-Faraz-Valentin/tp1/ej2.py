#!/usr/bin/python3
import os


class Pizza():

    def __init__(self, opcion):
        os.system("clear")
        while True:
            try:
                opcion = int(input("1-)Pizza vegetariana\n"
                                    "2-)Pizza no vegetariana \n"))
                if opcion == 1:
                    print("---Usted selecciono vegetariana---")
                    self.opcion = "vegetariana"
                    break
                elif self.opcion == 2:
                    print("---Usted selecciono no vegetariana---")
                    self.opcion= "no vegetariana"
                    break
                else:
                    print("opcion incorrecta")
            except:
                print ("POR FAVOR INGRESE UN NUMERO")
    def ingredientes(self):
        #pizza=self.ingreso()
        bucle=True

        if self.opcion=="vegetariana":
            while bucle:
                ingrediente = int(input("Ingredientes vegetarianos:\n"
                                        "1-)Pimiento\n2-)Tofu\n"))
                if ingrediente == 1:
                    bucle = False
                    return("Pimieto")
                elif ingrediente == 2:
                    bucle = False
                    return("Tofu")
                else:
                    print("opcion incorrecta")
        if self.opcion=="no vegetariana":
            while bucle:
                ingrediente = int(input("Ingredientes no vegetarianos:"
                                        "\n1-)Peperoni\n2-)Jamón\n3-)Salmón\n"))
                if ingrediente == 1:
                    bucle = False
                    return("Peperoni")
                elif ingrediente == 2:
                    bucle = False
                    return("Jamon")
                elif ingrediente == 3:
                    bucle = False
                    return("Salmón")
                else:
                    print("opcion incorrecta")

    def mostrar_pantalla(self):
        print("SU PIZZA",self.opcion,"CONTIENE MOZZARELLA,TOMATE Y "
              ,self.ingredientes())

if __name__ == "__main__":
    u=Pizza(0)
    u.mostrar_pantalla()