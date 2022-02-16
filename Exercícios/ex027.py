# Primeiro e último nome de uma pessoa
n = str(input('Digite seu nome completo: ')).strip().split()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {n[0]}')
print(f'Seu último nome é {n[-1]}')