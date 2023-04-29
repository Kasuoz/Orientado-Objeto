from model.pessoajur import pessoaJuridica

def create_psj(carro):
    carros = open('pessoaJuridica.txt', 'a')
    carros.write(str(carro)+'\n')
    carros.close

def read_psj():
    lista_carros = []
    carros = open('pessoaJuridica.txt', 'r')
    for carro in carros:
        carro = carro.strip()
        carro_objeto = carro.split(';')

        print(carro_objeto)

        pessoajuridica = pessoaJuridica()

        pessoajuridica.marca = carro_objeto[0]
        pessoajuridica.modelo = carro_objeto[1]
        pessoajuridica.placa = carro_objeto[2]
        pessoajuridica.cor = carro_objeto[3]
        pessoajuridica.ano = carro_objeto[4]

        lista_carros.append(carro)
    carros.close
    return lista_carros




