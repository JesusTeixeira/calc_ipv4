'''def funcao():
    print('Ola, aprendendo como fazer uma função')


funcao()
funcao()
'''
'''
def saudacao(msg='Ola', nome='usuario'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    print(msg, nome)

saudacao(nome='zezinho', msg='Ola')
saudacao('oi','luizinho')
saudacao('ola', 'manorgildo')
saudacao('como vai?', 'fernanda')
saudacao('tudo bem?', 'nathalia')
'''


def divisao(n1, n2):
    if n1 and n2 == 0:
        return

    return n1 / n2

divide = divisao(0,10)

if divide:
    print(divide)
else:
    print('Conta inválida')