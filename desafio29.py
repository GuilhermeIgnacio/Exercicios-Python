velocidade = float(input("Velocidade que o carro passou: "))

if velocidade > 80:
    print("Você excedu o limite de 80Km/h")
    multa = (velocidade - 80) * 7
    print("Você deve pagar uma multa de R${}".format(multa))
else:
    print("Siga com segurança.")