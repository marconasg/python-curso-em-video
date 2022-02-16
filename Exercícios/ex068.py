# Jogo do Par ou Ímpar
from random import randint
print('==' * 27)
print(f'{"VAMOS JOGAR PAR OU ÍMPAR":^54}')
print('==' * 27)
v = 0 # número de vitórias do jogador

while True:
    s = 0
    r = ''
    cpu = randint(0, 10)
    n = int(input('Digite um valor: '))
    s = cpu + n
    p = ' '
    
    # Caso o usuário escreva uma resposta inválida, pergunta novamente
    while p not in 'PI':
        p = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0] # palpite
    
    print('-' * 54)
    print(f'Você jogou {n} e o computador {cpu}. Total de {s} deu ', end='')
    
    # Verifica se a soma dos valores é par ou ímpar
    if s % 2 == 0:
        print('PAR!')
        r = 'P'
    else:
        print('ÍMPAR!')
        r = 'I'
    print('-' * 54)
    
    # Verifica se o palpite do jogar vence ou não
    if p in r:
        print('Você VENCEU!\nVamos jogar novamente...')
        v += 1
        print('==' * 27, end='\n')
    else:
        print('Você PERDEU!')
        break

print('==' * 27, end='\n')
print(f'GAME OVER! Você venceu {v} vezes.')