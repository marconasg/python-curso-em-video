# Boletim com listas compostas
alunos = []
dados = []

while True:
    dados.append(str(input('Nome: ')).strip())
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    dados.append([n1, n2]) # receba as notas numa lista
    dados.append((n1 + n2) / 2) # insere a média das notas digitadas numa lista
    alunos.append(dados[:]) # coloca todos os dados recebidos na lista alunos
    dados.clear() # apaga os itens na lista dados para o próximo loop
    
    # Caso o usuário escreva uma resposta inválida, pergunta novamente
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    
    # Para se a resposta for N
    if r == 'N':
        break

print('=' * 60)

# Mostra os nomes dos alunos e a média de suas notas
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
for pos, a in enumerate(alunos):
    print(f'{pos:<4}{a[0]:<13}{a[2]:.1f}')

print('=' * 60)

# Mostra pro usuário as notas do aluno que ele deseja ver
while True:
    opnota = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    
    if opnota == 999:
        break
    if opnota <= len(alunos) - 1: # mostra o resultado se o número digitado for menor ou igual ao tamanho da lista alunos
        print(f'Notas de {alunos[opnota][0]} são {alunos[opnota][1]}')
        print('=' * 60)

print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')