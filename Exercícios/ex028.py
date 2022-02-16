# Jogo da Adivinhação v1.0
from random import randint
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
n1 = randint(0, 5) # faz o computador sortear um número
n2 = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if n1 == n2:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {n1} e não no {n2}!')