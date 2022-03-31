salario = float(input("Salário R$"))


if salario > 1250:
    novoSalario = (salario * 0.1) + salario  # Aumento de 10%
    print("O novo salário desse funcionário será de R${:.2f}".format(novoSalario))
else:
    novoSalario1 = (salario * 0.15) + salario
    print("O novo salário desse funcionário será de R${:.2f}".format(novoSalario1))

