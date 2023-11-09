# Cotacao-Dolar
Esse código foi criado com o objetivo de informar a cotação do dolar para o usuário na data selecionada.
Projeto desenvolvido para a vaga de estágio em Riscos na Kinea.

Contribuições e comentários são aceitos, dado que após a entrega do código (09/11) o projeto não será subordinado a avaliação.

Explicação:

Desenvolva uma aplicação que o cliente consulte o banco de dados em busca da cotação de dólar na data inserida por ele. Caso não tenha, consulte a cotação na API do banco central, cadastre a cotação no banco de dados e retorne ao cliente.


1. Para o Frontend, desenvolva onde preferir

2. Para o Backend, o que preferir

3. Para o banco de dados, utilize de sua preferência,  pode utilizar o SqLite3

 
Passo a passo:

O usuário deve inserir a data pelo frontend, que irá requisitar ao backend.

O backend irá consultar a data no banco de dados, caso não tenha a cotação salva, buscará na API do banco central, salvar em banco de dados e retornar ao usuário.

Além de visualizar o valor da cotação, o mesmo deve indicar sua variação e se tal variação é estatisticamente significativo para uma análise mais detalhada.


Link da API do Banco Central: https://dadosabertos.bcb.gov.br/dataset/dolar-americano-usd-todos-os-boletins-diarios


Bônus:

1. Crie um docker-compose com a aplicação.

2. Disponibilizar online de alguma plataforma de sua preferência como (Heroku, Google Cloud, AWS).
