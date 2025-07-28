class Foo:
    def __init__(self, numero=None):
        self._numero = numero

    @property
    def numero(self):
        return self._numero or 0
    
    @numero.setter
    def numero(self, valor):
        _numero = self._numero or 0
        _valor = valor or 0
        self._numero = _numero + _valor

    @numero.deleter
    def numero(self):
        self._numero = -1

foo = Foo(10)
print(foo.numero)
foo.numero = 10
print(foo.numero)
del foo.numero
print(foo.numero)