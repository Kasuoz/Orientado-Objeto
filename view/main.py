from model.pessoafis import pessoaFisica
from model.pessoajur import pessoaJuridica
from controller.pessoafisica import create_psf, read_psf
from controller.pessoajuridica import create_psj, read_psj

def menu():
    menu = 1
    while (menu !=0):
        print("*"*30)

        menu_inicial = int(input('''Selecione o carro
        \n1 - Carro 1
        \n2 - Carro 2
        \n Digite o número da opção desejada: '''))

        match menu_inicial:
            case 1:
                menu = int(input("Menu de Cadastro \n 1 - Cadastrar Carro \n2 - Listar carro \n0 - Sair "))
                match menu: 
                    case 1:
                        print("Cadastro da conta")
                        pessoafisica = pessoaFisica()
                        pessoafisica.marca = input("Digite a marca: ")
                        pessoafisica.modelo = input("Digite a modelo: ")
                        pessoafisica.placa = input("Digite a placa: ")
                        pessoafisica.cor = input("Digite a cor: ")
                        pessoafisica.ano = input("Digite a ano: ")

                        create_psf(pessoaFisica)

                    case 2:
                        print("Lista")
                        read_psf()

            case 2:
                menu = int(input('''1 - Selecione
                 \n1 - Para Cadastrar: 
                 \n2 - Para listar:  
                 \n Digite o número escolhido: '''))
                
                match menu: 
                    case 1:
                        print("Cadastro da conta")
                        pessoajuridica = pessoaJuridica()
                        pessoajuridica.marca = input("Digite a marca: ")
                        pessoajuridica.modelo = input("Digite a modelo: ")
                        pessoajuridica.placa = input("Digite a placa: ")
                        pessoajuridica.cor = input("Digite a cor: ")
                        pessoajuridica.ano = input("Digite a ano: ")

                        create_psj(pessoaJuridica)

                    case 2:
                        print("Lista")
                        read_psj()
