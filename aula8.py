'''
* Criar variaveis para nome (str), idade (int),
* Altura (float) e peso (float) de uma pessoa
* Criar variavel com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casa decimais (peso e na altura da pessoa )
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
'''


nome = 'luiz'
idade = 32
altura = 1.80
peso = 80.5
ano_atual = 2019
nascimento = ano_atual - idade
imc = peso / altura ** 2


print(f'{nome} tem {idade} anos e {altura} de altura.')
print(f'{nome} pesa {peso} e seu imc é {imc:.2f}.')
print(f'{nome} nasceu em {nascimento}.')
print('"Já sei!"')


print()
print()
print()
print()

