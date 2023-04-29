from model.pessoafis import PessoaFisica
from model.pessoajur import PessoaJuridica

from controller.pessoafisica import create_psf, read_psf
from controller.pessoajuridica import create_psj, read_psj

def menu():
    menu = 1
    while (menu !=0):
        print("*"*30)

        menu_inicial = int(input('''Cadastrar carro
        \n1 - Carro 1
        \n2 - Carro 2
        \n Digite o número da opção desejada: '''))

        match menu_inicial:
            case 1:
                menu = int(input("Cadatrar digiite 1: "))
                match menu: 
                    case 1:
                        print("Cadastro da conta")
                        PessoaFisica = PessoaFisica()
                        PessoaFisica.marca = input("Digite a marca: ")
                        PessoaFisica.modelo = input("Digite a modelo: ")
                        PessoaFisica.placa = input("Digite a placa: ")
                        PessoaFisica.cor = input("Digite a cor: ")
                        PessoaFisica.ano = input("Digite a ano: ")

                    case 2:
                        print("Lista")
                        read_psf
