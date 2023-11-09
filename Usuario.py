#espaços: Data da cotação
#descritivo de como inserir a data (formato 'MM-DD-AAAA')
from datetime import datetime

def solicitar_usuario():

    print("----------------------")
    print("Informe a data de cotação desejada:")
    mes = input("informe o mes desejado:")
    dia = input("informe o dia desejado:")
    ano = input("informe o ano desejado:")
    print("----------------------")
    data = '{}-{}-{}'.format(mes, dia, ano)
    data = datetime.strptime(data, '%m-%d-%Y').date()
    return data
