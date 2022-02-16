# Contando vogais em Tupla
lista = ('aprender', 'programar', 'linguagem', 'python',
        'curso', 'gratis', 'estudar', 'praticar',
        'trabalhar', 'mercado', 'programador', 'futuro')
for p in lista: # traz as palavras dentro da lista
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p: # quebra a palavra em letras
        if letra.lower() in 'aeiou':
            print(letra, end=' ')