# Análise de dados em uma Tupla
v = (int(input('Digite um número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite mais um número: ')),
    int(input('Digite o último número: ')))
print(f'Você digitou os valores: {v}')
print(f'O valor 9 apareceu {v.count(9)} vezes')

# Verifica quantas vezes o valor 3 foi digitado
if v.count(3) >= 1:
    print(f'O valor 3 apareceu na {v.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

print(f'Os valores pares digitados foram ', end='')
# Varre os valores da tupla e escreve o valor na tela se for par
for n in v:
    if n % 2 == 0:
        print(f'{n} ', end='')