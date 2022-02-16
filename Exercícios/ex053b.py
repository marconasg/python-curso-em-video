# Detector de Palíndromo - usando for
f = str(input('Digite uma frase: ')).strip().upper().replace(' ', '')
inverso = ''
for letra in range(len(f) - 1, -1, -1):
    inverso += f[letra]
print(f'O inverso de {f} é {inverso}')
if f == inverso:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')