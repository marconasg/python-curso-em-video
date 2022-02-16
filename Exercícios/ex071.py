# Simulador de Caixa Eletrônico
print('=' * 40)
print(f'{"BANCO CEV":^40}')
print('=' * 40)
c50 = c20 = c10 = c1 = 0
t = 0
v = int(input('Que valor você quer sacar? R$'))

while t != v:
    if v - t >= 50:
        c50 += 1
        t += 50
    elif v - t >= 20:
        c20 += 1
        t += 20
    elif v - t >= 10:
        c10 += 1
        t += 10
    else:
        c1 += 1
        t += 1

if c50 >= 1:
    print(f'Total de {c50} cédulas de R$50')
if c20 >= 1:
    print(f'Total de {c20} cédulas de R$20')
if c10 >= 1:
    print(f'Total de {c10} cédulas de R$10')
if c1 >= 1:
    print(f'Total de {c1} cédulas de R$1')

print('=' * 40)
print('Volte sempre ao Banco CEV! Tenha um bom dia!')