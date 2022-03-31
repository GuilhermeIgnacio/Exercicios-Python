cidade = input('Digite o nome de uma cidade: ').strip()

x = cidade.upper()
a = x.split()
b = a[0]
c = b.find('SANTO')





if (c) == 0:
    print('A cidade {} começa com Santo'.format(cidade))
    exit()
else:
    print('A cidade {} não começa com Santo'.format(cidade))