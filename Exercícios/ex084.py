# Lista composta e análise de dados
todos = []
dados = []
mai = men = 0

while True:
    dados.append(str(input('Nome: ')).strip())
    dados.append(float(input('Peso: ')))
    
    # Se a lista de todos ainda não tiver preenchida
    if len(todos) == 0:
        mai = men = dados[1] # pega o peso que tá no índice [1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    
    todos.append(dados[:])
    dados.clear()
    
    # Caso o usuário escreva uma resposta inválida, pergunta novamente
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    
    # Para se a resposta for N
    if r == 'N':
        break

print('=' * 50)
print(f'Ao todo, você cadastrou {len(todos)} pessoas.')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in todos:
    if p[1] == mai:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi de {men}Kg. Peso de ', end='')
for p in todos:
    if p[1] == men:
        print(f'[{p[0]}]', end=' ')