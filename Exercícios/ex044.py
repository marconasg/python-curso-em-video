# Gerenciador de Pagamentos
print(f'{" Lojas Guanabara ":=^40}')
p = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque\n[ 2 ] à vista no cartão\n[ 3 ] 2x no cartão\n[ 4 ] 3x ou mais no cartão')
o = int(input('Qual é a opção? '))
if o == 1:
    f = p - (p * 10/100)
elif o == 2:
    f = p - (p * 5/100)
elif o == 3:
    f = p
    m = p / 2
    print(f'Sua compra será parcelada em 2x de R${m:.2f} sem juros.')
elif o == 4:
    x = int(input('Quantas parcelas? '))
    f = p + (p * 20/100)
    parcelas = f / x
    print(f'Sua compra será parcelada em {x}x de R${parcelas:.2f} com juros.')
else:
    f = p
    print('Opção inválida, tente novamente por favor.')
print(f'Sua compra de R${p:.2f} vai custar R${f:.2f} no final.')