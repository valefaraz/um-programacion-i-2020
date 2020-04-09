class Texto:

    def __init__(self):

        self.texto = '''Se denomina contaminación ambiental a la presencia de componentes nocivos 
(ya sean químicos, físicos o biológicos) en el medio ambiente (entorno natural y artificial), 
que supongan un perjuicio para los seres vivos que lo habitan, incluyendo a los seres humanos. 
La contaminación ambiental está originada principalmente por causas derivadas de la actividad humana, 
como la emisión a la atmósfera de gases de efecto invernadero o la explotación desmedida 
de los recursos naturales.
Una de las principales consecuencias de la contaminación ambiental es el calentamiento global, 
también conocido como cambio climático, 
por el cual la temperatura del planeta va aumentando de manera progresiva, 
tanto la temperatura atmosférica como la de mares y océanos.
La contaminación ambiental supone un riesgo para la salud de los seres vivos que habitan
los ecosistemas contaminados, incluyendo a los seres humanos. 
Además, la tala indiscriminada, la explotación excesiva de los recursos naturales y la emisión
de contaminantes al medio ambiente (gases a la atmósfera, vertidos en medios acuáticos, 
residuos sólidos) provoca la destrucción de ecosistemas.
De esta forma, muchas especies de animales y plantas ven cómo su hábitat natural se va
reduciendo cada vez más, pudiendo llegar a provocar incluso su extinción.'''

        self.palabras = {}
        self.pal = {}

    def mas_repetidas(self):
        for i in self.texto.lower().replace("," or "." or "-" or "\n",
                                            "").split(" "):
            if i not in self.palabras.keys():
                self.palabras[i] = 1
            else:
                self.palabras[i] += 1
        x = 0
        for i in sorted(self.palabras.items(), key=lambda x: x[1],
                        reverse=True):
            if x == 20:
                break
            self.pal[i[0]] = i[1]
            x += 1
        return self.pal

def run():
    tex = Texto()
    pal = tex.mas_repetidas()
    for i in sorted(pal.items()):
        print("'{}' se repitio {} veces".format(i[0], i[1]))

if __name__ == "__main__":
    run()
