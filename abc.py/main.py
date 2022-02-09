'''
file = open('abc.txt', 'w+')
file.write('line 1\n')
file.write('line 2\n')
file.write('line 3\n')

file.seek(0, 0)
print('Lendo linhas: ')
print(file.read())
print('#' * 10)



file.seek(0, 0)
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')
print('#' * 10)


file.seek(0 , 0)
for linha in file.readlines():
    print(linha, end='')
file.close()

'''

'''
with open('abc.txt', 'w+') as file:
    file.write('linha 1\n')
    file.write('linha 2\n')
    file.write('linha 3\n')
    
    file.seek(0)
    print(file.read())
    
print('#' * 10)

with open('abc.txt', 'r') as file:
    print(file.read())
    
print('#' * 10)

with open('abc.txt', 'a+') as file:
    file.write('outra linha\n')
    file.seek(0)
    print(file.read())
    
'''

'''
import os
os.remove('abc.txt')
'''