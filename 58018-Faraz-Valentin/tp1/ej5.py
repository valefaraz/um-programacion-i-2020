'''Escribir un programa que pida al usuario un número entero y muestre por pantalla un
triángulo rectángulo como el de más abajo.
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1'''

def triangulo():
    lista=""
    altura = int(input("Ingrese la altura del triangula rectangulo\n"))

    for i in range(altura):

        if i%2 == 0:
            
            lista += str(i+1)
            print(lista[::-1])

if __name__ == "__main__":
    triangulo()

