# Cateto e Hipotenusa
from math import hypot
cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))
# hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2) - outra forma de calcular a hipotenusa
print(f'A hipotenusa vai medir {hypot(cateto_oposto, cateto_adjacente):.2f}')