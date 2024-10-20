from database_libs import *
import os

def cadastrar_usuario(conexao, nome, email, age, phone):

    create_table(conexao)

    try:
        insert_user(conexao, nome, email, age, phone)
        print(f'Cadastro realizado com sucesso!','Usuário {nome} cadastrado')

    except:
        print('Erro','Usuário inválido ou já cadastrado')
        
    #conexao = desconect_db('Usuarios.db')


def opcao_do_usuario():

    letra = True

    # Força o usuário a digitar inteiro, enquanto for um caractere 
    while letra:
        
        try:
            
            numero = int(input('Digite sua opção desejada: '))
            if (numero ==0 or numero > 4):
                print("O valor informado não é uma opção válida!")
                letra = True
            else:
                letra = False

        except ValueError:

            print("O valor informado não é uma opção válida!")
            letra = True
    
    return numero

# Assegura que apenas números sejam digitados
def input_de_numeros_inteiros():

    letra = True

    # Força o usuário a digitar inteiro, enquanto for um caractere 
    while letra:
        
        try:

            numero = int(input('Digite: '))
            letra = False

        except ValueError:

            print("O valor informado não é um inteiro!")
            letra = True
    
    return numero


def mensagem_opcoes_usuario():
    print('Sistema de cadastro de usuários')
    print('''Escolha sua opção:
            1 - Cadastrar Usuário;
            2 - Consultar Usuários Cadastrados;
            3 - Sair.
          ''')
# Limpa a tela de acordo com o sistema operacional
def limpar_tela():
    if(os.name=='nt'):
        os.system('cls')
    else:
        os.system('clear')

def interface_do_usuario():
    # Conecta ao banco de dados:
    conexao = conect_db('Dados_de_Usuarios.db')
    
    opcao = 0
    while opcao != 3:
        limpar_tela()
        mensagem_opcoes_usuario()
        opcao = opcao_do_usuario()
        
        if (opcao ==1):
            limpar_tela()
            nome = input('Digite o nome do usuário:')
            email = input('Digite o email do usuário:')
            print('Digite sua idade, apenas números inteiros são aceitos:')
            idade = input_de_numeros_inteiros()
            print('Digite seu telefone com o dd e sem espaços ou traços (apenas númeors)')
            phone = input_de_numeros_inteiros()
            cadastrar_usuario(conexao, nome, email, idade, phone)
            
        elif (opcao ==2):
            limpar_tela()
            print('Segue a relação de usuários cadastrados até o momento:\n')
            #dados = ['Nome', 'Email', 'Idade', 'Telefone']
            dados = show_users(conexao)
            
            # Títulos da tabela do banco de dados
            print ("{:<15} {:<30} {:<15} {:<10}".format('Nome','Email','Idade','Telefone'))

            for registro in dados:
                #print(*registro, sep=" ")
                Nome, Email, Idade, Telefone = registro
                print ("{:<15} {:<30} {:<15}  {:<10}".format( Nome, Email, Idade, Telefone))
            input('Digite enter para voltar')

    conexao.close()
    input('Programa finalizado, digite enter para sair.')

interface_do_usuario()