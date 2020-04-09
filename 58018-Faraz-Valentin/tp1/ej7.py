'''Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por
pantalla el número de veces que aparece la letra en la frase.'''

class Frase():

    def contador(self, frase, letra):
        frase = frase.lower()
        letra = letra.lower()
        return frase.count(letra)

if __name__ == "__main__":
    u = Frase()
    frase = input("Ingese una frase\n")    
    letra = input("Ingrese una letra\n")
    print(u.contador(frase, letra))