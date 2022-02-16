# Cadastro de Jogador de Futebol v2.0
time = list()
dados = dict()
gols = list()

# Recebe os dados
while True:
    dados['nome'] = str(input('Nome do jogador: ')).strip().title()
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))

    for c in range(0, partidas):
        g = int(input((f'   Quantos gols na partida {c + 1}? ')))
        gols.append(g)

    dados['gols'] = gols[:]
    dados['total'] = sum(gols)
    time.append(dados.copy())
    gols.clear()
    
    # Caso o usuário escreva uma resposta inválida, pergunta novamente
    while True:
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if r in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    
    # Para se a resposta for N
    if r == 'N':
        break

print('=' * 60)

# Mostra os dados
print(f'{"cod":<4}{"nome":<15}{"gols":<15}{"total"}')
print('-' * 40)
for i, j in enumerate(time):
    print(f'{i:>3} {j["nome"]:<15}{str(j["gols"]):<15}{j["total"]}')

# Mostra pro usuário os dados do jogador que ele deseja ver
while True:
    print('-' * 40)
    op = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    
    if op == 999:
        break
    
    # Mostra o erro caso o número digitado esteja fora da quantidade de jogadores
    if op >= len(time):
        print(f'ERRO! Não existe jogador com o código {op}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[op]["nome"]}:')
        for i, g in enumerate(time[op]['gols']):
            print(f'    No jogo {i + 1} fez {g} gols.')

print('<< VOLTE SEMPRE >>')