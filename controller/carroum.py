from model.carroum import carroum

def create_cr1(carro):
    carros = open('carroUm.txt', 'a')
    carros.write(str(carro)+'\n')
    carros.close

def read_cr1():
    lista_carros = []
    carros = open('carroUm.txt', 'r')
    for carro in carros:
        carro = carro.strip()
        carro_objeto = carro.split(';')

        print(carro_objeto)

        carroUm = carroum()

        carroUm.marca = carro_objeto[0]
        carroUm.modelo = carro_objeto[1]
        carroUm.placa = carro_objeto[2]
        carroUm.cor = carro_objeto[3]
        carroUm.ano = carro_objeto[4]

        lista_carros.append(carroum)
    carros.close()
    return lista_carros

def delete_cr1(carro):
    carros = open('carroUm.txt', 'd')