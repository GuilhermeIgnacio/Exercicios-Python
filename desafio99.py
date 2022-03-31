from random import randint
from time import sleep


def maior():
    lista = list()
    for c in range(randint(1, 11)):
        lista.append(randint(0, 10))
    print(40*'-')
    print('Analisando os valores passados...')
    print(*lista, end='')
    print(f' Foram informados {len(lista)} valores ao todo')
    print(f'O maior valor informado foi {max(lista)}')
    print(40*'-')


for c in range(randint(1, 6)):
    sleep(0.3)
    maior()
