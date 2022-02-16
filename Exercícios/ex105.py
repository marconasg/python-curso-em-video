# Analisando e gerando Dicionários
def notas(*n, sit=False):
    """
    Função para analisar notas e situações de vários alunos.

    Args:
        sit (bool, optional): Indica se deve ou não adicionar a situação. Defaults to False.

    Returns:
        dict(): Dicionário com várias informações sobre a situação da turma.
    """
    dici = {}
    dici['total'] = len(n)
    dici['maior'] = max(n)
    dici['menor'] = min(n)
    dici['média'] = float(f'{sum(n) / len(n):.2f}')
    if sit:
        if dici['média'] < 6:
            dici['situação'] = 'RUIM'
        if dici['média'] >= 6:
            dici['situação'] = 'RAZOÁVEL'
        if dici['média'] >= 7:
            dici['situação'] = 'BOA'
    return dici

resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
# help(notas)