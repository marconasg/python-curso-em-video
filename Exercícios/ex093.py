# Cadastro de Jogador de Futebol 1.0
dados = {}
gols = []

dados['nome'] = str(input('Nome do jogador: ')).strip().title()
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))

for c in range(0, partidas):
    g = int(input((f'   Quantos gols na partida {c + 1}? ')))
    gols.append(g)

dados['gols'] = gols
dados['total'] = sum(gols)
print('=' * 60)
print(dados)
print('=' * 60)

for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')

print('=' * 60)

print(f'O jogador {dados["nome"]} jogou {len(dados["gols"])} partidas.')
for pos, g in enumerate(dados['gols']):
    print(f'    => Na partida {pos + 1}, fez {g} gols.')
print(f'Foi um total de {dados["total"]} gols.')