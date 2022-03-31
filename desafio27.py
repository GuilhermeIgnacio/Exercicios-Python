nome = input('Nome completo: ').strip()

a = nome.split()
b = a[0]
c = a[-1]

print('Primeiro Nome: {}'.format(b))
print('Último Nome: {}'.format(c))