def ficha(nome='<desconhecido>', gol=0):
    print(f'O jogador {nome} marcou {gol} gol(s).')


n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
