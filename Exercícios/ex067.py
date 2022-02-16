# Tabuada v3.0
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 40)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
        c += 1
    print('-' * 40)
print('Programa tabuada encerrado. Volte sempre!')