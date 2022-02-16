# Alistamento Militar
from datetime import date
nasc = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')
if idade < 18:
    faltam = 18 - idade
    sera = atual + faltam
    print(f'Ainda faltam {faltam} anos para o alistamento.\nSeu alistamento será em {sera}.')
elif idade > 18:
    deveria = idade - 18
    foi = atual - deveria
    print(f'Você já deveria ter se alistado há {deveria} anos.\nSeu alistamento foi em {foi}.')
else:
    print(f'Você tem que se alistar IMEDIATAMENTE!')