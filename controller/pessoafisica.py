from model.pessoafis import pessoaFisica

def create_psf(carro):
    carros = open('pessoaFisica.txt', 'a')
    carros.write(str(carro)+'\n')
    carros.close

def read_psf():
    lista_carros = []
    carros = open('pessoaFisica.txt', 'r')
    for carro in carros:
        carro = carro.strip()
        carro_objeto = carro.split(';')

        print(carro_objeto)

        pessoaFisica = pessoaFisica()

        pessoaFisica.marca = carro_objeto[0]
        pessoaFisica.modelo = carro_objeto[1]
        pessoaFisica.placa = carro_objeto[2]
        pessoaFisica.cor = carro_objeto[3]
        pessoaFisica.ano = carro_objeto[4]

        lista_carros.append(carro)
    carros.close
    return lista_carros