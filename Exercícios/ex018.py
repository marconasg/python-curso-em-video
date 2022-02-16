# Seno, Cosseno e Tangete
from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo que você deseja: '))
rad = radians(ang)
print(f'O ângulo de {ang:.0f} tem o Seno de {sin(rad):.2f}')
print(f'O ângulo de {ang:.0f} tem o Cosseno de {cos(rad):.2f}')
print(f'O ângulo de {ang:.0f} tem a Tangente de {tan(rad):.2f}')