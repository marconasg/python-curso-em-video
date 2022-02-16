# Jogo da Adivinhação v2.0
from random import randint
from time import sleep
print('-=-' * 15)
print('Olá, sou seu computador...')
print('-=-' * 15)
sleep(1)
cpu = randint(0, 10) # faz o computador sortear um número
print('Acabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi?\n')
p = int(input('Qual é seu palpite? '))
tentativas = 1
while p != cpu: # a condição do while dá pra fazer também com uma variável True ou False
    if p > cpu:
        print('Menos... Tente novamente.')
    else:
        print('Mais... Tente novamente.')
    p = int(input('Qual é seu palpite? '))
    tentativas += 1
print(f'Acertou com {tentativas} tentativas. Parabéns!')