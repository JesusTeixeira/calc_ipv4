from banco import Banco
from cliente import Cliente
from conta import ContaCorrente, ContaPoupanca

banco = Banco()

cliente1 = Cliente('JD', 30)
cliente2 = Cliente('Joao Baptista', 60)
cliente3 = Cliente('Chichica', 65)

conta1 = ContaPoupanca(1111, 234532, 0)
conta2 = ContaCorrente(2222, 234537, 0)
conta3 = ContaPoupanca(1212, 234534, 0)


cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

banco.inserir_cliente(cliente1)
banco.inserir_conta(conta1)


banco.inserir_cliente(cliente2)
banco.inserir_conta(conta2)


if banco.autenticar(cliente1):
    cliente1.conta.depositar(0)
    cliente1.conta.sacar(20)
else:
    print('Cliente não autenticado.')
    
print('###' * 10)

if banco.autenticar(cliente2):
    cliente2.conta.depositar(0)
    cliente2.conta.sacar(20)
else:
    print('Cliente não autenticado.')
    