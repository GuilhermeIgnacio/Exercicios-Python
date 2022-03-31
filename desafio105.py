def notas(*nota, sit=False):
    t = dict()
    print(nota)
    t['total'] = len(nota)
    t['maior'] = max(nota)
    t['menor'] = min(nota)
    t['media'] = sum(nota) / len(nota)
    if t['media'] >= 6:
        if sit:
            t['situação'] = 'BOA'

    if t['media'] < 6:
        if sit:
            t['situação'] = 'RUIM'
    return t


resp = notas(10, 10, 10, sit=True)
print(resp)


