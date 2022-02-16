# Sorteando um item na lista
from random import choice
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
print(f'O aluno escolhido foi {choice([a1, a2, a3, a4])}.')