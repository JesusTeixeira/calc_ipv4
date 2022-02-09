l1 = [1,2,3,4,5,6,7]
l2 = [v * 2 for v in l1]

print(l2)

print('========================&&======================')


lista = [
    ('chave', 'valor'),
    ('chave2', 'valor2'),
]

d1 = dict(lista)
print(d1)
print('========================&&======================')


lista = [
    ('chave', 2),
    (3, 'valor2'),
]

d1 = {x: y * 2 for x, y in lista}
print(d1)
print('========================&&======================')

d1 = {f'chave_{x}': x**2 for x in range(5)}
print(d1, type(d1))