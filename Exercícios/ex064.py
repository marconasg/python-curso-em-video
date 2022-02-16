# Tratando vários valores v1.0
n = t = s = 0

while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        t += 1
        s += n

print(f'\nVocê digitou {t} números e a soma entre eles foi {s}.')