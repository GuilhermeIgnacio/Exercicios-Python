def leiaInt(num):
    try:
        x = int(input(num))
    except (ValueError, TypeError):
        while True:
            print('ERRO: Digite um número inteiro Válido')
            x = str(input('Digite um número inteiro: '))
            if x.isnumeric():
                break
    return x
