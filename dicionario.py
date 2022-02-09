#
# #d1 = {'chave':'valor'}
# cada chave e valores tem que ser diferentes

#       CHAVE / VALOR DA CHAVE
d1 = {'card1':'001115655'}
d1['new_key'] = '11155544'

print(d1)#chamando a variavel 
print(d1['new_key'])
print()
print()
print('=========================88===================================')
f1 = {
    'str':'valor',
    123: 'outro valor',
    (1,2,3,4): 'tupla,'
}

f1['nomedachame'] = 'agora ela existe'

if d1.get('nomedachave') is not None:
    print(d1.get('nomedachave'))

#del f1['str'] apaga a chave str

print(f1)
print()
print()
print('=========================88===================================')

a1 = {
    'chave1' :'valor',
    'chave2' : 'outro valor',
   'chave3' : 'tupla,'
}

for k in a1.items():
    print(k)


print('=========================88===================================')

import copy
c1 = {1: 'a', 2: 'b', 3: 'c', 'd': ['Jésus douglas', 'Martins Teixeira']}
v = copy.deepcopy(c1)


v[1] = 'Jésus'
v['d'] [0] = 'Jésus'

print(c1)
print(v)