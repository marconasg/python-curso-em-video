# Custo da Viagem
d = int(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {d}Km.')
if d <= 200:
    c = d * 0.50
    print(f'E o preço da sua passagem será de R${c:.2f}')
else:
    l = d * 0.45
    print(f'E o preço da sua passagem será de R${l:.2f}')