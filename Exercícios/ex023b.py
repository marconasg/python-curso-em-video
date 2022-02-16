# Separando dígitos de um número - em str
n = int(input('Informe um número: '))
d = n / 10000
t = str(d)
print(f'Analisando o número {n}')
print(f'Unidade: {t[5]}')
print(f'Dezena: {t[4]}')
print(f'Centena: {t[3]}')
print(f'Milhar: {t[2]}')