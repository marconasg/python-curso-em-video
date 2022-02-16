# Jogo de Dados em Python
from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'jogador1': randint(1, 6),
            'jogador2': randint(1, 6),
            'jogador3': randint(1, 6),
            'jogador4': randint(1, 6)}
ranking = []
print('Valores sorteados:')
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print()
print('=' * 50)
print()
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('== RANKING DOS JOGADORES ==')
for pos, j in enumerate(ranking):
    print(f'   {pos + 1}º lugar: {j[0]} com {j[1]}.')
    sleep(1)