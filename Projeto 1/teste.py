produtos2 = {'codigo': 1, 'nome': 'Jenipapo', 'preco': 25,
    'codigo': 2, 'nome': 'Lichia', 'preco': 28,
    'codigo': 3, 'nome': 'Pitaya', 'preco': 30,
    'codigo': 4, 'nome': 'Kiwi', 'preco': 24,
    'codigo': 5, 'nome': 'Goiaba', 'preco': 12,
    'codigo': 6, 'nome': 'Pitanga', 'preco': 14,
    'codigo': 7, 'nome': 'Café', 'preco': 20}

produtos3 = {
    'codigo': [1, 2, 3, 4, 5, 6, 7],
    'nome': ['Jenipapo', 'Lichia', 'Pitaya', 'Kiwi', 'Goiaba', 'Pitanga', 'Café'],
    'preco': [25, 28, 30, 24, 12, 14, 20]
    }

#print(produtos2[0])

#carrinho = [produtos2[0]]

#print(carrinho)

#carrinho = produtos2[1]

#print(carrinho)

#print(type(produtos3))
carrinho = {}
#lista = produtos3.values()
#print(produtos3.values())

carrinho.update({'color': 'White'})

print(carrinho)
