# Palpites para a Mega Sena
from random import randint
from time import sleep
lista = []
jogos = []
print('-' * 40)
print(f'{"JOGA NA MEGA SENA":^40}')
print('-' * 40)
qtd = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1

while tot <= qtd:
    cont = 0
    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

print('-' * 9, f' SORTEANDO {qtd} JOGOS ', '-' * 9)
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print(f'{" < BOA SORTE! > ":-^40}')