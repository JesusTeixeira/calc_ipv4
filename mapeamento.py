
from dados import produtos, pessoas, lista

'''
nova_lista = map(lambda x: x * 2, lista)
#nova_lista = [x * 2 for x in lista] resolve do mesmo jeito.
print(lista)
print(list(nova_lista))
'''
'''
for produtos in produtos:
    print(produtos)
'''
'''
precos = map(lambda p: p['preco'], produtos)

for preco in precos:
    print(preco)
    '''
'''
def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p

novos_produtos = map(aumenta_preco, produtos)

for produto in novos_produtos:
    print(produto)
'''

'''
nome = map(lambda p: p['nome'], pessoas)#trocar nome por idade

for pessoas in nome:
    print(pessoas)
    print()
'''

def aumenta_idade(p):
    p['nova_idade'] = round(p['idade'] * 1.20)


nomes = map(aumenta_idade, pessoas)

for pessoa in nomes:
    print(pessoas)