# Analisador Completo
somaidade = 0 # soma de todas as idades
idadevelho = 0 # idade do homem mais velho
idadenome = '' # nome do homem mais velho
contmulher = 0 # quantidade de mulheres com menos de 20 anos

for c in range(1, 5):
    print(f'----- {c}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    somaidade += idade
    if sexo == 'M':
        if idade > idadevelho:
            idadevelho = idade
            idadenome = nome
    else:
        if idade < 20:
            contmulher += 1

media = somaidade / 4
print(f'\nA média de idade do grupo é de {media:.1f} anos.')
print(f'O homem mais velho tem {idadevelho} anos e se chama {idadenome}.')
print(f'Ao todo são {contmulher} mulheres com menos de 20 anos.')