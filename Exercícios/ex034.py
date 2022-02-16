# Aumentos Múltiplos
s = float(input('Qual é o salário do funcionário? R$'))
if s > 1250:
    ns = s + (s * (10/100))
else:
    ns = s + (s * (15/100))
print(f'Quem ganhava R${s:.2f} passa a ganhar R${ns:.2f} agora.')