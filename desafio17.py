from math import hypot

co = float(input('Comprimento do Cateto Opostos: '))
ca = float(input('Comprimento do Cateto Adjacente: '))
h = hypot(co, ca)

print('A hipotenusa vai medir: {:.2f}'.format(h))