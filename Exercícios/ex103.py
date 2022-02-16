# Ficha do jogador
def ficha(n = '<desconhecido>', g = 0):
    """
    Mostra o nome do jogador e quantos gols ele fez.

    Args:
        n (str): nome do jogador
        g (int): quantidade de gols
    """
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')

print('-' * 30)
jogador = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if jogador.strip() == '':
    ficha(g = gols)
else:
    ficha(jogador, gols)