# Progressão Aritmética v1.0
print('=' * 40)
print(f'{"10 TERMOS DE UMA PA":^40}')
print('=' * 40)
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = p + 10 * r # possibilita contar 10 vezes
for c in range(p, decimo, r):
    print(f'{c} →', end=' ')
print('ACABOU')