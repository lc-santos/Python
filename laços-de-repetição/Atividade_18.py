'''18) - Escrever um algoritmo que leia três valores inteiros e verifique se eles podem ser os lados de um triângulo. Se for, informar qual o tipo de triângulo que eles formam: equilátero, isóscele ou escaleno. Propriedade: o comprimento de cada lado de um triângulo é menor do que a soma dos comprimentos dos outros dois lados.
	  Triângulo Equilátero: aquele que tem os comprimentos dos três lados iguais;
	  Triângulo Isóscele: aquele que tem os comprimentos de dois lados iguais. Portanto, todo triângulo equilátero é também isóscele;
	  Triângulo Escaleno: aquele que tem os comprimentos de seus três lados diferentes.
	  Repita esse processo 5 vezes.'''

for cont in range(1,6,1):
    a = int(input("Lado A:"))
    b = int(input("Lado B:"))
    c = int(input("Lado C:"))
   
    if (a < b + c) and (b < a + c) and (c < a + b):
        print("Os lados formam um triângulo.")
       
        if a == b and b == c: 
            print("Tipo: Equilátero")    
        if a == b or b == c or a == c:
            print("Tipo: Isósceles")
        else: 
            print("Tipo: Escaleno")
    else:
        print("Não formam um triângulo.")