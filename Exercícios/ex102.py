# Função para Fatorial
def fatorial(num, show=False):
    """
    -> Calcula o Fatorial de um número.
    param num: O número a ser calculado.
    param show: (opcional) Mostrar ou não a conta.
    return: O valor do Fatorial de um número num.
    """
    
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(f' = ', end='')
        f *= c
    return f

n = int(input('Fatorial de: '))
print(fatorial(n, show=True))
print()
help(fatorial)