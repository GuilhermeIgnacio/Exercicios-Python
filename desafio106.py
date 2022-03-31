def ajuda(comando):
    p = f"Acessando o manual do comando '{comando}' "
    print(len(p)*'-')
    print(p)
    print(len(p)*'-')

    return help(comando)


while True:
    a = str(input('Função ou Biblioteca > '))
    if a == 'fim':
        fim = 'Até Logo!'
        tamanho = len(fim) + 4
        print(tamanho*'-')
        print(f'  {fim}')
        print(tamanho*'-')
        break
    ajuda(a)

