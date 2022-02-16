# Tuplas com Times de Futebol
times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza',
        'Corinthians', 'Bragantino', 'Fluminense', 'América-MG',
        'Atlético-GO', 'Santos', 'Ceará SC', 'Internacional',
        'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude',
        'Grêmio', 'Bahia', 'Sport Recife', 'Chapecoense')
print('=' * 40)
print(f'Classificação do Brasileirão: {times}')
print('=' * 40)
print(f'Os 5 primeiros são: {times[:5]}')
print('=' * 40)
print(f'Os 4 últimos são: {times[-4:]}')
print('=' * 40)
print(f'Times em ordem alfabética: {sorted(times)}')
print('=' * 40)
print(f'O Chapecoense está na {times.index("Chapecoense") + 1}ª posição')