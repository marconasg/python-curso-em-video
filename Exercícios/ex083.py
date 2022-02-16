# Validando expressões matemáticas
expr = str(input('Digite a expressão: ')).strip()
pilha = []

# Varre cada símbolo na expressão digitada
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')