def ola_mundo():
    return 'Olá mundo!'

def mestre(funcao):
    return funcao()

print(ola_mundo())

print('======================**==================')


def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fala_oi(nome):
    return f'Oi {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

executando = mestre(fala_oi, 'Jesus')
executando2 = mestre(saudacao, 'Jesus', saudacao='Bom dia')
print(executando)
print(executando2)