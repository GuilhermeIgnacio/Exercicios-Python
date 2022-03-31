n1 = float(input("Primeira Nota: "))
n2 = float(input("Segunda Nota: "))

media = (n1 + n2) / 2

print('Média {}'.format(media))

if media < 5.0:
    print('Reprovado')
elif 5.0 <= media <= 6.9:
    print('Recuperção')
elif media >= 7.0:
    print("Aprovado")