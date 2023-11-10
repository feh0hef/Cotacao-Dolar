#Realizar a busca da cotação e trazer sua variação
#alem se é significativo ou não
from dados import solicitar_api, solicitar_BD, insert_BD
from Usuario import solicitar_usuario
import numpy as np
import pandas as pd

data_bd = solicitar_usuario()

#interações
def coletar_dados(data_bd):
    """ Coletar os dados da cotação """
    #Data = "YYYY-MM-DD"
    verificar_BD = solicitar_BD(data_bd)
    BD_vazio = verificar_BD.empty

    if BD_vazio == True:

        ano, mes, dia = data_bd.split("-", 2)

        mes = int(mes)
        dia = int(dia)
        ano = int(ano)

        if dia < 10 and mes < 10:
            data_api = '{}-0{}-0{}'.format(mes, dia, ano)
        elif dia < 10 and mes >= 10:
            data_api = '{}-{}-0{}'.format(mes, dia, ano)
        elif dia >= 10 and mes < 10:
            data_api = '{}-0{}-{}'.format(mes, dia, ano)
        else:
            data_api = '{}-{}-{}'.format(mes, dia, ano)

        cotacao = solicitar_api(data_api)
        insert_BD(data_api)
    else:
        cotacao = verificar_BD

    return cotacao

def cotacao_passada():
    """ Pegar a cotação do ultimo mes """

    ano, mes, dia = data_bd.split("-", 2)

    mes = int(mes)
    dia = int(dia)
    ano = int(ano)

    Um_mes = mes-1
    Um_ano = ano-1

    if Um_mes >= 10 and dia >= 10:
        cotacao_Um_mes = "{}-{}-{}".format(ano, Um_mes, dia)
    elif Um_mes >= 10 and dia < 10:
        cotacao_Um_mes = "{}-{}-0{}".format(ano, Um_mes, dia)
    elif (1 < Um_mes < 10) and dia < 10:
        cotacao_Um_mes = "{}-0{}-0{}".format(ano, Um_mes, dia)
    elif (1 < Um_mes <10) and dia >= 10:
        cotacao_Um_mes = "{}-0{}-{}".format(ano, Um_mes, dia)
    elif mes == 0 and dia < 10:
        cotacao_Um_mes = "{}-{}-0{}".format(Um_ano, 12, dia)
    elif mes == 0 and dia >= 10:
        cotacao_Um_mes = "{}-{}-{}".format(Um_ano, 12, dia)
    
    #dados do ultimo mes
    cot_Ummes = coletar_dados(cotacao_Um_mes)
    return cot_Ummes

def calculos_cot():
    """ Calculos de variação e preço médio """

    Ultimo_mes = cotacao_passada()
    cotacao = coletar_dados(data_bd) 
    data_bd

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

    return data_bd, cot_compra, cot_venda, var_compra, var_venda, medio_compra, medio_venda, desv, pm_baixo
