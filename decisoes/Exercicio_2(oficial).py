a = int(input('Digite valor A: '))
b = int(input('Digite valor B: '))

if b < a:
    c = a
    a = b
    b = c

print(f'A = {a} B = {b} em ordem crescente')

