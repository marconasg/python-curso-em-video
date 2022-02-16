# Analisando Triângulos v1.0
print('-=-' * 12)
print('Analisador de Triângulos')
print('-=-' * 12)
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    print('Os segmentos acima PODEM formar um triângulo.')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo.')