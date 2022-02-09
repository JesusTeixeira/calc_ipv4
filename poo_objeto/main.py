from pessoa import Pessoa


p1 = Pessoa('Luiz', 28)
#p2 = Pessoa('lucas', 24)

p1.comer('maça')
p1.falar('POO')
p1.parar_comer()
p1.falar('POO')
p1.comer('alimento')
p1.parar_falar()
p1.falar('assunto')

print(p1.get_ano_nascimento())