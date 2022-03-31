def leiaInt(dado):
    a = str(input(dado))
    while True:
        if a.isnumeric():
            int(a)
            break
        else:
            print('INVÁLIDO, DIGITE UM NÚMERO')
            a = str(input('Insira um Número: '))
    return a


n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')