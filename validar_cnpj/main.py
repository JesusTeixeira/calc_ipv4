# 04.252.011/0001-10
# 71.506.168/0001-11

import cnpj


cnpj1 = '71.506.168/0001-11'

if cnpj.valida(cnpj1):
    print(f'{cnpj1} é valido')
else:
    print(f'{cnpj1} é invalido')