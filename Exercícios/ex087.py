# Mais sobre Matriz em Python
matriz = [[], [], []]
spar = stercol = 0 # soma dos pares e soma da terceira coluna

# l = linha e c = coluna
for l in range(0, (len(matriz))):
    for c in range(0, (len(matriz))):
        matriz[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))

print('=' * 50)
# Mostra os valores como se fosse uma matriz
for l in range(0, len(matriz)):
    for c in range(0, len(matriz)):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
        if c == 2:
            stercol += matriz[l][c]
    print() # pula uma linha no final de cada linha da matriz

print('=' * 50)
print(f'A soma dos valores pares é {spar}.')
print(f'A soma dos valores da terceira coluna é {stercol}.')
print(f'O maior valor da segunda linha é {max(matriz[1])}.')