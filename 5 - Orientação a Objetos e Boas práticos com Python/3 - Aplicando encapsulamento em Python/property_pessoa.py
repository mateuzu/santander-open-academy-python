class Pessoa:
    def __init__(self, nome, sobrenome, ano_nascimento):
        self._nome = nome
        self._sobrenome = sobrenome
        self._ano_nascimento = ano_nascimento

    @property
    def nome_completo(self):
        return f"{self._nome} {self._sobrenome}"
    
    @property
    def idade(self):
        _ano_atual = 2025
        return _ano_atual - self._ano_nascimento

    
usuario = Pessoa("Mateus", "Ferreira", 2002)
print(usuario.nome_completo)
print("Idade:", usuario.idade)