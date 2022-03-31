n1 = int(input("Primeiro Número: "))
n2 = int(input("Segundo Número: "))
n3 = int(input("Terceiro Número: "))

if (n1 >= n2) and (n1 >= n3):
    maior = n1
elif (n2 >= n1) and (n2 >= n3):
    maior = n2
else:
    maior = n3


# -----------------------------------------------------------------


if (n1 <= n2) and (n1 <= n3):
    menor = n1
elif (n2 <= n1) and (n2 <= n3):
    menor = n2
else:
    menor = n3

print("O maior número é o {}".format(maior))
print("O menor número é o {}".format(menor))
