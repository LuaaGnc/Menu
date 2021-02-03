import os.path
from time import sleep

# Definição de Cores a utilizar
cores = ('\033[m',              # 0 - Sem cores
         '\033[0;30;31m',       # 1 - vermelho
         '\033[0;30;32m',       # 2 - Verde
         '\033[0;30;33m',       # 3 - Amarelo
         '\033[0;30;34m',       # 4 - Azul
         '\033[0;30;35m',       # 5 - Roxo
         '\033[7;30m',          # 6 - Branco
         '\033[0m')             # 7 - Final

opcoes = {
        'zero': 'MENU PRINCIPAL',
        
        'um': 'Ver pessoas cadastradas',
        
        'dois': 'Cadastrar nova pessoa',
        
        'tres': 'Sair do Programa',
        'tres_opt': 'ATÉ LOGO  - - - - SAINDO DO SISTEMA - - - -  ATÉ LOGO'
    }
    

def introd_menu(numero='0'):

    print('-' * 30)
    print(cores[5] + f'{opcoes["zero"].center(30)}' + cores[7])
    print('-' * 30)
    print('1 - ', cores[4] + opcoes['um'] + cores[7])
    print('2 - ', cores[4] + opcoes['dois'] + cores[7])
    print('3 - ', cores[4] + opcoes['tres'] + cores[7])
    print('-' * 30)
    
    num = input(cores[3] + 'Sua opção >> ' + cores[7])
    print('\n\n')
    
    if num == '3':
        saida()
    else:
        valido_menu(num)
    

# Valida se o número é ou não válido
def valido_menu(numero):
    """
    :param numero: Valor qualquer
    :return: int(numero)

    --> Verifica se o valor corresponde a um número correspondente aos demonstrados no menu!
    --> Números disponíveis: [1, 2, 3]
    """
    
    if numero == '1' or numero == '2':
        # Leva para LISTA  ou  CADASTRO
        print('-' * 60)
        print(f' Opção {numero}'.center(60))
        print('-' * 60, end='\n\n')
        sleep(0.3)
        
        if numero == '1':
            opt1()
        else:
            opt2()
        
        sleep(2)
        introd_menu()

    else:
        # Significa que cometeram um erro
        if numero.isnumeric():
            print(cores[1] + 'ERRO!! -> Digite um valor válido!\n\n' + cores[7])
            sleep(1.5)
            introd_menu()
        else:
            print(cores[1] + 'ERRO!! -> Digite um número inteiro válido\n\n' + cores[7])
            sleep(1.5)
            introd_menu()


# Ver pessoas cadastradas
def opt1():
    # Local de armazenamento do arquivo
    path = 'C:\\Users\\luisg\\OneDrive\\Documentos\\GitHub\\Menu\\Armazem\\db.txt'
    
    # Se o arquivo não for encontrado, ele cria um arquivo
    try:
        # Abre para leitura
        arquivo = open(path, 'r+')
    except FileNotFoundError:
        # Cria o arquivo
        arquivo = open(path, 'w+')
    
    for i in arquivo.readlines():
        print(f' --> {i}')
    print()


# Cadastrar uma pessoa
def opt2():
    
    # Abre o arquivo no PATH determinado e no APPEND mode
    file = open('C:\\Users\\luisg\\OneDrive\\Documentos\\GitHub\\Menu\\Armazem\\db.txt', 'a+')
    
    nome = input(cores[5] + 'Digite o nome da pessoa: ' + cores[7])
    idade = int(input(cores[5] + 'Digite a idade da pessoa: ' + cores[7]))
    
    # Escreve no arquivo
    file.write(f'nome: {nome} + idd: {idade}\n')
    file.close()
    
    print('-' * 30)
    print(cores[2] + 'CADASTRADO COM SUCESSO'.center(30) + cores[7])
    print('-' * 30)
            
def saida():
    print('-' * 100)
    print(cores[2] + opcoes['tres_opt'].center(100) + cores[7])
    print('-' * 100, end='\n\n\n')
