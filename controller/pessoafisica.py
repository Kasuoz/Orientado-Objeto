from model.pessoafis import PessoaFisica

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

        PessoaFisica = PessoaFisica()

        PessoaFisica.marca = carro_objeto[0]
        PessoaFisica.modelo = carro_objeto[1]
        PessoaFisica.placa = carro_objeto[2]
        PessoaFisica.cor = carro_objeto[3]
        PessoaFisica.ano = carro_objeto[4]

        lista_carros.append(carro)
    carros.close
    return lista_carros