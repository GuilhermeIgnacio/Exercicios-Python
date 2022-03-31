salarioAtual = float(input('Salário: R$'))

porcentagem = 15 / 100
aumento = salarioAtual * porcentagem
novoSalario = aumento + salarioAtual

print('Com o reajuste o funcionário passará a receber: R${:.2f}'.format(novoSalario))
