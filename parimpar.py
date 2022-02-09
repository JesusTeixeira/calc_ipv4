'''
Faça um programa que peça ao usuario para digitar um numero inteiro e saber se é par ou impar

'''

num1 = input('Digite um numero inteiro: ')

if num1.isdigit():
    num1 = int(num1)

    if num1 % 2 == 0:
        print(f'{num1} é par')

    else:
        print(f'{num1} é impar')
else:
    print('Isso não é um numero inteiro.')