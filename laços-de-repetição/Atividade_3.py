'''03) - Faça um algoritmo que receba um número e mostre uma mensagem caso este número seja maior que 80, menor que 25 ou igual a 40. O usuário deverá informar se deseja continuar informando os valores.'''

program = True

while program == True:
    
    n1 = int(input("Informe um valor: "))
    
    if n1 == 40:
        print("é igual a 40")
        
    if n1 > 80:
        print("é maior que 80")
    
    if n1 < 25:
        print("é menor que 25")
    
     
    new = int(input("Tentar outro número?: [1] Sim [2] Não:  "))
    if new == 1: 
        continue
    if new == 2:
        print("Fim do programa")
        break

