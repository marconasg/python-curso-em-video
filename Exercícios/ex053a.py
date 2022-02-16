# Detector de Palíndromo
f = str(input('Digite uma frase: ')).strip().upper()
f = f.replace(' ', '')
fr = f[::-1] # frase invertida
print(f'O inverso de {f} é {fr}')
if f == fr:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')