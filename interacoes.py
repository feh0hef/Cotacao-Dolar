#Realizar a busca da cotação e trazer sua variação
#alem se é significativo ou não
from dados import solicitar_api, solicitar_BD, insert_BD
from Usuario import solicitar_usuario
import numpy as np
import pandas as pd

def sol_data():
    data = str(solicitar_usuario())
    return data

data = sol_data()

#interações
def coletar_dados(data):
    """ Coletar os dados da cotação """
    #Data = "YYYY-MM-DD"
    verificar_BD = solicitar_BD(data)
    BD_vazio = verificar_BD.empty

    if BD_vazio == True:
        cotacao = solicitar_api(data)
        insert_BD(data)
    else:
        cotacao = verificar_BD

    return cotacao

def cotacao_passada():
    """ Pegar a cotação do ultimo mes """
    cotacao = coletar_dados(data)

    ano, mes, dia = data.split("-", 2)

    mes = int(mes)
    dia = int(dia)
    ano = int(ano)

    Um_mes = mes-1
    Um_ano = ano-1

    if (1 < Um_mes < 10) and dia < 10:
        cotacao_Um_mes = "{}-0{}-0{}".format(ano, Um_mes, dia)
    elif (1 < Um_mes <10) and dia >= 10:
        cotacao_Um_mes = "{}-0{}-{}".format(ano, Um_mes, dia)
    elif mes == 1 and dia < 10:
        cotacao_Um_mes = "{}-{}-0{}".format(Um_ano, 12, dia)
    elif mes == 1 and dia >= 10:
        cotacao_Um_mes = "{}-{}-{}".format(Um_ano, 12, dia)
    
    #dados do ultimo mes
    cot_Ummes = coletar_dados(cotacao_Um_mes)
    return cot_Ummes

def calculos_cot():
    """ Calculos de variação e preço médio """

    Ultimo_mes = cotacao_passada()
    cotacao = coletar_dados(data) 
    data

    Ultimo_mes['key'] = 1
    cotacao['key'] = 1

    consol = pd.merge(cotacao, Ultimo_mes, on=['key'])

    cot_compra = str(np.round(consol['cotacaocompra_x'], 2))
    cot_venda = str(np.round(consol['cotacaovenda_x'], 2))

    #variação último mes
    var_compra = str(np.round(consol['cotacaocompra_x'] - consol['cotacaocompra_y'], 2))
    var_venda = str(np.round(consol['cotacaovenda_x'] - consol['cotacaovenda_y'],2))

    #preço médio
    medio_compra = str(np.round(((consol['cotacaocompra_x'] + consol['cotacaocompra_y'])/2), 2))
    medio_venda = str(np.round(((consol['cotacaovenda_x'] + consol['cotacaovenda_y'])/2), 2))

    if var_compra or var_venda < 0:
        desv = True
    else:
        desv = False

    if medio_compra or medio_venda < 4.5:
        pm_baixo = True
    else:
        pm_baixo = False

    return data, cot_compra, cot_venda, var_compra, var_venda, medio_compra, medio_venda, desv, pm_baixo
