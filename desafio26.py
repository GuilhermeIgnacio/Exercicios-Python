nome = input('Nome: ').strip()

a = nome.lower()
b = a.count('a')
c = a.find('a')
d = a.rfind('a')

print('A letra "A" aparece {} vezes no nome {}'.format(b, nome))
print('A primeira letra "A" aparece na posição {}'.format(c))
print('A última letra "A" aparece na posição {}'.format(d))