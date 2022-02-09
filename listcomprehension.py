l1 = [1,2,3,4,5,6,7,8,9,]
ex2 = [v * 2 for v in l1]

print(ex2)
print('================888===================')
ex3 = [(v, v2) for v in l1 for v2 in range(3)]
print(ex3)

print('================888===================')
l2 = ['anabele','isabele','isa']
ex4 = [v.replace('a','@') for v in l2]
ex4_1 = [v.replace('a','@').upper() for v in l2]
print(ex4)
print(ex4_1)

print('================888===================')
tupla = (
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),
)

ex5 = [(y, x) for x, y in tupla]
print(ex5)
print('================888===================')

c3 = list(range(50))
ex6 = [v for v in c3 if v % 2 == 0]

print(ex6)

print('================888===================')