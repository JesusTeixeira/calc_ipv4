'''
try:
    print(a) 
except:
    pass
'''
'''
try:
    print(a)
except NameError as erro:
    print('Erro do desenvolver, fale com ele')
except Exception as erro:
    print('ocorreu um erro inesperado.')

print('bora continuar...')
'''

try:
   # a = []
    a = {}
    print(a[1])
except NameError as erro:
    print('Erro do desenvolver, fale com ele')
except (IndexError, KeyError) as erro:
    print('erro de indice ou chave.')
except Exception as erro:
    print('ocorreu um erro inesperado.')

finally:
    print('finalmente.')
print('bora continuar')