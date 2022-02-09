#se voce quer criar uma variavel que nao muda seu valor, usa-se a variavel com todas as letra maiusculas
import math

PI = math.pi

def dobra_lista(lista):
    return [x*2 for x in lista]


def multiplica(lista):
    r = 1
    for i in lista:
        r *= i
    return r

lista = [1,2,3,4,5]
print(dobra_lista(lista))
print(multiplica(lista))
print(PI)