class Bebida:
    def __init__(self,ingrediente,precio):
        self._ingredientes = ingrediente
        self._precio = precio

    def fabricar(self):
        pass
class Agua(Bebida):
    def __init__(self,ingrediente,precio):
        super().__init__(ingrediente,precio)
        self.ingredientes = 'Agua'
        self.precio = 50

    def fabricar(self):
        return f'Fabricando agua  con {self.ingredientes} y precio {self.precio}'

class Granizado(Bebida):
    def __init__(self,ingrediente,precio):
        super().__init__(ingrediente,precio)
        self.ingredientes = 'Cafe, leche, azucar, canela'
        self.precio = 200

    def fabricar(self):
        return f'Fabricando granizado  con {self.ingredientes} y precio {self.precio}'

class Cortado(Bebida):
    def __init__(self,ingrediente,precio):
        super().__init__(ingrediente,precio)
        self.ingredientes = 'Cafe, leche'
        self.precio = 250

    def fabricar(self):
        return f'Fabricando cortado  con {self.ingredientes} y precio {self.precio}'

class Gaseosa(Bebida):
    def __init__(self,ingrediente,precio):
        super().__init__(ingrediente,precio)
        self.ingredientes = 'Agua, saborizante, gas'
        self.precio = 150

    def fabricar(self):
        return f'Fabricando gaseosa  con {self.ingredientes} y precio {self.precio}'