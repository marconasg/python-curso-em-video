# Números Primos
vd = 0 # vezes divisível
n = int(input('Digite um número: '))
for c in range(1, n+1):
    if n % c == 0: # toda vez que o resto da divisão for 0, soma +1 na variável vd
        print(f'\033[1;33m{c}\033[m', end=' ')
        vd +=1
    else: 
        print(f'\033[31m{c}\033[m', end=' ')
print(f'\nO número {n} foi divisível {vd} vezes.\nE por isso ele', end=' ')
if vd == 2: # divisível duas vezes é primo
    print('É PRIMO!')
else: # divisível mais do que duas vezes não é primo
    print('NÃO É PRIMO!')