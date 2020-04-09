'''Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas,
Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en
cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura>
has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y
<nota> cada una de las correspondientes notas introducidas por el usuario.'''

class Curso():
    def __init__(self, materias):
        self.materias = materias
        self.notas = {}
    
    def pedir_notas(self):
            for x in self.materias:
                print("ingrese la nota de",x)
                note = int(input(""))
                if note <= 10 and note >= 1:
                        self.notas[x] = note
    def mostrar(self):
        for n in self.materias:
            print("Su nota de",n, "es", self.notas[n])

if __name__ == "__main__":
    materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    u = Curso(materias)
    u.pedir_notas()
    u.mostrar()
