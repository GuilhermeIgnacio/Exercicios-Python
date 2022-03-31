a = float(input('Primeira Reta: '))
b = float(input('Segunda Reta: '))
c = float(input('Terceira Reta: '))

if a+b>=c and b+c>=a and c+a>=b:
    print('O Triângulo é válido.')
else:
    print('O Triângulo não é válido')