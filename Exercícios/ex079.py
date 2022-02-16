# Valores únicos em uma lista
valores = []

while True:
    n = int(input('Digite um valor: '))
    if n in valores:
        print('Valor duplicado! Não vou adicionar...')
    else:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    
    r = ' '
    # Caso o usuário escreva uma resposta inválida, pergunta novamente
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    
    # Para se a resposta for N
    if r == 'N':
        break

print('=' * 50)
valores.sort()
print(f'Você digitou os valores {valores}')