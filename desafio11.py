l = int(input('Largura da parede em Metros: '))
h = int(input('Altura da parede em Metros: '))

a = l * h  # Área da figura
t = a / 2  # Quantidade de tinta necessária

print('')

print('A parede tem {} M2'.format(a))
print('Será necessário {} litros de tinta para pintar a parede'.format(t))
