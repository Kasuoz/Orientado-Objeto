from model.carroum import carroum
from model.carrodois import carrodois


from controller.carroum import create_cr1, read_cr1
from controller.carrodois import create_cr2, read_cr2

def menu():
    menu = 1
    while (menu !=0):
        print("*"*100)

        menu_inicial = int(input('''Quer cadastrar qual carro?
        \n1 - Carro 1
        \n2 - Carro 2
        \n Digite o número da opção desejada: '''))

        match menu_inicial:
            case 1:
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
