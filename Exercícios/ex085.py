# Listas com pares e ímpares
valores = [[], []]

for c in range(0, 7):
    n = int(input(f'Digite o {c + 1}º valor: '))
    if n % 2 == 0:
        valores[0].append(n) # adiciona na lista par
    else:
        valores[1].append(n) # adiciona na lista ímpar

print('=' * 50)
valores[0].sort()
valores[1].sort()
print(f'Os valores pares digitados foram: {valores[0]}')
print(f'Os valores ímpares digitados foram: {valores[1]}')