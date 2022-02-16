# Módulo para os exercícios da Aula 22
def aumentar(n = 0, porc = 0):
    res = n + (n * porc / 100)
    return res

def diminuir(n = 0, porc = 0):
    res = n - (n * porc / 100)
    return res

def dobro(n = 0):
    res = n * 2
    return res

def metade(n = 0):
    res = n / 2
    return res

def moeda(n = 0, moeda = 'R$'):
    return f'{moeda}{n:>.2f}'.replace('.', ',')