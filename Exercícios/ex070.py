# Estatísticas em produtos
print('-' * 50)
print(f'{"LOJA SUPER BARATÃO":^50}')
print('-' * 50)
t = m1000 = b = i = 0
bs = '' # barato em str

while True:
    n = str(input('Nome do produto: ')).strip().title()
    p = float(input('Preço: R$'))
    r = ' '
    t += p
    i += 1 # pega o total de inputs
    
    if p > 1000:
        m1000 += 1
    
    # No primeiro input as variáveis vão receber o que foi digitado pela primeira vez
    if i == 1 or p < b:
        b = p
        bs = n
    
    print()
    # Caso o usuário escreva uma resposta inválida, pergunta novamente
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        print()
    
    # Para se a resposta for N
    if r == 'N':
        break

print(f'{" FIM DO PROGRAMA ":-^50}')
print(f'\nO total de compra foi R${t:.2f}')
print(f'Temos {m1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {bs} que custa R${b:.2f}')