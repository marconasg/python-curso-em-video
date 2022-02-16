# Aluguel de Carros
d = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
p = d * 60 + km * 0.15
print(f'O total a pagar é de R${p:.2f}')