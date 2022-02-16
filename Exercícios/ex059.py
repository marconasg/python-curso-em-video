# Criando um Menu de Opções
from time import sleep
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))

# Menu
print('\n[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa\n')
o = int(input('>>>>> Qual é a sua opção? '))

# Condições para cada opção escolhida
while o != 5:
    if o <= 5:
        if o == 1:
            s = v1 + v2
            print(f'A soma entre {v1} + {v2} é {s}')
        elif o == 2:
            m = v1 * v2
            print(f'O resultado de {v1} x {v2} é {m}')
        elif o == 3:
            maior = v1
            if v2 > v1:
                maior = v2
            print(f'Entre {v1} e {v2} o maior valor é {maior}')
        elif o == 4:
            print('Informe os números novamente:')
            v1 = int(input('Primeiro valor: '))
            v2 = int(input('Segundo valor: '))
    else:
        print('Opção inválida. Tente novamente.')
    print('-=-' * 10)
    sleep(1.5)
    print('\n[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa\n')
    o = int(input('>>>>> Qual é a sua opção? '))

# Fim do programa
print('\nFinalizando...')
print('-=-' * 10)
sleep(1.5)
print('Fim do programa! Volte sempre!')