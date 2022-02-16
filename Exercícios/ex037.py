# Conversor de Bases Numéricas
n = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print('[ 1 ] converter para BINÁRIO\n[ 2 ] converter para OCTAL\n[ 3 ] converter para HEXADECIMAL')
o = int(input('Sua opção: '))
if o == 1:
    print(f'{n} convertido para BINÁRIO é igual a {n:b}')
elif o == 2:
    print(f'{n} convertido para OCTAL é igual a {n:o}')
elif o == 3:
    print(f'{n} convertido para HEXADECIMAL é igual a {n:X}')
else:
    print('Opção inválida, tente novamente por favor.')