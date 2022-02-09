valor = '0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789' 
n = 10

contadores = [i for i in range (0, len(valor), n)]
tuplas = [(i, i + n ) for i in range(0, len(valor), n)]
lista =[valor[i:i + n] for i in range(0, len(valor), n)]
raw = [f'valor[{i}:{i + n}]' for i in range(0, len(valor), n)]
retorno = '.'.join(lista)
print(contadores)
print(tuplas)
print(raw)
print(retorno)