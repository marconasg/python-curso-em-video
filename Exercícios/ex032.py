# Ano Bissexto
from datetime import date
a = int(input('Que ano quer analisar? Caso queira analisar o ano atual, coloque 0: '))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(f'O ano {a} é Bissexto')
else:
    print(f'O ano {a} não é Bissexto')