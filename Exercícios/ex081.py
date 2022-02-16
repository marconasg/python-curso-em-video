# Extraindo dados de uma lista
lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    
    r = ' '
    # Caso o usuário escreva uma resposta inválida, pergunta novamente
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    
    # Para se a resposta for N
    if r == 'N':
        break

print('=' * 50)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')