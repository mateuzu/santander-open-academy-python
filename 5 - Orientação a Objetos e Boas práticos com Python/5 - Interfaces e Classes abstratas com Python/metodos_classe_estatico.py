class Pessoa:
    
    def __init__(self, nome=None, idade=None):
        self.nome = nome,
        self.idade = idade

    #Método de classe
    @classmethod
    def criar_pessoa(cls, ano, mes, dia, nome):
        idade = 2025 - ano
        return Pessoa(nome, idade)
    
    #Método estatico
    @staticmethod
    def maior_idade(idade):
        return idade >= 18
    
teste = Pessoa.criar_pessoa(2002, 8, 31, "Mateus")
print(teste.nome, teste.idade)
print(Pessoa.maior_idade(18))
print(Pessoa.maior_idade(17))