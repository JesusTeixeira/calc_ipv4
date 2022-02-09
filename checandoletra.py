variavel = ['Jesus Douglas', 'Menorgildo', 'Wandergleyson']

for valor in variavel:
    if valor.startswith('J'):
        print('Começa com J', valor)
    else:
        print('Não inicia com J', valor)

print('====================$%+=====================')


variavel = ['Menorgildo', 'Wandergleyson', 'jesus douglas']

start_J = False
for valor in variavel:
    if valor.lower().startswith('j'):
        start_J = True


if start_J:
    print('Existe uma palavra que começa com J.')
else:
    print('Não existe uma palavra que começa com J.')

print('====================$%+=====================')


variavel = ['Menorgildo', 'Wandergleyson', 'djesus douglas']

for valor in variavel:
    print(valor)
    if valor.lower().startswith('j'):
        break
else:
    print('Não existe uma palavra que começa com J.')