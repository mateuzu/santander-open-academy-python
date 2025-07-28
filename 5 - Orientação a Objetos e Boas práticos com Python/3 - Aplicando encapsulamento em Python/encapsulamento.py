class Conta:
    def __init__(self, numero_agencia, saldo=0):
        self._saldo = saldo
        self.numero_agencia = numero_agencia

    def depositar(self, valor):
        #...
        self._saldo += valor

    def sacar(self, valor):
        #...
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo


conta = Conta("0001", 100)

# Isso será executado pelo compilador, mas NAO deve ser feito
# print(conta._saldo)
# conta._saldo += 100

conta.depositar(100)
print(conta.mostrar_saldo())