#espaços: Data da cotação
#descritivo de como inserir a data (formato 'MM-DD-AAAA')
from datetime import datetime

def solicitar_usuario():

    print("----------------------")
    print("Informe a data de cotação desejada:")
    mes = int(input("informe o mes desejado:"))
    dia = int(input("informe o dia desejado:"))
    ano = int(input("informe o ano desejado:"))
    print("----------------------")

    if dia < 10 and mes < 10:
        data_bd = '{}-0{}-0{}'.format(ano, mes, dia)
    elif dia < 10 and mes >= 10:
        data_bd = '{}-{}-0{}'.format(ano, mes, dia)
    elif dia >= 10 and mes < 10:
        data_bd = '{}-0{}-{}'.format(ano, mes, dia)
    else:
        data_bd = '{}-{}-{}'.format(ano, mes, dia)

    return data_bd
