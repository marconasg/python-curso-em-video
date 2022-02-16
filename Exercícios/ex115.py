# Arquivos com Python
from ex115lib import interface, arquivo
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)

while True:
    resp = interface.menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resp == 1:
        # Opção de listar o conteúdo de um arquivo
        arquivo.lerArquivo(arq)
    elif resp == 2:
        # Opção de cadastrar uma nova pessoa
        interface.topo('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip()
        idade = interface.leiaInt('Idade: ')
        arquivo.cadastrar(arq, nome, idade)
    elif resp == 3:
        interface.topo('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[1;31mERRO! Digite uma opção válida!\033[m')
    sleep(1)