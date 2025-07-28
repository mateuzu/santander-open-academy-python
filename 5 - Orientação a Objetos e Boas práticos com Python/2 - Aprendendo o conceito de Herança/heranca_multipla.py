class Animal:
    def __init__(self, numero_patas):
        self.numero_patas = numero_patas

    def __str__(self):
        return f"{self.__class__.__name__}:{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

# Subgrupo de mamíferos
class Mamifero(Animal):
    # def __init__(self, cor_pelo, numero_patas):
    #     self.cor_pelo = cor_pelo
    #     super().__init__(numero_patas)
    
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

# Subgrupo de aves
class Ave(Animal):
    # def __init__(self, cor_bico, numero_patas):
    #     self.cor_bico = cor_bico
    #     super().__init__(numero_patas)
    
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)


# Animais mamíferos
class Cachorro(Mamifero):
    def latir(self):
        print("Au au au")

class Gato(Mamifero):
    def miar(self):
        print("Miau miau")

class Canguru(Mamifero):
    def pular(self):
        print("Pulando...")

# Animais aviários
class Aguia(Ave):
    def cacar(self):
        print("Caçando presa...")

# Ornitorrindo é Mamífero e Ave ao mesmo tempo
class Ornitorrinco(Mamifero, Ave):
    def botar_ovo(self):
        print(Ornitorrinco.mro())
        print("Botando ovo...")

    def nadar(self):
        print("Nadando")

# Intanciando objetos
bethoven = Cachorro(cor_pelo="Preto", numero_patas=4)
garfield = Gato(cor_pelo="Laranja", numero_patas=4)
canguru = Canguru(cor_pelo="Marrom", numero_patas=2)
aguia = Aguia(cor_bico="Amarelo", numero_patas=2)
ornitorrinco = Ornitorrinco(numero_patas=4, cor_pelo="Marrom", cor_bico="Cinza")

# Acessando os métodos de cada objetos
bethoven.latir()
print(bethoven)

garfield.miar()
print(garfield)

canguru.pular()
print(canguru)

aguia.cacar()
print(aguia)

ornitorrinco.botar_ovo()
print(ornitorrinco)