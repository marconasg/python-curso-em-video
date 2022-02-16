# Validando entrada de dados em Python
def leiaInt(msg):
    """
    Faz a leitura de um número inteiro.

    Args:
        msg (str): mensagem digitada

    Returns:
        str: um número
    """
    while True:
        num = str(input(msg))
        if num.isnumeric():
            return int(num) # retorna o valor em inteiro
        print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')