'''
lista = ['a','b','c','d','e']

string = 'abcde'
print(string[1])
print(string[::2])



l1 = [1,2,3,4]
l2 = [5,6]
l3 = l1 + l2
print(l3)

print('#################################')

l1 = [1,2,3,4]
l2 = [5,6]
l1.extend(l2)
print(l1)
print(l2)
print('#################################')

l1 = [1,2,3,4]
l2 = [5,6,7]

l2.append('0')

print( l2[3] )
print(l1)

print('#################################')

l1 = [1,2,3,4]
l2 = [5,6,7,8]

l2.insert(0, 'abacate')

print( l2[0] )
print('#################################')


l2 = [4,5,6]
print(l2)
l2.insert(0, 'banana')
print(l2)
l2.pop()
print(l2)

print('#################################')

l2 = [4,5,6]
print(l2)
l2.insert(0, 'banana')
print(l2)
del(l2[0])
print(l2)

print('#################################')

l2 = [4,5,6]

print(max(l2))
print(min(l2))

'''

'''
l2 = list(range(0, 100, 8))

for valor in l2:
    print(valor)

'''

l2 = ['String', True, 10, -20.5]

for elemento in l2:
    print(f'O tipo de elemento é {type(elemento)} e seu valor é {elemento}')