
class Expendedora:
    def __init__(self, configuracion):
        self.configuracion = configuracion
        self.recaudacion = 0

    def producir(self, bebida):
        self.recaudacion += bebida.precio
        return bebida.fabricar()

    def cobrar(self):
        return f'La recaudacion de la maquina es {self.recaudacion}$ en total'

    def masCara(self, bebidas):
        masCara = max(bebidas, key=lambda bebida: bebida.precio)
        mostrar = str(masCara.precio) + '$ ' + masCara.__class__.__name__

        return f'{mostrar} es la bebida mas cara de la maquina'