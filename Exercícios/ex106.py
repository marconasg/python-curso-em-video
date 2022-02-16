# Sistema interativo de ajuda em Python
from time import sleep

cores = {'normal': '\033[m',
        'vermelho': '\033[97;41m',
        'verde': '\033[97;42m',
        'azul': '\033[97;44m',
        'branco': '\033[30;107m'}

def ajuda(comando):
    titulo(f'Acessando o manual do comando \'{comando}\'', 'azul')
    print(cores['branco'], end='')
    help(comando)
    print(cores['normal'], end='')
    sleep(2)

def titulo(txt, cor='normal'):
    tam = len(txt) + 4
    print(cores[cor], end='')
    print('~' * tam)
    print(f'{txt:^{tam}}')
    print('~' * tam)
    print(cores['normal'], end='')
    sleep(1)

op = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 'verde')
    op = str(input('Função ou Biblioteca > '))
    if op.upper() == 'FIM':
        break
    else:
        ajuda(op)

titulo('ATÉ LOGO!', 'vermelho')