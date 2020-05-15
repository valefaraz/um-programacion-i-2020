from billetes import *
import math

class MultiploError(Exception):
    pass

class DineroInsuficienteError(Exception):
    pass

class CombinacionDeBilletesError(Exception):
    pass

class RangoPorcentajeError(Exception):
    pass

class ExtraccionNegativaError(Exception):
    pass

class Cajero():

    def __init__(self):
        self.billetes_mil = []
        self.billetes_quinientos = []
        self.billetes_doscientos = []
        self.billetes_cien = []
        self.total = 0
        self.extraccion = []
        self.billetes_extraidos=""

    def agregar_dinero(self, lista_billetes):
        for x in lista_billetes:
            if x.denominacion == 100:
                self.billetes_cien.append(x)
            elif x.denominacion == 200:
                self.billetes_doscientos.append(x)
            elif x.denominacion == 500:
                self.billetes_quinientos.append(x)
            elif x.denominacion == 1000:
                self.billetes_mil.append(x)

    def contar_dinero(self):
        billetes =[len(self.billetes_cien), len(self.billetes_doscientos),
                    len(self.billetes_quinientos), len(self.billetes_mil)]
        self.total = (billetes[0]*100 + billetes[1]*200 + billetes[2]*500 + billetes[3]*1000)
        #print("Total disponible en el cajero:", self.total)
        billetes_contados=[]
        for x in range(len(billetes)):
            if x == 0:
                valor = 100
            if x == 1:
                valor = 200
            if x == 2:
                valor = 500
            if x == 3:
                valor = 1000
            string = (str(billetes[x]) + " billetes de $" + str(valor))
            billetes_contados.append(string)
        return(", ".join(billetes_contados))

    def extraer_dinero(self, monto):
        disponible =[len(self.billetes_cien), len(self.billetes_doscientos),
                    len(self.billetes_quinientos), len(self.billetes_mil)]
        try:
            if monto%100 != 0:
                raise MultiploError("El monto no es multiplo de 100")

            if monto > self.total:
                raise DineroInsuficienteError("No hay suficiente dinero")
            
            if int(monto) < 0:
                raise ExtraccionNegativaError("El monto a retirar no puede ser negativo")
            
            contador = 0
            while True:
                while monto >= 1000 and disponible[3] != 0:
                    disponible[3] -= 1
                    contador += 1000
                    monto -= 1000
                    self.extraccion.append("$1000")
                while monto >= 500 and disponible[2] != 0:
                    disponible[2] -= 1
                    contador += 500
                    monto -= 500
                    self.extraccion.append("$500")
                while monto >= 200 and disponible[1] != 0:
                    disponible[1] -= 1
                    contador += 200
                    monto -= 200
                    self.extraccion.append("$200")
                while monto >= 100 and disponible[0] != 0:
                    disponible[0] -= 1
                    contador += 100
                    monto -= 100
                    self.extraccion.append("$100")
                if monto == 0:
                    break
                else:
                    self.extraccion = []
                    raise CombinacionDeBilletesError("No hay billetes para esa combinacion de dinero")
        except TypeError:
            return("Error, debe ingresar un numero")
        veces100 = str(self.extraccion.count("$100"))+" billetes de $100, "
        veces200 = str(self.extraccion.count("$200"))+" billetes de $200, "
        veces500 = str(self.extraccion.count("$500"))+" billetes de $500, "
        veces1000 = str(self.extraccion.count("$1000"))+" billetes de $1000"
        if veces100 != 0:
            self.billetes_extraidos += veces100
        if veces200 != 0:
            self.billetes_extraidos += veces200
        if veces500 != 0:
            self.billetes_extraidos += veces500
        if veces1000 != 0:
            self.billetes_extraidos += veces1000
        self.total = (self.total - contador)
        return(self.billetes_extraidos)
        
    def extraer_dinero_cambio(self, monto, porc):
        disponible =[len(self.billetes_cien), len(self.billetes_doscientos),
                    len(self.billetes_quinientos), len(self.billetes_mil)]
        try:
            if porc > 100 or porc < 0:
                raise RangoPorcentajeError("El porcentaje debe ser entre 0 y 100")

            if monto > self.total:
                raise DineroInsuficienteError("No hay suficiente dinero")

            if monto%100 != 0:
                raise MultiploError("El monto no es multiplo de 100")

            porc = math.trunc(monto * porc / 100)
            sacar = porc
            sacar = str(sacar)[::-1]
            if len(sacar) <= 2:
                sacar = 100
            else:
                sacar = sacar[::-1][:2]
                sacar = (int(sacar[::-1]) + 1) * 100
            if sacar - porc >= 100 or sacar - porc <= 0:
                sacar = porc

            self.extraccion = []
            total_billetes_cambio = (len(self.billetes_cien)*100 + len(self.billetes_doscientos)*200
                                    + len(self.billetes_quinientos)*500)
            if sacar == 100 and disponible[0] == 0:
                sacar = 200 
            elif sacar >= 200 and sacar <= 400 and disponible[1] == 0 and disponible[0] == 0:
                sacar = 500
            elif sacar >= 500 and sacar <= 900:
                if disponible[1] == 0 or disponible[0] == 0:
                    sacar = 1000
            sin_cambio = monto -sacar
            while sacar <  total_billetes_cambio or (sacar - total_billetes_cambio)%100 == 0:
                while sacar >= 100 and disponible[0] != 0:
                    disponible[0] -= 1
                    self.total -= 100
                    sacar -= 100
                    #resto = sacar %200
                    #if resto == 0:
                    #    disponible[0] = 0
                    self.extraccion.append("$100")
                while sacar >= 200 and disponible[1] != 0:
                    disponible[1] -= 1
                    self.total -= 200
                    sacar -= 200
                    #resto = sacar %500
                    #if resto == 0:
                    #    disponible[1] = 0
                    self.extraccion.append("$200")
                while sacar >= 500 and disponible[2] != 0:
                    disponible[2] -= 1
                    self.total -= 500
                    sacar -= 500
                    #resto = sacar %1000
                    #if resto == 0:
                    #    disponible[2] = 0
                    self.extraccion.append("$500")
                if sacar == 0:
                    break
                else:
                    break
            while sacar >= 1000 and disponible[3] != 0:
                    disponible[3] -= 1
                    self.total -= 1000
                    sacar -= 1000
                    self.extraccion.append("$1000")
            return(self.extraer_dinero(sin_cambio))
        except TypeError:
            return("Error, el dinero y/o el porcentaje deben ser numeros")
            
if __name__ == "__main__":
    cajero = Cajero()

    billete100 = BilleteDe100()
    billete200 = BilleteDe200()
    billete500 = BilleteDe500()
    billete1000 = BilleteDe1000()

    cajero.agregar_dinero(
                            [billete1000,billete1000,billete1000,
                            billete1000,billete1000,billete1000,
                            billete1000,billete1000,billete1000,
                            billete1000,billete1000,billete1000,
                            billete1000,billete1000,billete1000,
                            
                            billete500,billete500,billete500,billete500,billete500,
                            billete500,billete500,billete500,billete500,billete500,
                            billete500,billete500,billete500,billete500,billete500])

    billetes_disponibles = cajero.contar_dinero()
    print("Billetes disponibles:", billetes_disponibles)
    print("Dinero total disponible:", cajero.total)
    extraccion = cajero.extraer_dinero(1000)
    print("Se extrajo del cajero:",extraccion)
    #print("Dinero total disponible despues de la extraccion:", cajero.total)
    
    #extraccion_con_cambio = cajero.extraer_dinero_cambio(7000,10)
    #print("Se extrajo del cajero", extraccion_con_cambio)