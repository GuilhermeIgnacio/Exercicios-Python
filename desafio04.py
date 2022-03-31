algo = input('Digite algo: ')

print('O tipo primitivo desse valor é', type(algo))

print('Só tem espaços?', algo.isspace())
print('É um número?', algo.isnumeric())
print('É alfabético?', algo.isalpha())
print('É alfanumérico?', algo.isalnum())
print('Está em letras maiúsculas?', algo.isupper())
print('Está em letras minúsculas?', algo.islower())
print('Está captalizada?', algo.istitle())

