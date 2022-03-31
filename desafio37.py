numero = int(input('Insira um número: '))

print('-=-' * 10)
print('Digite 1 para binário')
print('Digite 2 para octal')
print('Digite 3 para hexadecimal')
print('-=-' * 10)

opcao = int(input('Opção: '))

if opcao == 1:
    binario = bin(numero)
    print(f'Número {numero} em binário: {binario[2:]}')

elif opcao == 2:
    octal = oct(numero)
    print(f'O Número {numero} em octal: {octal[2:]}')

elif opcao == 3:
    hexadecimal = hex(numero)
    print(f'O Número {numero} em hexadecimal: {hexadecimal[2:]}')

