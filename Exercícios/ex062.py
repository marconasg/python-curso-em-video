# Progressão Aritmética v3.0
print('=' * 40)
print(f'{"GERADOR DE PA":^40}')
print('=' * 40)
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
total = 0
t = 10

while t != 0:
    c = 1
    while c <= t:
        print(f'{p} →', end=' ')
        p += r
        c += 1
        total += 1
    print('PAUSA')
    t = int(input('Quantos termos você quer mostrar a mais? '))

print(f'Progressão finalizada com {total} termos mostrados.')