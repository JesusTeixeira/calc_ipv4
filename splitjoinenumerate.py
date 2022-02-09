'''
test = 'o brasil é penta no futebol'
lista = test.split(' ')

print(lista)

print('================**==================')


test = 'o brasil é penta no futebol'
lista = test.split(' ')
lista2 = test.split(',')

for valor in lista:
    print(f'A palavra {valor} apareceu {lista.count(valor)}x na frase.')

print('================**==================')


test = 'o brasil é penta no futebol'
lista = test.split(' ')
lista2 = test.split(',')


palavra = ''
contagem = 0
for valor in lista:
    qtd_vezes = lista.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')
'''

print('================**==================')

test = 'o brasil é penta no futebol'
lista = test.split(' ')
lista2 = ','.join(lista)

print(test)
print(lista)
print(lista2)
print('================**==================')

test = 'o brasil é penta no futebol'
lista = test.split(' ')

for indice, valor in enumerate(lista):
    print(indice, valor, lista[indice])