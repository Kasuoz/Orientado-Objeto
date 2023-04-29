from model.pessoajur import PessoaJuridica

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

        PessoaJuridica = PessoaJuridica()

        PessoaJuridica.marca = carro_objeto[0]
        PessoaJuridica.modelo = carro_objeto[1]
        PessoaJuridica.placa = carro_objeto[2]
        PessoaJuridica.cor = carro_objeto[3]
        PessoaJuridica.ano = carro_objeto[4]

        lista_carros.append(carro)
    carros.close
    return lista_carros




