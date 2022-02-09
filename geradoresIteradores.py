#iterador
lista = [0,1,2,3,4,5]

for v in lista:
    print(v)

print('=========%%===========')
import sys

l1 = list(range(10))
print(sys.getsizeof(lista))
print('=========%%===========')
import sys
import time

def gera():
    r = []
    for n in range(100):
        r.append(n)
        time.sleep(0.1)

    return r

g = gera()

for v in g:
    print(v)

print('=========%%===========')

import sys
import time

def gera():
    for n in range(100):
        yield n 
        time.sleep(0.1)
g = gera()

for v in g:
    print(v)

print('=========%%===========')

import sys
import time
 

def gera():
    v1 = 'valor 1'
    yield v1
    v1 = 'valor 2'
    yield v1
    v1 = 'valor 3'
    yield v1

g = gera()
print(next(g))
print(next(g))
print(next(g))
print('=========%%===========')

import sys
import time

lista1 = [x for x in range(1000)]
print(type(lista))
lista2 = (x for x in range(1000))
print(lista)

print(sys.getsizeof(lista1))#espaço na memoria
print(sys.getsizeof(lista2))#espaço na memoria