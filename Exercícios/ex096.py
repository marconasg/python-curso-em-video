# Função que calcula área
def area(a, b):
    total = a * b
    print(f'A área de um terreno {a}x{b} é de {total}m².')

print()
print('Controle de Terrenos')
print('-' * 20)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)