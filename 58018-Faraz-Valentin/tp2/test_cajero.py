from cajero import *
from billetes import *

import unittest


class TestCajero(unittest.TestCase):

    def setUp(self):
        self.billete100 = BilleteDe100()
        self.billete200 = BilleteDe200()
        self.billete500 = BilleteDe500()
        self.billete1000 = BilleteDe1000()
        self.cajero = Cajero()

        self.carga1 = (
                        [self.billete1000,self.billete1000,self.billete1000,
                        self.billete1000,self.billete1000,self.billete1000,
                        self.billete1000,self.billete1000,self.billete1000,
                        self.billete1000])
        
    def test_a(self):
        self.cajero.agregar_dinero(self.carga1)
        contar = self.cajero.contar_dinero()
        self.assertEqual(contar, ("0 billetes de $100, 0 billetes de $200"
                                ", 0 billetes de $500, 10 billetes de $1000"))
        extraccion1 = self.cajero.extraer_dinero(5000)
        self.assertEqual(extraccion1, ("0 billetes de $100, 0 billetes de $200"
                                    ", 0 billetes de $500, 5 billetes de $1000"))
        
        extraccion2 = self.cajero.extraer_dinero(12000)
        self.assertEqual(extraccion2, ("No hay suficiente dinero"))
        extraccion3 = self.cajero.extraer_dinero(5520)
        self.assertEqual(extraccion3, ("El monto no es multiplo de 100"))







if __name__ == "__main__":
    unittest.main()