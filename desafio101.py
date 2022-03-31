from datetime import date


def voto(ano):
    idade = date.today().year - ano
    print(f'{idade} anos, ', end='')
    if idade < 16:
        resp = 'NÃO VOTA.'
        return resp
    elif 16 <= idade < 18:
        resp = 'VOTO OPCIONAL.'
        return resp
    elif 18 <= idade < 65:
        resp = 'VOTO OBRIGATÓRIO.'
        return resp
    elif idade >= 65:
        resp = 'VOTO OPCIONAL.'
        return resp


a = voto(int(input('Ano de Nascimento: ')))
print(a)
