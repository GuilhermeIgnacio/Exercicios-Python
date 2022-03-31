casa = float(input("Valor da casa: R$"))
salario = float(input('Seu salário: R$'))
anos = float(input('Em quantos anos pretende pagar: '))

salarioPorcentagem = salario * 0.30
mensal = casa / (anos * 12)



if mensal > salarioPorcentagem:
    print('Empréstimo Negado')
else:
    print('Empréstimo Aceito')

print('Prestação R${:.2f}'.format(mensal))