# Primeira e última ocorrência de uma string
f = str(input('Digite uma frase: ')).strip().lower()
f = f.replace('á', 'a')
f = f.replace('ã', 'a')
f = f.replace('à', 'a')
print(f'A letra A aparece {f.count("a")} vezes na frase.')
print(f'A primeira letra A apareceu na posição {f.find("a") + 1}.')
print(f'A última letra A apareceu na posição {f.rfind("a") + 1}.')