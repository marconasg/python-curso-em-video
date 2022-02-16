# Pedra, Papel e Tesoura
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
print('Suas opções:')
print('[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA\n')
j = int(input('Qual é sua jogada? '))
c = randint(0,2)

# Mostra Jokenpô com timer
sleep(0.5)
print('\nJO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ!\n')

# Menu das jogadas
print('-=-' * 10)
print(f'Computador jogou {itens[c]}')
print(f'Jogador jogou {itens[j]}')
print('-=-' * 10)

# Testes de quem ganha ou empate 
if j == 0 and c == 2:
    print('JOGADOR VENCE\n')
elif j == 2 and c == 1:
    print('JOGADOR VENCE\n')
elif j == 1 and c == 0:
    print('JOGADOR VENCE\n')
elif j == c:
    print('EMPATE\n')
else:
    print('COMPUTADOR VENCE\n')