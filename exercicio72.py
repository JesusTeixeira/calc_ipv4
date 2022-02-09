carrinho = []

carrinho.append(('P1',30))
carrinho.append(('P2',20))
carrinho.append(('P3',50))


soma = sum([float(y) for x, y in carrinho])
print(soma)