# Funções para votação
def voto(ano):
    from datetime import date
    
    idade = date.today().year - ano
    print(f'Com {idade} anos: ', end='')
    
    if idade < 16:
        return 'NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return 'VOTO OPCIONAL.'
    else:
        return 'VOTO OBRIGATÓRIO.'

print('-' * 30)
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))