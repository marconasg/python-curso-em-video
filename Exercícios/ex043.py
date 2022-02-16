# Índice de Massa Corporal
p = float(input('Qual é seu peso? (kg) '))
a = float(input('Qual é sua altura? (m) '))
imc = p / a ** 2
print(f'O IMC é de {imc:.1f}')
if imc < 18.5:
    print('Você está abaixo do peso normal.')
elif imc < 25:
    print('Parabéns, você está na faixa de peso normal.')
elif imc < 30:
    print('Você está em sobrepeso.')
elif imc < 40:
    print('Você está em obesidade!')
else:
    print('Você está em obesidade mórbida, cuidado!')