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
        self.carga2 = (
                        [self.billete1000,self.billete1000,self.billete1000,
                        self.billete1000,self.billete1000,self.billete1000,
                        self.billete1000,self.billete1000,self.billete1000,
                        self.billete1000,
                        self.billete500,self.billete500,self.billete500,
                        self.billete500,self.billete500,self.billete500,
                        self.billete500,self.billete500,self.billete500,
                        self.billete500,self.billete500,self.billete500,
                        self.billete500,self.billete500,self.billete500,
                        self.billete500,self.billete500,self.billete500,
                        self.billete500,self.billete500])
        self.carga3 = (
                        [self.billete1000,self.billete1000,self.billete1000,
                        self.billete1000,self.billete1000,self.billete1000,
                        self.billete1000,self.billete1000,self.billete1000,
                        self.billete1000,
                        self.billete500,self.billete500,self.billete500,
                        self.billete500,self.billete500,self.billete500,
                        self.billete500,self.billete500,self.billete500,
                        self.billete500,self.billete500,self.billete500,
                        self.billete500,self.billete500,self.billete500,
                        self.billete500,self.billete500,self.billete500,
                        self.billete500,self.billete500,
                        self.billete200,self.billete200,self.billete200,
                        self.billete200,self.billete200,self.billete200,
                        self.billete200,self.billete200,self.billete200,
                        self.billete200,self.billete200,self.billete200,
                        self.billete200,self.billete200,self.billete200])
        
    def test_1(self):
        self.cajero.agregar_dinero(self.carga1)
        contar = self.cajero.contar_dinero()
        self.assertEqual(contar, ("0 billetes de $100, 0 billetes de $200"
                                ", 0 billetes de $500, 10 billetes de $1000"))
        extraccion = self.cajero.extraer_dinero(5000)
        self.assertEqual(extraccion, ("0 billetes de $100, 0 billetes de $200"
                                    ", 0 billetes de $500, 5 billetes de $1000"))
        
        extraccion1 = self.cajero.extraer_dinero(12000)
        self.assertEqual(extraccion1, ("No hay suficiente dinero"))
        extraccion2 = self.cajero.extraer_dinero(5520)
        self.assertEqual(extraccion2, ("El monto no es multiplo de 100"))
    
    def test_2_a_b(self):
        self.cajero.agregar_dinero(self.carga2)
        contar = self.cajero.contar_dinero()
        self.assertEqual(contar, ("0 billetes de $100, 0 billetes de $200"
                                ", 20 billetes de $500, 10 billetes de $1000"))
        extraccion = self.cajero.extraer_dinero(5000)
        self.assertEqual(extraccion, ("0 billetes de $100, 0 billetes de $200"
                                    ", 0 billetes de $500, 5 billetes de $1000"))
        
    def test_2_c(self):
        self.cajero.agregar_dinero(self.carga2)
        contar = self.cajero.contar_dinero()
        self.assertEqual(contar, ("0 billetes de $100, 0 billetes de $200"
                                ", 20 billetes de $500, 10 billetes de $1000"))
        extraccion = self.cajero.extraer_dinero(12000)
        self.assertEqual(extraccion, ("0 billetes de $100, 0 billetes de $200"
                                    ", 4 billetes de $500, 10 billetes de $1000"))

    def test_2_d_e(self):
        self.cajero.agregar_dinero(self.carga2)
        contar = self.cajero.contar_dinero()
        self.assertEqual(contar, ("0 billetes de $100, 0 billetes de $200"
                                ", 20 billetes de $500, 10 billetes de $1000"))
        extraccion1 = self.cajero.extraer_dinero(12100)
        self.assertEqual(extraccion1, ("Error. No hay una combinación de billetes que nos permita extraer ese monto."))
        extraccion_cambio = self.cajero.extraer_dinero_cambio(7000,10)
        self.assertEqual(extraccion_cambio,("0 billetes de $100, 0 billetes de $200"
                                    ", 2 billetes de $500, 6 billetes de $1000"))
    
    def test_3_a_b(self):
        self.cajero.agregar_dinero(self.carga3)
        contar = self.cajero.contar_dinero()
        self.assertEqual(contar, ("0 billetes de $100, 15 billetes de $200"
                                ", 20 billetes de $500, 10 billetes de $1000"))
        extraccion1 = self.cajero.extraer_dinero(5000)
        self.assertEqual(extraccion1, ("0 billetes de $100, 0 billetes de $200"
                                    ", 0 billetes de $500, 5 billetes de $1000"))
    def test_3_c(self):
        self.cajero.agregar_dinero(self.carga3)
        contar = self.cajero.contar_dinero()
        self.assertEqual(contar, ("0 billetes de $100, 15 billetes de $200"
                                ", 20 billetes de $500, 10 billetes de $1000"))
        extraccion1 = self.cajero.extraer_dinero(12000)
        self.assertEqual(extraccion1, ("0 billetes de $100, 0 billetes de $200"
                                    ", 4 billetes de $500, 10 billetes de $1000"))
    def test_3_d(self):
        self.cajero.agregar_dinero(self.carga3)
        contar = self.cajero.contar_dinero()
        self.assertEqual(contar, ("0 billetes de $100, 15 billetes de $200"
                                ", 20 billetes de $500, 10 billetes de $1000"))
        extraccion2 = self.cajero.extraer_dinero(12100)
        self.assertEqual(extraccion2, ("Error. No hay una combinación de billetes que nos permita extraer ese monto."))
    
    def test_3_e(self):
        self.cajero.agregar_dinero(self.carga3)
        self.cajero.contar_dinero()
        extraccion1 = self.cajero.extraer_dinero_cambio(7000, 10)
        self.assertEqual(extraccion1, ("0 billetes de $100, 5 billetes de $200"
                                ", 0 billetes de $500, 6 billetes de $1000"))

if __name__ == "__main__":
    unittest.main()