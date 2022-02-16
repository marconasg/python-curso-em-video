# Matriz em Python
matriz = [[], [], []]

for l in range(0, (len(matriz))):
    for c in range(0, (len(matriz))):
        matriz[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))

print('=' * 50)
for l in range(0, len(matriz)):
    for c in range(0, len(matriz)):
        print(f'[{matriz[l][c]:^5}]', end='')
    print() # pula uma linha no final de cada linha da matriz