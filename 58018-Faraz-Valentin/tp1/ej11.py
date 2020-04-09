'''Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un
curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre
por pantalla los créditos de cada asignatura en el formato <asignatura> tiene
<créditos> créditos, donde <asignatura> es cada una de las asignaturas del
curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de
créditos del curso.'''

class Curso():

    def __init__(self):

        self.dic = {'Matemáticas': 6, 'Física': 4, 'Química': 5}

    def mostrar(self):

        c = 0
        for materia in self.dic:
            print("\n"+materia+" tiene "+str(self.dic[materia])+" creditos.")
            c += self.dic[materia]
        print("\nNumero total de creditos: ", c)


if __name__ == "__main__":
    C = Curso()
    C.mostrar()