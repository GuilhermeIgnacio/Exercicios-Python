from urllib.request import urlopen

try:
    html = urlopen("https://www.google.com/")
except:
    print()
    print('\033[1:31mGoogle Não Disponível')
else:
    print()
    print('\033[1:36mConsegui acessar o Google com sucesso')