from model.carrodois import carrodois

def create_cr2(carro):
    carros = open('carrodois.txt', 'a')
    carros.write(str(carro)+'\n')
    carros.close

def read_cr2():
    lista_carros = []
    carros = open('carrodois.txt', 'r')
    for carro in carros:
        carro = carro.strip()
        carro_objeto = carro.split(';')

        print(carro_objeto)

        carroDois = carrodois()

        carroDois.marca = carro_objeto[0]
        carroDois.modelo = carro_objeto[1]
        carroDois.placa = carro_objeto[2]
        carroDois.cor = carro_objeto[3]
        carroDois.ano = carro_objeto[4]

        lista_carros.append(carro)
    carros.close
    return lista_carros
