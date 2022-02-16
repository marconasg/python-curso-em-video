# Validação de Dados
sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0] # o [0] é pra pegar somente a primeira letra
# while sexo not in 'MmFf': outro modo de testar
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')