Year = int(input("Ano: "))

if((Year % 400 == 0) or
     (Year % 100 != 0) and
     (Year % 4 == 0)):
    print("O ano {} é um ano bissexto".format(Year))
else:
    print("O ano {} não é um ano bissexto".format(Year))