class Billete():

    def __init__(self):
        self.denominacion = None
        self.moneda = "Pesos"
        self.representacion = None

class BilleteDe100(Billete):

    def __init__(self):
        Billete.__init__(self)
        self.denominacion = 100
        self.representacion = '$100'

class BilleteDe200(Billete):

    def __init__(self):
        Billete.__init__(self)
        self.denominacion = 200
        self.representacion = '$200'

class BilleteDe500(Billete):

    def __init__(self):
        Billete.__init__(self)
        self.denominacion = 500
        self.representacion = '$500'

class BilleteDe1000(Billete):

    def __init__(self):
        Billete.__init__(self) 
        self.denominacion = 1000
        self.representacion = '$1000'