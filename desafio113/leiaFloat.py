from isFloat import *


def leiaFloat(num):
    try:
        x = float(input(num))
    except(ValueError, TypeError):
        while True:
            print('ERRO: Digite um número real válido')
            x = str(input('Digite um número real: '))
            if isFloat(x):
                break
    return x
