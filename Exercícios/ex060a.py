# Cálculo do Fatorial - com while
n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')

while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='') # substitui o x por = quando chegar em 1
    f *= c
    c -= 1

print(f)