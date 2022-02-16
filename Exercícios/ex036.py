# Aprovando Empréstimo
v = float(input('Valor da casa: R$'))
s = float(input('Salário do comprador: R$'))
a = int(input('Quantos anos de financiamento? '))
p = v / (a * 12)
print(f'Para pagar uma casa de R${v:.2f} em {a} anos, a prestação será de R${p:.2f}')
# Verifica a porcentagem da prestação em cima do salário
m = p / s * 100
if m > 30:
    print('Empréstimo negado!')
else:
    print('Empréstimo concedido!')