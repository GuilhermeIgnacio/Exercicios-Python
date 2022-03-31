from time import sleep


def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}')
    if passo < 0:
        for c in range(inicio, fim-1, passo):
            sleep(0.3)
            print(f'{c} ', end='')
    else:
        for c in range(inicio, fim+1, passo):
            sleep(0.3)
            print(f'{c} ', end='')
    print('FIM!')
    print(40*'-')

contador(1, 10, 1)
contador(10, 0, -2)

print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
print(40*'-')
if f < 0 and p == 0:
    p -= 1

if f > 0 and p == 0:
    p += 1


contador(i, f, p)
