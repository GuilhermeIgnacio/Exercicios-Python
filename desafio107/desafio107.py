from moeda import *

p = float(input('Digite o Preço: R$ '))
print(f'O dobro de {moeda(p)} é {moeda(dobro(p))}')
print(f'A metade de {moeda(p)} é {moeda(metade(p))}')
print(f'Aumento 10% de {moeda(p)}, temos: {moeda(aumento(p, 10))}')
print(f'Reduzindo 13% de {moeda(p)}, temos: {moeda(reduzir(p, 13))}')
