# Introdução à Programação Orientada a Objetos com Python

Conhecer o paradigma de programação orientada a objetos com Python.

## O que é Orientação a Objetos

Antes de falarmos de POO, vamos falar sobre **paradigmas de programação**

#### Paradigmas de programação

Um paradigma de programação é um estilo/modelo e programação. Não é uma linguagem (Python, Java, C, etc), e sim a forma como você soluciona os problemas através do código.

>Exemplo: Problema - bebar água
- Solução 1: Usar um copo para beber água
- Solução 2: Usar uma garrafa para beber água

**Alguns paradgimas famosos**
- Imperativo ou procedural
- Funcional
- Orientado a eventos

### Programação Orientada a Objetos

O paradigma de programação orientada a objetos estrutura o código abstraindo problemas em objetos do mundo real, facilitando o entendimento do código e tornando-o mais modular e extensível. Os dois conceitos chaves para aprender POO são: *classes* e *objetos*.

O paradigma de POO ganhou muita notoriedade pela capacidade de aproximar um problema computacional com soluções e objetos da vida real.

> Por exemplo: Imagine que você queira desenvolver um programa para gravar produtos vendidos em um supermercado. 
- Com orientação a objetos, é possível criar classes/objetos que irão mapear os produtos dentro do sistema. 
- Classe: Na classe, podemos definir as características do produto (nome, preço, fabricante, valor, etc). Essas características vão na especificação da classe, por isso ela determina atributos comuns de um produto (ou seja, algo que todos produtos possuem)
- Objeto: Enquanto um objeto (bolacha, farinha, refrigerante) seria um produto específico. O objeto é uma instância da classe, então ele atribui características específicas a ele usando a classe como base/molde.

--------------------------------------------------------------------

## Classe e objetos

>Objetivo: Aprender a utilizar classes e objetos com Python

- Classe: Uma classe define as características (atributos) e comportamentos (métodos) de um objeto, porém não conseguimos usá-las diretamente. 
- Objetos: Já os objetos podemos usá-los e eles possuem as características e comportamentos que foram definidos nas classes.

>Por exemplo: Vamos imaginar a construção de uma casa.
- Classe: Nesse exemplo, a classe pode ser comparada como a planta. Essa planta vai definir as características da casa (quantidade de quartos, posição do banheiro, hall de entrada, etc)
- Objeto: Ainda nesse exemplo, um objeto pode ser comparado à casa construída, tendo usado a planta (classe) como base para sua construção.

> Vamos visualizar no código:
- Classe: Essa classe define propriedades (características e comportamentos) de um cachorro. Repare como os atributos são *generalistas* como nome, cor e se está acordado. É importante usar atributos que são gerais, ou seja, que todos possuam.
- Vale ressaltar que o atributo `acordado` tem um valor padrão definido (`True`). Sendo assim, se esse parâmetro não for repassado pelo usuário, o valor padrão será utilizado
```py
class Cachorro:
    def _init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        print("Auau")
    
    def dormir(self):
        self.acordado = False
        print("Zzzzz...")
```
- Objeto: O objeto é uma instância construída da classe. Aqui, somos mais específicos na sua definição. Então, para o nosso exemplo, o atributo `nome` recebe o nome de um cachorro específico, a cor idem.
```py
cao_1 = Cachorro ("chappie", "amarelo", False) # Criando objeto com os valores
cao_2 = Cachorro ("Aladim", "branco e preto") # Nesse caso, acordado irá receber o valor padrão que é igual a True

cao_1.latir()

print(cao_2.acordado)
cao_2.dormir()
print(cao_2.acordado)
```

-----------------------------------------------------------------

## Criando seu primeiro programa com POO

João tem uma bicicletaria e gostaria de registrar as vendas de suas bicicletas. Crie um programa onde João informe: cor, modelo, ano e valor da bicicleta vendida. Uma bicicleta pode: buzinar, parar e correr. Adicione esses comportamentos!

**Código**
```py
class Bicicleta:

    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
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

    def __str__(self):
        return f"{self.__class__.__name__}: {','.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

# instanciado objeto
primeira_bicicleta = Bicicleta("vermelha", "caloi", 2022, 600)

# executando métodos
primeira_bicicleta.buzinar()
primeira_bicicleta.correr()
primeira_bicicleta.parar()
Bicicleta.buzinar(primeira_bicicleta) # também é possível executar os métodos dessa forma 

print(primeira_bicicleta.cor, primeira_bicicleta.modelo, primeira_bicicleta.ano, primeira_bicicleta.valor)

print(primeira_bicicleta)
```
Para que não fique muito confuso, vamos explicar cada trecho.

#### Declarando a classe
Para declarar uma classe, seguimos uma estrutura semelhante a de função, sendo: `class Nome:`. Tudo que estiver abaixo dessa declaração e seguindo a identação, fará parte da classe. 
```py
class Bicicleta:
    # Aqui dentro, as declarações fazem parte da classe

# Fora, as declarações NÃO fazem parte da classe

```

#### Construtor
Em python, temos o conceito de iniicalizador (ou construtor) veremos sobre isso mais a frente, mas de forma resumida: Um construtor é um "método" que instancia um objeto. Nesse caso, quando precisarmos criar uma `Bicicleta`, é este método `__init__` que será executado.
- Um construtor pode ou não receber atributos que serão utilizados na construção do objeto. Nesse caso, estamos definindo os atributos `cor, modelo, ano, valor`.
  - O `self` NÃO é um parâmetro que devemos passar ao criar objetos. Ele é uma referência explicita ao objeto. Ou seja, quando fazemos `self.cor = cor`, é como dizer: "A cor desse objeto será a cor que está vindo do construtor". Para ficar mais claro:
    - `self.cor`: Está se referindo ao atributo cor do objeto `Bicicleta`
    - `=` Operador de atribuição
    - `cor`: Parâmetro do construtor. Iremos repassar esse parâmetro para criar objetos
>Vale ressaltar que o *self não precisa ser nomeado assim, mas isso é uma boa prática
```py
def __init__(self, cor, modelo, ano, valor):
    self.cor = cor
    self.modelo = modelo
    self.ano = ano
    self.valor = valor
```

>Você pode renomear os atributos do parâmetro para algo como `cor_construtor` e, em seguida, utilizá-lo após o operador `=` para que fique mais claro qual variável é do objeto e qual vem do construtor. Mas o padrão é utilizar o mesmo nome
```py
def __init__(self, cor_construtor, modelo_construtor, ano_construtor, valor_construtor):
    self.cor = cor_construtor
    self.modelo = modelo_construtor
    self.ano = ano_construtor
    self.valor = valor_construtor
```

#### Métodos
Os métodos de uma classe são funções que executam uma determinada operação.
>Um erro comum em Python é criar métodos sem passar o `self`
- Importante ressaltar que os métodos devem receber o atributo `self` para que seja feita uma referência ao próprio objeto. Com essa referência, podemos mostrar uma propriedade do objeto, como por exemplo o método `__str__`.
  - O método `__str__` é uma forma de retornar as propriedades do objeto. É como se fosse um "resumo" do objeto e seus atributos. Existem 2 maneiras de fazer isso:
    - **Manualmente**: Nessa maneira, retornamos uma string com os atributos sendo mapeados manualmente. Uma desvantagem é que se adicionarmos outro atributo à classe, devemos modificar esse método para adicioná-lo
    - **Dinamicamente**: Nessa maneira, acessamos os atributos do objeto utilizando o método `self.__dict__.items()`, que retorna um dicionário dos atributos declarados. Uma vantagem dessa estrutura é que se um novo atributo for adicionado, não é necessário alterar o método, pois ele será mapeado dinamicamente.
    - Esse método é útil para retornar as informações do objeto de maneira organizada. Ao executar algo como `print(objeto)`, esse método será executado (mesmo sem chamá-lo explicitamente).
- Um método sem `self` pode resultar em dois problemas:
  - Se eu declarar um atributo, mas não declarar o `self`, o Python vai considerar esse atributo como sendo o `self`. Isso pode gerar diversas confusões, principalmente se você precisar utilizar essa variável no exemplo 
  - Se eu NÃO declarar o `self`, o compilador nem executa o código (caso o método seja chamado em alguma parte do programa)
>No trecho abaixo, eu ocultei a declaração da classe para não deixar muito grande. Mas é de suma importância que esses métodos fiquem "dentro" da declaração da classe. Atente-se à identação
```py
# Ocultei a declaração da classe para não ficar muito grande
def buzinar(self):
    print("Plim Plim...")

def parar(self):
    print("Parando bike...")
    print("Bike parada")

def correr(self):
    print("Vruuuum....")

# 1° Self declarado com outro nome = errado -> O Python vai achar que numero_marcha é o self
def trocar_marcha(numero_marcha): 
    print(numero_marcha) # Nesse caso, ele vai exibir o próprio objeto, pois ele acha que numero_marcha == self
    print("Marcha trocada...")

# 2° Self não declarado = errado -> Nesse caso, da erro de compilação pois self é obrigatório
def drift():
    print("Drift...")

# 1° Maneira: Atributos retornados manualmente
def __str__(self):
    return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"

# 2° Maneira: Atributos retornados dinamicamente
def __str__(self):
    return f"{self.__class__.__name__}: {','.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
``` 

#### Instanciar um objeto
Uma vez que o construtor foi criado e a classe teve seus métodos definidos, podemos instanciar um objeto. 
- Para utilizar o construtor e criar um objeto, devemos repassar esses valores utilizando `Bicicleta("", "", 0, 0)` (aqui eu utilizei valores nulos só para exemplificar) para uma variável, que será um objeto.
```py
class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

        # Métodos aqui embaixo

#minha_bike é um objeto   cor    modelo   ano  valor
minha_bike = Bicicleta("Amarela", "BMX", 2000, 450) # repare como o 'self' não é um atributo que é repassado
```

#### Acessando os métodos
Uma vez que um objeto foi instanciado, podemos acessar os métodos/comportamentos que foram definidas na clase. Temos duas formas de fazer isso:
- **Utilizando o objeto**: Nessa maneira, vamos utilizar o objeto criado para acessar os métodos seguindo essa estrutura: `objeto.metodo()`.
- **Utilizando a classe**: Dessa maneira, podemos utilizar a classe e repassar um objeto instanciado como parâmetro. Isso dá certo porque todos os métodos devem ter um `self` como parâmetro, ou seja, todos os métodos tem uma referência para o próprio objeto. Quando passamos um objeto no parâmetro, ele será utilizado para executar o método
```py
minha_bike = Bicicleta("Amarela", "BMX", 2000, 450)

minha_bike.buzinar() # Utilizando o objeto
Bicicleta.buzinar(minha_bike) # Utilizando a classe
```

>Como o acesso à métodos é muito parecido com atributos, não vou criar um tópico para isso. Mas a título de informação: Para acessar os atributos do objeto, podemos seguir a mesma estrutura de `objeto.atributo`. Então, se eu quiser exibir o ano da minha bicicleta, posso fazer isso: `minha_bike.ano`

---------------------------------------------------------------

## Construtores e destrutores

>Objetivo: Entender o conceito de construtor e destrutor. 

#### Método construtor

O método construtor sempre é executado quando uma nova instância da classe é criada. Nesse método inicializamos o estado do nosso objeto. 

Para declarar o método construtor da classe, criamos um método com o nome `__init__`.

```py
class Cachorro:
    def _init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
```

#### Método destrutor

O método destrutor sempre é executado quando uma instância (objeto) é destruída. Destrutores em Python não são tão necessários quanto em C++ porque o Pyton tem um coletor de lixo que lida com o gerenciamento de memória automaticamente. 

>Um coletor de lixo é um componente que mapeia os objetos do código a fim de desacolá-los da memória quando não estiverem mais em uso. O Python possui todo um mecanismo interno de gerenciamento de memóriam onde utiliza um contador de referência para descobrir se um objeto ainda está sendo utilizado ou se pode ser removido. 

Para declarar o método destrutor da classe, criamos um método com o nome `__del__`.

>Vimos que o Python possui um coletor de lixo que faz essa liberação de memória automaticamente, sendo assim, para quê utilizar o método `__dek__`?
- O método destrutor é muito útil quando você quer realizar alguma ação ANTES do objeto ser destruído. Com isso, podemos definir o método `__del__` com a implementação de algum código dentro do seu bloco

```py
class Cachorro:
    def __del__(self):
        print("Destruindo a instância")

dalmata = Cachorro()
del dalmata # Destruindo a instância
```

