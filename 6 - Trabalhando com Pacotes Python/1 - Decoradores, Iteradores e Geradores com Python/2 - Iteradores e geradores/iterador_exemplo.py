class DobrarNumero:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):
        return self
    
    # o método __next__ irá buscar pelo proximo elemento
    def __next__(self):
        try:
            numero = self.numeros[self.contador] * 2
            self.contador += 1
            return numero * 2
        except IndexError:
            raise StopIteration
        
for i in DobrarNumero(numeros=[2, 4, 6, 8]):
    print(i)