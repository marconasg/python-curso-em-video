# Tabuada v2.0
n = int(input('Digite um número para ver sua tabuada: '))
print('-' * 12)
for c in range(1, 11):
    print(f'{n} x {c:2} = {n*c}')
print('-' * 12)