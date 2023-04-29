from model.pessoafis import PessoaFisica

def create_psj(carro):
    carros = open('pessoaJuridica.txt', 'a')
    carros.write(str(carro)+'\n')
    carros.close

def read_psj():
    lista_carros = []
    carros = open('pessoaJuridica.txt', 'r')

    for carro in carros:
        
        carro = carro.strip()
        carro__objeto = carro.split(';')

        print(carro__objeto)
        
        pessoajuridica = PessoaFisica()

        pessoajuridica.pais = carro__objeto[0]
        pessoajuridica.estado = carro__objeto[1]
        
        pessoajuridica.marca = carro__objeto[2]
        pessoajuridica.modelo = carro__objeto[3]
        pessoajuridica.placa = carro__objeto[4]
        pessoajuridica.cor = carro__objeto[5]
        pessoajuridica.ano = carro__objeto[6]

        lista_carros.append(pessoajuridica)
        
    carros.close
    return lista_carros


