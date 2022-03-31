dias = int(input('Por quantos dias este veículo foi utilizado? '))
km = float(input('Quantos KMs este veículo percorreu? '))

preçoFinal = (dias * 60) + (km * 0.15)

print('O valor do aluguel do veículo ficou em: R${:.2f}'.format(preçoFinal))
