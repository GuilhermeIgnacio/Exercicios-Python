preço = float(input('Preço atual do produto R$: '))

valorFinal = preço - (preço * 5 / 100)

print('Com 5% de desconto, o valor final do produto vai ser: R${:.2f}'.format(valorFinal))
