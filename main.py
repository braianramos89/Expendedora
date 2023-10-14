
from Agua import *
from Configuracion import *
from Expendedora import *

bebida1 = Agua('Agua',50)
bebida2 = Granizado('Cafe, leche, azucar, canela',200)
bebida3 = Cortado('Cafe, leche',250)
bebida4 = Gaseosa('Agua, saborizante, gas',150)

bebidas = [bebida1,bebida2,bebida3,bebida4]

configuracion = Configuracion(bebidas)

expendedora = Expendedora(configuracion)

print(expendedora.producir(bebida1))
print(expendedora.producir(bebida2))
print(expendedora.producir(bebida3))
print(expendedora.producir(bebida4))

print(expendedora.cobrar())

print(expendedora.masCara(bebidas))