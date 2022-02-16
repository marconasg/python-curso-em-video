# Módulo para os exercícios da Aula 22
def aumentar(n, porc):
    res = n + (n * porc / 100)
    return res

def diminuir(n, porc):
    res = n - (n * porc / 100)
    return res

def dobro(n):
    res = n * 2
    return res

def metade(n):
    res = n / 2
    return res