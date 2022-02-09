#positivos [0123456789101112131415]
'''
teste = 'em busca da melhor versao'
print(teste[15])

teste = 'em busca da melhor versao'
print(teste[20])
'''


#negativo
'''
teste = 'em busca da melhor versao'
print(teste[:-1])

teste = 'em busca da melhor versao'
print(teste[:-5])


teste = 'em busca da melhor versao'
new_teste = teste[3:7]
print(new_teste)
'''

#pulando de 2 em 2
'''
teste = 'em busca'
new_teste = teste[0:6:2]
print(new_teste)


teste = 'em_busca'
new_teste = teste[::2]
print(new_teste)'''

#len


teste = 'python_s2'

print(len(teste))

for letra in teste:
    print(letra)