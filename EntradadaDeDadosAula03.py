'''
Entrada de dados - aula03

Fazer cast(converter varial para tipo int)
'''

nome = input('Qual seu nome ? ')
idade = input('Qual a sua idade ? ')

ano_nascimento = 2021 - int(idade)

print()
print(f'{nome} tem {idade} anos. '
      f'{nome} nasceu em {ano_nascimento}.')


print()
print()
print()
print()      

#forma mais direta
num1 = int(input('Digite um numero: '))


#criar uma variavel str e depois converter ela
num2 = input('Digite outro numero: ')
num2 = int(num2)

print(num1 + num2)