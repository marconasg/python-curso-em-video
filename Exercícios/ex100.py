# Funções para sortear e somar
from time import sleep
from random import randint

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    
    for c in range(0, 5):
        lista.append(randint(1, 10))
    
    for v in lista:
        print(v, end=' ', flush=True)
        sleep(.5)
    print('PRONTO!')

def somapar(valores):
    totpar = 0
    
    for v in valores:
        if v % 2 == 0:
            totpar += v
    
    print(f'Somando os valores pares de {numeros}, temos {totpar}')

numeros = []
sorteia(numeros)
somapar(numeros)