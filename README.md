# Beverage Vending Machine Software

This Python project simulates the operation of a beverage vending machine with different beverage configurations. Not all vending machines have the same set of available beverages. Each beverage has its ingredients, and prices, such as a glass of water containing only water, or a creamy coffee with milk, coffee, brown sugar, and cinnamon.

## Project Overview

- The vending machine can produce a variety of beverages based on its configuration.
- The machine charges users for each beverage served. The pricing varies:
  - A glass of water costs 50 pesos.
  - Any carbonated beverage (water + flavor + carbonation) costs triple the price of water.
  - Each type of coffee has a different price.
  - Granizado beverages cost 50 pesos for each ingredient they contain.
- The machine keeps a record of the user's charges for each beverage served.

## Operations

This project includes the following operations:

1. **Preparing Beverages:** You can prepare a glass of soda and a "Creamy Coffee Granizado" to test the machine's functionality.
2. **Total Revenue Calculation:** You can calculate the total revenue earned by the vending machine.
3. **Finding the Most Expensive Beverage:** You can find the most expensive beverage that the machine can offer based on its configuration.

## Example Usage

```python
from Agua import *
from Configuracion import *
from Expendedora import *

# Create beverage objects
bebida1 = Agua('Agua', 50)
bebida2 = Granizado('Cafe, leche, azucar, canela', 200)
bebida3 = Cortado('Cafe, leche', 250)
bebida4 = Gaseosa('Agua, saborizante, gas', 150)

# Create a configuration with the beverages
bebidas = [bebida1, bebida2, bebida3, bebida4]
configuracion = Configuracion(bebidas)

# Create the vending machine
expendedora = Expendedora(configuracion)

# Prepare and print some beverages
print(expendedora.producir(bebida1))
print(expendedora.producir(bebida2))
print(expendedora.producir(bebida3))
print(expendedora.producir(bebida4))

# Calculate and print the total revenue
print(expendedora.cobrar())

# Find and print the most expensive beverage
print(expendedora.masCara(bebidas))
