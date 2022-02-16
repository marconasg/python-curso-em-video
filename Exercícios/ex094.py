# Unindo dicionários e listas
pessoas = []
media = []
dados = {}

# Recebe os dados
while True:
    dados['nome'] = str(input('Nome: ')).strip().title()
    
    # Caso o usuário escreva uma resposta inválida, pergunta novamente
    while True:
        dados['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    
    dados['idade'] = int(input('Idade: '))
    media.append(dados['idade'])
    pessoas.append(dados.copy())
    
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
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
print(f'B) A média de idade é de {sum(media) / len(pessoas):.1f} anos.')

print('C) As mulheres cadastradas foram ', end='')
for p in pessoas:
    # Escreve o nome da pessoa se for do sexo feminino
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')

print('\nD) Lista das pessoas que estão acima da média:')
for p in pessoas:
    # Escreve os dados da pessoa se a idade dela for maior que a média
    if p['idade'] > sum(media) / len(pessoas):
        print(f'    nome = {p["nome"]}; sexo = {p["sexo"]}; idade = {p["idade"]};')

print('<< ENCERRADO >>')