# Transformando módulos em pacotes
from ex111p.utilidadescev import moeda

p = float(input('Digite o preço: R$'))
moeda.resumo(p, 35, 22)