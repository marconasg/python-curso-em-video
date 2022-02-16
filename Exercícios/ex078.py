# Maior e menor valores na Lista
valores = list()

# Adiciona diversos valores na lista inseridos pelo usuário
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {c}: ')))

print('=' * 55)
print(f'Você digitou os valores {valores}')

# Verifica o valor em cada posição pra definir o maior ou menor
for pos, v in enumerate(valores):
    if pos == 0: # no índice 0, o maior e menor valor recebem v
        maior = menor = v
        maiorpos = menorpos = [pos]
    else: # depois do índice 0 verifica:
        if v > maior: # se o valor em v é maior que o valor em maior
            maior = v
            maiorpos = [pos]
        elif v == maior: # se tiver dois ou mais valores maiores iguais em posições diferentes, adiciona mais um item na lista
            maiorpos.append(pos)
        if v < menor: # se o valor em v é menor que o valor em menor
            menor = v
            menorpos = [pos]
        elif v == menor: # se tiver dois ou mais valores menores iguais em posições diferentes, adiciona mais um item na lista
            menorpos.append(pos)

print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i in maiorpos: # varre e mostra as posições
    print(f'{i}... ', end='')

print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for i in menorpos: # varre e mostra as posições
    print(f'{i}... ', end='')