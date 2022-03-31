numero = int(input('Insira um número e descubra se ele é par ou não: '))

if numero == 0:
    print("Zero é um número neutro.")
    exit()

if (numero % 2 ) == 0:
    print("O número {} é par".format(numero))
else:
    print("O número {} é ímpar".format(numero))