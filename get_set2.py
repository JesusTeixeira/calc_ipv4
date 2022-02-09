class Pessoa:
    def __init__(self):
        #self.atributo = 'inicial'
        self._nome = 'inicial'
    
    @property
    def nome(self):
        #return 'jesus douglas'
        return self._nome
    
    
    @nome.setter
    def nome(self, nome):
        #self.atributo = nome
        self._nome = nome



p1 = Pessoa()
p1.nome = 'Froodo'
print(p1.nome)