class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False    #_ligado fica oculto e nao aparece instanciado
        
        
    def ligar(self):
        if self._ligado:
            return
        self._ligado = True
        
    
    def desligar(self):
        if not self._ligado:
            return           # o return nao permite o resto do codigo ser executado
        self._ligado = False
        
        
        