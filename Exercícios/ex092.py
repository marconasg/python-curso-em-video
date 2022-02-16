# Cadastro de Trabalhador em Python
from datetime import date
dados = {}
dados['nome'] = str(input('Nome: ')).strip().title()
dados['idade'] = date.today().year - int(input('Ano de Nascimento: '))
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

# Dicionário variável
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = 35 - (date.today().year - dados['contratação']) + dados['idade']

print('=' * 60)

# Varre cada item do dicionário para mostrar os dados
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')