'''Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un
nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al
usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.'''

class Curso():
    def ingreso(self):
            name = input("Ingrese su nombre(Primera letra con mayuscula) \n")
            sexo = input("Ingrese su sexo.('M' para masculino y 'F' para femenino) \n")
            return (name, sexo)
            


    def elegir_grupo(self):

        grupo1=['A','B','C','D','E','F','G','H','I','J','K','L','M']
        grupo2=['N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']

        name, sexo = self.ingreso()
        name = list(name)
        if name[0] in grupo1 and sexo == 'F':
            print("Se encuentra en el grupo A")
            return(False)
        if name[0] in grupo1 and sexo == 'M':
            print("Se encuentra en el grupo B")
            return(False)
        if name[0] in grupo2 and sexo == 'F':
            print("Se encuentra en el grupo B")
            return(False)
        if name[0] in grupo2 and sexo == 'M':
            print("Se encuentra en el grupo A")
            return(False)
        print("Error de ingreso")
               
if __name__ == "__main__":
    u = Curso()
    u.elegir_grupo()
    
