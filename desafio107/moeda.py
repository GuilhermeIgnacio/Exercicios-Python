def dobro(preco=0.0):
    x = preco * 2
    return x


def metade(preco=0.0):
    x = preco / 2
    return x


def aumento(preco=0.0, taxa=0):
    x = preco + (preco * taxa/100)
    return x


def reduzir(preco=0.0, taxa=0):
    x = preco - (preco * taxa/100)
    return x


def moeda(preco=0.0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')