# Maior e Menor Valores
r = 'S'
s = t = 0

while r in 'Ss':
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    t += 1
    s += n
    if t == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

m = s / t
print(f'\nVocê digitou {t} números e a média foi {m:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')