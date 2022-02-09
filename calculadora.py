while True:
    num1 = input('Digite um numero: ')
    num2 = input('Digite outro numero: ')
    operador = input('Digite um operador: ')
    sair = input('Deseja sair? [s]im ou [n]ão ')

    if not num1.isnumeric() or not num2.isnumeric():
        print('Voce precisa digitar um numero. ')
        continue

    num1 = int(num1)
    num2 = int(num2)


    if operador == '+':
        print(num1 + num2)
    
    elif operador == '-':
        print(num1 - num2)

    elif operador == '*':
        print(num1 * num2)

    elif operador == '/':
        print(num1 / num2)

    else:
        print('Digite um operador valido. xD')

    if sair == 's':
        break