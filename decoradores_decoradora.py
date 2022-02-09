def fala_oi():  #funcao#
    print('oi')

variavel = fala_oi  #variavel recebe funcao#

print(type(variavel))

print('*' * 10)


def master():
    def slave():
        print('oi')
        
    slave()
    
master()