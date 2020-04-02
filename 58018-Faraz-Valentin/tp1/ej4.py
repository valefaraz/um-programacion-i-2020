'''Escribir un programa que pida al usuario un número entero y muestre por pantalla un
triángulo rectángulo como el de más abajo, de altura el número introducido.
*
**
***
****
*****'''

def triangulo():
    while True:
        try:

            altura = int(input("Ingrese la altura del triangula rectangulo\n"))
            if altura==0:
                break
            for i in range(altura): 
                print("*"* (i+1))
        except:
            print("Ingrese un NUMERO")
        

if __name__ == "__main__":
    triangulo()
