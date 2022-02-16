# Conversor de Medidas
m = float(input('Uma distância em metros: '))
print(f'A medida de {m}m corresponde a')
print(f'{m/1000}km\n{m/100}hm\n{m/10}dam\n{m*10:.0f}dm\n{m*100:.0f}cm\n{m*1000:.0f}mm')