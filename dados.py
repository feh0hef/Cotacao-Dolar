import requests
import numpy as np
import psycopg2 as pg
import pandas as pd
import pprint
import json
from conexoesBD import postgresql
from datetime import date
from sshtunnel import SSHTunnelForwarder

#Solicitar dados na API
def solicitar_api(data = str):
    "solicitar dados na api do bcb"

    link = link = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{data}'&$top=100&$format=json&$select=cotacaoCompra,cotacaoVenda,dataHoraCotacao"

    requisicao = requests.get(link)

    teste_conx = str(requisicao)

    if teste_conx == "<Response [400]>":

        informacoes = requisicao.json()
        
        pprint.pprint(informacoes)

        tabela_informacoes = pd.DataFrame(informacoes['value'])

        tabela_informacoes[['dataCotacao', 'horaCotacao']] = tabela_informacoes['dataHoraCotacao'].str.split(pat=' ', n=1, expand=True)
        tabela_informacoes.drop(columns=['horaCotacao', 'dataHoraCotacao'], inplace=True)
    else:
        print("Erro de conexão com a API \nTente novamente mais tarde.")
        exit()
        
    return tabela_informacoes

#Solicitar dados no banco de dados
def solicitar_BD(data = str):
    """ Solicitar dados do banco de dados """

    try:
        conn = postgresql()
    except pg.Error as e:
        print(e)
        print('Conexão com o postgreSQL não foi realizada')
    finally:
        cur = conn.cursor()
        print('Conexão com o postgreSQL realizada.')

    try:
        print('Realizando coleta.')
        query = "SELECT cotacaoCompra, cotacaoVenda, dataCotacao from cotacaodolar"
        historico = pd.read_sql(query, conn)
    except pg.Error as e:
        print(e)
        pass
    finally:
        cur.close()
        conn.close()
        print('Fim da execução.')

    historico['datacotacao'] = historico['datacotacao'].astype(str)
    dado = historico[historico['datacotacao'].str.contains(data)]
    return dado

#Inserir dados no banco de dados
def insert_BD(data = str):
    "Inserir dados no Banco de dados"

    link = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{data}'&$top=100&$format=json&$select=cotacaoCompra,cotacaoVenda,dataHoraCotacao"

    requisicao = requests.get(link)

    informacoes = json.loads(requisicao.text)
    
    pprint.pprint(informacoes)

    tabela_informacoes = pd.DataFrame(informacoes['value'])

    tabela_informacoes[['dataCotacao', 'horaCotacao']] = tabela_informacoes['dataHoraCotacao'].str.split(pat=' ', n=1, expand=True)
    tabela_informacoes.drop(columns=['horaCotacao', 'dataHoraCotacao'], inplace=True)

    try:
        conn = postgresql()
    except pg.Error as e:
        print(e)
        print('Conexão com o postgreSQL não foi realizada')
    finally:
        cur = conn.cursor()
        print('Conexão com o postgreSQL realizada.')

    #Carregar dados em lista para inseção
    tabela_informacoes['dt_envio'] = date.today()
    dadoslegado = tabela_informacoes.values.tolist()

    try:
        print('Inicio da inserção.')
        query = "INSERT INTO cotacaodolar (cotacaoCompra, cotacaoVenda, dataCotacao, dt_envio) VALUES (%s, %s, %s, %s)"
        cur.executemany(query, dadoslegado)
        conn.commit()
    except pg.Error as e:
        print(e)
        pass
    finally:
        cur.close()
        conn.close()
        print('Fim da execução.')

#Inserir dados historicos no banco de dados
def insertHist_BD():
    "Inserir dados históricos no Banco de dados"

    link = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial='01-04-2000'&@dataFinalCotacao='11-03-2023'&$top=10000&$format=json&$select=cotacaoCompra,cotacaoVenda,dataHoraCotacao"

    requisicao = requests.get(link)

    informacoes = requisicao.json()
    
    pprint.pprint(informacoes)

    tabela_informacoes = pd.DataFrame(informacoes['value'])

    tabela_informacoes[['dataCotacao', 'horaCotacao']] = tabela_informacoes['dataHoraCotacao'].str.split(pat=' ', n=1, expand=True)
    tabela_informacoes.drop(columns=['horaCotacao', 'dataHoraCotacao'], inplace=True)

    try:
        conn = postgresql()
    except pg.Error as e:
        print(e)
        print('Conexão com o postgreSQL não foi realizada')
    finally:
        cur = conn.cursor()
        print('Conexão com o postgreSQL realizada.')

    #Carregar dados em lista para inseção
    tabela_informacoes['dt_envio'] = date.today()
    dadoslegado = tabela_informacoes.values.tolist()

    try:
        print('Inicio da inserção.')
        query = "INSERT INTO cotacaodolar (cotacaoCompra, cotacaoVenda, dataCotacao, dt_envio) VALUES (%s, %s, %s, %s)"
        cur.executemany(query, dadoslegado)
        conn.commit()
    except pg.Error as e:
        print(e)
        pass
    finally:
        cur.close()
        conn.close()
        print('Fim da execução.')