nome = input('Insira o nome: ').strip()

a = nome.upper()
b = a.find('SILVA')

if (b) == 0:
    print('O nome {} possui SILVA'.format(nome))
    exit()
else:
    print('O nome {} não possui SILVA'.format(nome))
