# Módulo para o Exercício 115
def linha(tam = 42):
    return '-' * tam

def leiaInt(txt):
    while True:
        try:
            n = int(input(txt))
        except:
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
        else:
            return n

def topo(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    topo('MENU PRINCIPAL')
    for pos, item in enumerate(lista):
        print(f'\033[33m{pos + 1}\033[m - \033[34m{item}\033[m')
    print(linha())
    op = leiaInt('\033[32mSua opção: \033[m')
    return op