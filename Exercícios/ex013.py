# Reajuste Salarial
salario = float(input('Qual é o salário do funcionário? R$'))
novo = salario + (salario * 0.15)
# novo = salario + (salario * 15 / 100) - outro método pra tirar a porcentagem
print(f'Um funcionário que ganhava R${salario:.2f}, com 15% de aumento, passa a receber R${novo:.2f}')