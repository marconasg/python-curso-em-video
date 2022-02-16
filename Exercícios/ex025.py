# Procurando uma string dentro de outra
n = str(input('Qual é seu nome completo? ')).strip().lower().split()
print(('Seu nome tem Silva? '), ('silva' in n))