# Maior e menor sequência
maior = 0
menor = 0
for c in range(1, 6):
    p = float(input(f'Peso da {c}ª pessoa: '))
    if c == 1: # como é a primeira entrada, tanto o maior quanto o menor podem receber o primeiro peso
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        elif p < menor:
            menor = p
print(f'\nO maior peso lido foi de {maior}kg.\nO menor peso lido foi de {menor}kg.')