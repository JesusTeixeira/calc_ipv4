cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']

estados = ['SP', 'MG', 'BA']

cidades_estados = zip(cidades, estados)

#print(list(cidades_estados))
print(dict(cidades_estados))

print('=====&&=====' * 10)


from itertools import zip_longest

cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'outro', 'outro']

estados = ['SP', 'MG', 'BA']

cidades_estados = zip_longest(estados, cidades, fillvalue='Estado')

#print(list(cidades_estados))
print(dict(cidades_estados))


print('=====&&=====' * 10)


variavel = ((x, y) for x, y in zip('alo', 'alo'))
print(list(variavel))