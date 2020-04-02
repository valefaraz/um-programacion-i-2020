
class Alumno():

    def ingreso(self):
        name = input("Ingrese su nombre(Primera letra con mayuscula) \n")
        sexo = input("Ingrese su sexo.('M' para masculino y 'F' para femenino) \n")
        return (name, sexo)

    def elegir_grupo(self):

        grupo1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
        grupo2 = ['N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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
    u = Alumno()
    u.elegir_grupo()
