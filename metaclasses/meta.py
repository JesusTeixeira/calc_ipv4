class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)
        
        if 'b_fala' not in namespace:
            print(f'Oi, voce precisa criar o metodo b_fala em {name}')
        else:
            if not callable(namespace['b_fala']):
                print(f'b_fala precisa ser um metodo, nao atributo em {name}.')
        return type.__new__(mcs, name, bases, namespace)

class A(metaclass=Meta):
    def fala(self):
        self.b_fala()
        
        
class B(A):
    teste = 'Valor'
    b_fala = 'Wow'
    pass

    def sei_la(self):
        pass


