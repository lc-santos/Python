

num = int(input('Qual o número?:'))


#imparpar = num % 2

#if imparpar == 0:
# print(f'O número {num} é par')
#else: print(f'O número {num} é impar')


resposta = (num % 2) == 0
if resposta == True:
 print(f'O valor {num} é Par')
else: print(f'O valor {num} é impar')
