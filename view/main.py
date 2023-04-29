from model.pessoafis import PessoaFisica
from model.pessoajur import PessoaJuridica

from controller.pessoafisica import create_psf, read_psf
from controller.pessoajuridica import create_psj, read_pj

def menu():
    menu = 1
    while(menu !=0):
        
        print("*"*30)

        menu_inicial = int(input('''Cadastrar conta
        \n1- PessoaFisica 
        \n2- PessoaJuridica
        \n digite o numero da opcao desejada >> 
        '''))

        match menu_inicial:
            case 1:
                menu = int(input("Menu de Cadastro \n 1- Cadastrar Conta \n2-Listar Conta \n 0-sair do sistema"))
                match menu:
                    case 1 :
                        print("*"*20, "Cadastro de conta", "*"*20)
                        pessoaFisica = PessoaFisica()
                        pessoaFisica.titular = input("Digite o nome do titular >> ")
                        pessoaFisica.cpf = input("Digite seu cpf >> ")
                        pessoaFisica.saldo_inicial = int(input("Digite o seu saldo inicial >>"))

                        cond = "sim"
                        cond = input("Deseja Cadastrar segundo titular \n sim\n nao \n >>> ")
                        if cond == "sim":
                                pessoaFisica.segundo_titular = input("Digite o segundo Titular >> ")

                        create_psf(pessoaFisica)
                    case 2:
                        print("*"*20, "Lista Contas ",  "*"*20)
                        read_psf()
                        
            
            case 2:
                menu = int(input("Menu de Cadastro \n 1- Cadastrar Conta \n2-Listar Conta \n 0-sair do sistema"))
                match menu:
                    case 1 :
                        print("*"*20, "Cadastro de conta", "*"*20)
                        pessoaJuridica = PessoaJuridica()
                        pessoaJuridica.titular = input("Digite o nome do titular >> ")
                        pessoaJuridica.cnpj = input("Digite seu cnpj >> ")
                        pessoaJuridica.saldo_inicial = int(input("Digite o seu saldo inicial >>"))

                        cond = "sim"
                        cond = input("Deseja Cadastrar segundo titular \n sim\n nao \n >>> ")
                        if cond == "sim":
                                pessoaJuridica.segundo_titular = input("Digite o segundo Titular >> ")

                        create_psj(pessoaJuridica)
                    case 2:
                        print("*"*20, "Lista Contas ",  "*"*20)
                        read_pj()