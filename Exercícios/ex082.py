# Dividindo valores em várias listas
completa = []
pares = []
impares = []

# Adiciona os valores na lista completa
while True:
    completa.append(int(input('Digite um número: ')))
    
    # Caso o usuário escreva uma resposta inválida, pergunta novamente
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    
    # Para se a resposta for N
    if r == 'N':
        break

# Adiciona os valores pares na lista pares e os ímpares na lista impares
for v in completa:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print('=' * 50)
print(f'A lista completa é {completa}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')