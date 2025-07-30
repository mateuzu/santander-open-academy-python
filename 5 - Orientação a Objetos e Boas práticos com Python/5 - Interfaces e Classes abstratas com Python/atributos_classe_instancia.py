class Estudante:
    escola = "DIO" # Variável de classe
    
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero
    
    def __str__(self):
        return f"{self.nome} ({self.numero}) {self.escola}"


def mostrar_valores(*alunos):
    for aluno in alunos:
        print(aluno)

gui = Estudante ("Guilherme", 56451)
gi = Estudante ("Giovanna", 17323)
mostrar_valores(gui, gi)

gui.nome = "Novo nome"
mostrar_valores(gui, gi)