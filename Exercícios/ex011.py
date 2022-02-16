# Pintando Parede
l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
area = l * a
tinta = area / 2
print(f'Sua parede tem a dimensão de {l}x{a} e sua área é de {area:.1f}m².')
print(f'Para pintar essa parede, você precisará de {tinta:.1f}l de tinta.')