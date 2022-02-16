# Lista de Preços com Tupla
produtos = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90,
            'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(produtos)):
    # if type(pos) is str: - outro jeito de verificar, aqui testando se é str
    if pos % 2 == 0: # todo produto está no índice par
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')
print('-' * 40)