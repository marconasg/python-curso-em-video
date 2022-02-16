# Progressão Aritmética v2.0
print('=' * 40)
print(f'{"10 TERMOS DE UMA PA":^40}')
print('=' * 40)
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 1

while c <= 10:
    print(f'{p} →', end=' ')
    p += r
    c += 1

print('FIM')