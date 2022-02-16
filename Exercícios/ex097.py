# Print especial
def escreva(msg):
    print('~' * (len(msg) + 4))
    print(f'{msg:^{len(msg) + 4}}')
    print('~' * (len(msg) + 4))

escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')