# Análise de dados do grupo
maior = masc = fem = 0

while True:
    print('-' * 40)
    print(f'{"CADASTRE UMA PESSOA":^40}')
    print('-' * 40)
    idade = int(input('Idade: '))
    sexo = r = ' '
    
    # Caso o usuário escreva uma resposta inválida, pergunta novamente
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        masc += 1
    if sexo == 'F' and idade < 20:
        fem += 1
    
    print('-' * 40)
    
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    
    # Para se a resposta for N
    if r == 'N':
        break

print(f'\nTotal de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {masc} homens cadastrados\nE temos {fem} mulheres com menos de 20 anos')