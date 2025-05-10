custo = float(input("Quanto custou o produto?: "))
percentual = float(input("Qual será o percentual de acréscimo?: "))

calculo = custo * percentual / 100
valor_final =  custo + calculo

print("O valor de R$ {} com o percentual de {}% ficou: R$ {}".format(custo,percentual,valor_final))