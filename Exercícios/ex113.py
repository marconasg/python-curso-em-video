# Funções aprofundadas em Python
def leiaInt(txt):
    while True:
        try:
            n = int(input(txt))
        except:
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
        else:
            return n

def leiaFloat(txt):
    while True:
        try:
            n = float(input(txt))
        except:
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
        else:
            return n

num = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {num} e o real foi {real}')