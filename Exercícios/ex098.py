# Função de Contador
from time import sleep

def contador(i, f, p):
    print('-' * 40)
    
    if p == 0:
        p = 1
    if p < 0:
        p = abs(p) # a função abs transforma o número em positivo
    
    print(f'Contagem de {i} até {f} de {abs(p)} em {abs(p)}')
    sleep(1)
    
    if i > f:
        p = -p
        f -= 2
    
    for c in range(i, f + 1, p):
        print(c, end=' ', flush=True)
        sleep(.5)
    print('FIM!')

contador(1, 10, 1)
contador(10, 0, 2)
print('-' * 40)
print('Agora é sua vez de personalizar a contagem!')
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))