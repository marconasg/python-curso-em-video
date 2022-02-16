# Analisador de Textos
n = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {n.upper()}')
print(f'Seu nome em minúsculas é {n.lower()}')
print(f'Seu nome tem ao todo {len(n.replace(" ", ""))} letras')
# print(f'Seu nome tem ao todo {len(n) - n.count(" ")} letras') - outro método para contar sem espaços
dividir = n.split()
print(f'Seu primeiro nome é {dividir[0]} e ele tem {len(dividir[0])} letras')