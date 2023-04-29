<<<<<<< HEAD
from model.carroum import carroum
from model.carrodois import carrodois


from controller.carroum import create_cr1, read_cr1
from controller.carrodois import create_cr2, read_cr2
=======
from model.pessoafis import pessoaFisica
from model.pessoajur import pessoaJuridica
from controller.pessoafisica import create_psf, read_psf
from controller.pessoajuridica import create_psj, read_psj
>>>>>>> 3075a411379ae433745f13aff223818975cbf28d

def menu():
    menu = 1
    while (menu !=0):
<<<<<<< HEAD
        print("*"*100)

        menu_inicial = int(input('''Quer cadastrar qual carro?
=======
        print("*"*30)

        menu_inicial = int(input('''Selecione o carro
>>>>>>> 3075a411379ae433745f13aff223818975cbf28d
        \n1 - Carro 1
        \n2 - Carro 2
        \n Digite o número da opção desejada: '''))

        match menu_inicial:
            case 1:
<<<<<<< HEAD
                menu = int(input("Cadastrar digite 1/ para Listar  digite 2 / para sair digite 0: "))
                match menu: 
                    case 1:
                        print("Cadastro da conta")
                        carroUm = carroum()
                        carroUm.marca = input("Digite a marca: ")
                        carroUm.modelo = input("Digite a modelo: ")
                        carroUm.placa = input("Digite a placa: ")
                        carroUm.cor = input("Digite a cor: ")
                        carroUm.ano = input("Digite a ano: ")

                        create_cr1(carroUm)


                    case 2:
                        print("Lista")
                        read_cr1()

            case 2:
                menu = int(input("Cadastrar digite 1/ para Listar  digite 2 / para sair digite 0: "))
                match menu: 
                    case 1:
                        print("Cadastro da conta")
                        carroDois = carrodois()
                        carroDois.marca = input("Digite a marca: ")
                        carroDois.modelo = input("Digite a modelo: ")
                        carroDois.placa = input("Digite a placa: ")
                        carroDois.cor = input("Digite a cor: ")
                        carroDois.ano = input("Digite a ano: ")

                        create_cr2(carroDois)


                    case 2:
                        print("Lista")
                        read_cr2()
=======
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
>>>>>>> 3075a411379ae433745f13aff223818975cbf28d
