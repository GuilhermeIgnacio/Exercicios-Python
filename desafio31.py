distancia = float(input("Distancia a percorrer em KM: "))

preco = distancia * 0.50
preco1 = distancia * 0.45

if distancia <= 200:
    print("Sua viagem de {:.2f}Km custará R${:.2f}".format(distancia, preco))
else:
    print("Sua viagem de {:.2f}Km custará R${:.2f}".format(distancia, preco1))
