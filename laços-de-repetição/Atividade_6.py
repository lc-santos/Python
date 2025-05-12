
'''06) - A concessionária de veículos “CARANGO VELHO” está vendendo os seus veículos com desconto. Faça um algoritmo que calcule e exiba o valor do desconto e o valor a ser pago pelo
cliente de vários carros. O desconto deverá ser calculado de acordo com o ano do veículo. Até 2000 - 12% e acima de 2000 - 7%. O sistema deverá perguntar
se o usuário deseja continuar calculando desconto até que a resposta seja: “(N) Não”.
Informar total de carros com ano até 2000, total de carros acima do ano 2000 e o total geral.'''


program = True
carro2000 = 0
carro2001 = 0
consultas = 1
valor = 0 
valortotal = 0


while program == True:
    valor = int(input("Qual o valor do carro escolhido?: "))
    ano = int(input("Qual o ano do carro?: "))
    if ano <= 2000:
        carro2000 += 1
        valortotal = valor + valortotal
        print(f'O carro no valor de {valor} com o desconto de 12%, custará: {valor - valor * 12 / 100}')
    if ano > 2000:
        carro2001 += 1 
        valortotal = valor + valortotal
        print(f'O carro no valor de {valor} com o desconto de 7%, custará: {valor - valor * 7 / 100}')    
            
    repeat = str(input("Deseja comprar mais algum carro?: [S] Sim [N] Não: ")).upper()
    if repeat == "S":
        consultas += 1
        continue
    
    if repeat == "N":
        print("Ok")
        print(" Total de carros: {}\n Total de carros até 2000: {}\n Total de carros acima de 2000: {}\n Valor total: {}".format(consultas,carro2000,carro2001,valortotal))
        break
    
    
    