# Verificando as primeiras letras de um texto
c = str(input('Em que cidade você nasceu? ')).strip().lower().split()
print('santo' in c[0])
# print(c[:5].lower() == 'santo') - outro método para verificar