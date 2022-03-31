import random

aluno1 = 'Guilherme'
aluno2 = 'João'
aluno3 = 'Ana'
aluno4 = 'Maria'

alunos = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(alunos)

print('A ordem de apresentação será:{}'.format(alunos))