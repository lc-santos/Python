#  Ler o nome do vendedor
# o seu salario fixo e o total de vendas, sabendo que o vendedor ganha 15% da comissao sobre suas vendas efetuadas

nome_vendedor = input('Informe o nome do vendedor: ')
salario_fixo = float(input('Informe o salário fixo do vendedor: '))
total_vendas = float(input('Informe o total do vendedor: '))

comissao = total_vendas * 15 / 100
salario_final = salario_fixo + comissao

print('O vendedor', nome_vendedor)
print('Possui o salário fixo de R$', salario_fixo)
print('E o seu salário final é R$', salario_final)