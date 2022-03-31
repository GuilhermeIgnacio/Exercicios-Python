def fatorial(num, show=True):
    if show == 'n':
        show = False
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


fa = fatorial(int(input('Fatorial de: ')), str(input('Deseja ver o progresso? [S/N] ')).strip().lower())
print(fa)
