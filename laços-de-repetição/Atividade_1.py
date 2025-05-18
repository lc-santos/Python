'''01) - Ler 80 números e ao final informar quantos número(s) est(á)ão no intervalo entre 10 (inclusive) e 150 (inclusive).'''

contador = 0
program = 80

while program >= 0:
    num = int(input("Informe um número: "))
    program -= 1
    if num >= 10 <= 150:
        contador = contador + 1
    if program < 0:
        print("Total de números entre 10 e 150: {}".format(contador))
        break