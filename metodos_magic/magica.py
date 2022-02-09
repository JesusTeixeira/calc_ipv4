'''class A:
    def __new__(cls, *args, **kwargs):
        
        cls.nome = 'Jésus Douglas'
        
        return object.__new__(cls)
    
    
    def __init__(self):
        print('Eu sou o INIT')'''
        
'''     
class A:
    def __new__(cls, *args, **kwargs):
        
        def haha(*args, **kwargs):
            print('fala um OI')
            
        cls.haha = haha
        
        return object.__new__(cls)
    
    
    def __init__(self):
        print('Eu sou o INIT')'''
        
        
        
class A:
    def __new__(cls, *args, **kwargs):
        
        if not hasattr(cls, '_jaexiste'):
             cls._jaexiste = object.__new__(cls)
         
        return cls._jaexiste
    
    def __init__(self):
        print('Eu sou o INIT')