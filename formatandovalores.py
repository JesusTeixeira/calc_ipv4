num1 = 1
print(f'{num1:0>10}')

num2  = 1150
print(f'{num2:0<10}')

num3 = 2488
print(f'{num3:0^10}')


nome = 'Jésus Douglas'
print(len(nome))


nome = 'jesus douglas'
nome_formatado = '{}'.format(nome)
print(nome_formatado)

nome = 'jesus douglas'
nome_formatado = '{:@>20}'.format(nome)
print(nome_formatado)

nome = 'jesus douglas'
nome_formatado = '{n:%<20}'.format(n=nome)
print(nome_formatado)

nome = 'jesus douglas'
sobrenome = 'Teixeira'
nome_formatado = '{1:#^20}'.format(nome,sobrenome)
print(nome_formatado)


nome = 'jesus douglas'
print(nome.lower())
print(nome.upper())
print(nome.title())