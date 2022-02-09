from dados import produtos, pessoas, lista

'''
#nova_lista = filter(lambda x: x > 5, lista)
nova_lista = [x for x in lista if x > 5]
print(list(nova_lista))
'''

'''
nova_lista = filter(lambda p: p['preco'] > 50, produtos)

for produtos in nova_lista:
    print(produtos)

'''

#def filtra(produto):
 #   if produto['preco'] > 50:
#        produto['e_caro'] = True
 #   return True

def filtra(pessoas):
    if pessoas['idade'] >= 18:
        return True
    else:
        return False

nova_lista = filter(filtra, pessoas)#trocar produtos por pessoas

for produto in nova_lista:
    print(produto)