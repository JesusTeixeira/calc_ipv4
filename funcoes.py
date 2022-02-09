variavel = 'valor'

def func():
    print(variavel)

def func2():
    variavel = 'outro valor'
    print(variavel)

func()
func2()
print(variavel)
print('======================**==================')


variavel = 'valor'

def func():
    print(variavel)

def func2(arg=None):
    arg = arg.replace('v', 'c')
    return arg

func()
outra_variavel = func2(arg=variavel)
print(outra_variavel)
print('======================**==================')

def func():
    outra_variavel = 'Jésus Douglas'
    return outra_variavel

def func2(arg):
    print(arg)

var = func()
func2(var)