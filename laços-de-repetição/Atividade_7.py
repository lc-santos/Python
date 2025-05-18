'''Faça um algoritmo que receba o preço de custo e o preço de venda de 40 produtos. Mostre como resultado se houve lucro,
prejuízo ou empate para cada produto. Informe média de preço de custo e do preço de venda.'''

for i in range(1, 40, 1):
    preco = float(input("Qual o valor do produto?: "))
    venda = float(input("Qual será o preço de venda?: "))
    if venda > preco:
        print("Houve lucro")
    if venda == preco:
        print("Empate")
    if venda < preco:
        print("Não houve lucro")