class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor...")

    def __str__(self):
        return f"{self.__class__.__name__}:{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Carro(Veiculo):
    pass

class Moto(Veiculo):
    pass

class Caminhao(Veiculo):

    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não' "estou carregado"}")

civic = Carro("Preto", "ABC-1234", 4)
civic.ligar_motor()

honda = Moto("Vermelha", "ABC-0001", 2)
honda.ligar_motor()

caminhao = Caminhao("Prata", "ABC-1000", 6)
caminhao.ligar_motor()
caminhao.esta_carregado()