nome = 'jesus douglas'

for letra in nome:
    print(letra)

print('#'*20)

for letra in nome:
    print(letra)

print(nome)

print('#'*50)

nome = 'jd'
iterador = iter(nome)

try:
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
except:
    pass