from datetime import date

ano = int(input("Em que ano você nasceu? "))

anoAtual = date.today().year

calc = anoAtual - ano

tempoFaltando = 18 - calc
tempoPassado = calc - 18

if calc < 18:
    print("Você tem {} anos ou ja fez, Você ainda não atingiu a idade para se alistar!".format(calc))
    print("Falta {} ano(s) para você pode se alistar".format(tempoFaltando))
elif calc == 18:
    print("Você tem {} anos ou ja fez, Está na hora de se alistar!".format(calc))
elif calc > 18:
    print("Você tem {} anos ou ja fez, Já passou da hora de se alistar!".format(calc))
    print("Passou {} ano(s) do seu alistamento.".format(tempoPassado))
