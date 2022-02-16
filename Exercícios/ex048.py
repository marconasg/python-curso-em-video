# Soma ímpares múltiplos de três
s = 0
t = 0
for c in range(1, 501, 2):
    if c % 3 == 0: # checa se é múltiplo de 3
        s += c
        t += 1
print(f'A soma de todos os {t} valores solicitados é {s}.')