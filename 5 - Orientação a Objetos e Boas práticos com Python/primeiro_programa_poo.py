class Bicicleta:

    # Construtor para inicializar um objeto
    # self: referência explicita para o objeto | semelhante ao this do Java
    def __init__(self, cor_construtor, modelo_construtor, ano_construtor, valor_construtor):
        self.cor = cor_construtor
        self.modelo = modelo_construtor
        self.ano = ano_construtor
        self.valor = valor_construtor
    
    def buzinar(self):
        print("Plim Plim...")

    def parar(self):
        print("Parando bike...")
        print("Bike parada")

    def correr(self):
        print("Vruuuum....")

    # Método sem self = errado
    def trocar_marcha(numero_marcha):
        print(numero_marcha)
        print("Marcha trocada...")

    # Método sem self = errado
    def drift():
        print("Drift...")

    # def __str__(self):
    #     return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"

    # Retornando os valores do atributo do objeto instanciado de maneira dinamica
    # Se um novo atributo for adicionado, ele será mapeado por essa estrutura
    def __str__(self):
        return f"{self.__class__.__name__}: {','.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

# instanciado objeto
primeira_bicicleta = Bicicleta("vermelha", "caloi", 2022, 600)

# executando métodos
primeira_bicicleta.buzinar()
primeira_bicicleta.correr()
primeira_bicicleta.parar()
Bicicleta.buzinar(primeira_bicicleta) # também é possível executar os métodos dessa forma 

#Exibindo atributos do objeto
print(primeira_bicicleta.cor, primeira_bicicleta.modelo, primeira_bicicleta.ano, primeira_bicicleta.valor)

# retorna uma representação string do objeto - semelhante: toString()
print(primeira_bicicleta)