n1 = int(input("Digite um valor inteiro: "))
n2 = int(input("Digite outro valor inteiro: "))
n3 = int(input("Digite outro valor inteiro: "))

if n1 < n2:
    if n1 < n3:
        if n2 < n3:
            print(f'{n1}{n2}{n3}')
            
if n1 > n2:
     if n1 < n3:
        if n2 < n3:
                print (f'{n2}{n1}{n3}')

if n3 < n1:
     if n3 < n2:
        if n1 > n2:
                print (f'{n3}{n2}{n1}')
                
if n2 < n3:
     if n2 < n1:
        if n1 >= n3:
                print (f'{n2}{n3}{n1}')
                
if n2 > n1:
     if n2 > n3: 
         if n1 < n3:               
                print (f'{n1}{n3}{n2}')
                
if n3 < n1:
     if n2 > n3: 
         if n2 > n1:               
                print (f'{n3}{n1}{n2}')
                
                

                
