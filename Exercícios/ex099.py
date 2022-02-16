# Função que descobre o maior
from time import sleep

def maior(* num):
    print('-' * 40)
    print('Analisando os valores passados...')
    sleep(1)
    
    for v in num:
        print(v, end=' ', flush=True)
        sleep(.5)
    
    if len(num) >= 1:
        print(f'\nForam informados {len(num)} valores ao todo.')
        print(f'O maior valor informado foi {max(num)}.')
    else:
        print('Não foi informado nenhum valor.')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()