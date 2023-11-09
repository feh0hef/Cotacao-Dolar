from interacoes import calculos_cot

#Valores após solicitação
data, cot_compra, cot_venda, var_compra, var_venda, medio_compra, medio_venda, desv, pm_baixo = calculos_cot()

texto = f"""
----------------------
Data da cotação:{data:10}
Compra:{cot_compra:10}
Venda:{cot_venda:10}
----------------------
Preço médio no último mês:
Preço médio de Compra:{medio_compra:10}
Preço médio de Venda:{medio_venda:10}
----------------------
Variação no último mês:
variação de Compra:{var_compra:10}
variação de Venda:{var_venda:10}
"""

print(texto)

if desv == True and pm_baixo == True:
    print("O dólar apresentou no último mês desvalorização")
    print("E manteve seu preço médio de negociação abaixo de R$ 4.5")
elif desv == True and pm_baixo == False:
    print("O dólar apresentou no último mês desvalorização")
    print("E manteve seu preço médio de negociação acima de R$ 4.5")
elif desv == False and pm_baixo == False:
    print("O dólar apresentou no último mês valorização")
    print("E manteve seu preço médio de negociação acima de R$ 4.5")
elif desv == False and pm_baixo == True:
    print("O dólar apresentou no último mês valorização")
    print("E manteve seu preço médio de negociação abaixo de R$ 4.5")
else:
    print("")