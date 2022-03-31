nome = str(input('Nome completo: '))

a = len(nome) - nome.count(' ')
b = nome.split()
c = b[0]
d = len(c)


print('Nome com todas as letras maiúsculas:  {}'.format(nome.upper()))
print('Nome com todas as letras minúsculas: {}'.format(nome.lower()))
print('Quantidade de letras: {}'.format(a))
print('Quantidade de letras no primeiro nome: {}'.format(d))