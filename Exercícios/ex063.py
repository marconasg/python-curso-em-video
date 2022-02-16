# Sequência de Fibonacci v1.0
c = p = 1
s = 0
print('-' * 40)
print(f'{"Sequência de Fibonacci":^40}')
print('-' * 40)
t = int(input('\nQuantos termos você quer mostrar? '))
print()
print('-' * 40)

while c <= t:
    print(f'{s} → ', end='')
    s += p # soma o resultado com o valor anterior
    p = s - p # pra pegar o valor anterior, p recebe o s menos p
    c += 1

print('FIM')
print('-' * 40)