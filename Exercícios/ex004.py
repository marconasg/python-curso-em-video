# Dissecando uma Variável
algo = input('Digite algo: ')
print('O tipo primitivo desse valor é',type(algo))
print('Só tem espaços?',algo.isspace())
print('É numérico?',algo.isnumeric())
print('É alfanumérico?',algo.isalnum())
print('É alfabético?',algo.isalpha())
print('Está todo em maiúscula?',algo.isupper())
print('Está todo em minúscula?',algo.islower())
print('Está capitalizada?',algo.istitle())