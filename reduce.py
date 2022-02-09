from dados import produtos, pessoas, lista
from functools import reduce

acumula = 0
for item in lista:
    acumula += item

print(acumula)

print('=' * 15)

soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
print(soma_lista)


soma_precos = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(soma_precos / len(produtos))#media preço dos produtos


soma_idades = reduce(lambda ac, p: ac + p['idade'], pessoas, 0)
print(soma_idades)
print(soma_idades / len(pessoas))