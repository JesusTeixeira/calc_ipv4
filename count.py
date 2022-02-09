from itertools import count

'''contador = count(start=2, step=2)

for valor in contador:
    print(valor)

    if valor >= 10:
        break
'''
print('======' * 5, '&&' * 2,'======' * 5)


'''
contador = count()
lista = ['jesus', 'pedro', 'maria', 'eduardo']
lista = zip(contador, lista)

print(list(lista))
'''
print('======' * 5, '&&' * 2,'======' * 5)

from itertools import combinations, permutations

pessoas = ['samuel','layrton', 'junho', 'gilson', 'derisvan',]
for grupo in combinations(pessoas, 2):
    print(grupo)
print('======' * 5, '&&' * 2,'======' * 5)
for grupo in permutations(pessoas,2):
    print(grupo)