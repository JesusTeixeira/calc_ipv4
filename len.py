'''
usuario = input('Digite seu usuario: ')
qtd_caracteres = len(usuario)

print(usuario, 'tem', qtd_caracteres, 'caracteres',  'e seu classe é', type(qtd_caracteres))'''

'''
usuario = input('Digite seu usuario: ')
qtd_caracteres = len(usuario)

if qtd_caracteres < 6:
    print('Digite no minimo 6 caracteres. ')
else:
    print('Você foi cadastrado no sistema')
    '''

string1 = input('Digite alguma coisa: ')
string2 = input('Digite outra coisa: ')


print(f'A quantidade de caracteres digitado foi {len(string1 + string2)}')