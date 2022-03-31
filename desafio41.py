from datetime import date

ano = int(input('Insira o ano que você nasceu: '))

calc = date.today().year - ano

if calc <= 9:
    print('Você já fez ou vai fazer {} ano(s), então você se enquadra na categoria MIRIM'.format(calc))
elif calc <= 14:
    print('Você já fez ou vai fazer {} ano(s), então você se enquadra na categoria INFANTIL'.format(calc))
elif calc <= 19:
    print('Você já fez ou vai fazer {} ano(s), então você se enquadra na categoria JUNIOR'.format(calc))
elif calc <=20:
    print('Você já fez ou vai fazer {} ano(s), então você se enquadra na categoria SÊNIOR'.format(calc))
elif calc > 20:
    print('Você já fez ou vai fazer {} ano(s), então você se enquadra na categoria MASTER'.format(calc))

