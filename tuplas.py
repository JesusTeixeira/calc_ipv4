l1 = (1, 2, 3, 4, 'jesus douglas')

for v in l1: #iterando sobre a lista
    print(v )

print(l1[4])#buscando o indice 4

print(l1[2:])#fatear a lista

#tupla precisa de um elemento seguido de virgula, ou mais de um elesmento, para ter mais informaçoes.

t1 = (1,2,3,4)
#t1 = (1,2,3,4) * 5 ira repetir 5x essa tupla
t2 = (5,6,7,8)
t3 = t1 + t2
print(t1)
print(t2)
print(t3)

g1 = (1,2,3,4,5)
g1 = list(g1) #lista
g1[1] = 3000
g1 = tuple(g1) #tranfomado em tupla 
print(g1)

#para alterar uma tupla, voce transforma ela numa lista e altera o valor, depois tranformar em tupla novamente.