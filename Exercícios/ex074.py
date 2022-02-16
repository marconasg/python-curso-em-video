# Maior e menor valores em Tupla
from random import randint
v = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ', end='')
for c in v:
    print(f'{c} ', end='')
print(f'\nO maior valor sorteado foi {max(v)}\nO menor valor sorteado foi {min(v)}')