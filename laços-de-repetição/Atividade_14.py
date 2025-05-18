'''14) - Dados três valores A, B e C, em que A e B são números reais e C é um caractere, pede-se para imprimir o resultado da operação
de A por B se C for um símbolo de operador aritmético; caso contrário deve ser impressa uma mensagem de operador não definido.
Tratar erro de divisão por zero. Repita esse processo cinco vezes.'''


for i in range(5):

    a = float(input("Valor a: "))
    b = float(input("Valor b:"))
    c = str(input("Simbolo da operação: "))

    if c == "-":
        print(a - b)

    if c == "+":
        print(a + b)

    if c == "*":
        print(a * b)

    if c == "/":
        print(a / b)
    else:
        print("Operador não definido")