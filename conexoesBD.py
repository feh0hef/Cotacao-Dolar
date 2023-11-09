import psycopg2 as pg

def postgresql():
    #conexão com o postgreSQL
    conn = pg.connect(database='cotacaoDolar',
        host='localhost',
        user='postgres',
        password= 'nanda1234',
        port='5432')
    return conn

