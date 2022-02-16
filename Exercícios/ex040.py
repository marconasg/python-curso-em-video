# Clássico de Média Escolar
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print(f'Tirando {n1} e {n2}, a média do aluno é {m:.1f}')
if m >= 7:
    print('O aluno está aprovado.')
elif m < 5:
    print('O aluno está reprovado.')
else:
    print('O aluno está em recuperação.')