n1 = int(input("Digite um valor inteiro: "))
n2 = int(input("Digite outro valor inteiro: "))
n3 = int(input("Digite outro valor inteiro: "))

soma = 0

if n1 > n3:
    if n2 > n3:
        soma = n1 + n2
        print(soma)
        

        
if  n3 > n2:
    if n1 > n2:
        soma = n3 + n1
        print(soma) 
        
if n2 > n1:
    if n3 > n1:
       soma = n2 + n3
       print(soma) 
            