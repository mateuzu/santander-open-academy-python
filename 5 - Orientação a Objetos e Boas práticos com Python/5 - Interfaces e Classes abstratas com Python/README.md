# Interfaces e classes abstratas com Python

> Objetivo: Entender o que são interfaces e classes abstratas e como podemos utilizá-las com Python

---------------------------------------------------------------

## Variáveis de classe e variáveis de instância 

Todos os objetos nascem com o mesmo número de atributos de classe e de instância. Atributos de instância são diferentes para cada objeto (cada objeto tem uma cópia), já os atributos de classe são compartilhados entre os objetos.

- Toda variável de classe está declarada logo após a definição da classe. No exemplo abaixo, `escola` é uma variável de classe. As variáveis de classe são compartilhadas entre os objetos do mesmo tipo, o que significa que se ela for alterada, a alteração será aplicada para todos os objetos.
- Toda variável de instância é referenciada utilizando o `self`. As variáveis de instância (no exemplo, `nome` e `matricula`) são únicas para cada objeto. O que significa que se alguma alteração for realizada, irá se refletir somente no próprio objeto.
```py
class Estudante:
    escola = "DIO" # Variável de classe
    
    def __init__(self, nome, numero):
        self.nome = nome # Variável de instancia
        self.numero = numero # Variável de instancia
    
    def __str__(self):
        return f"{self.nome} ({self.numero}) {self.escola}"


def mostrar_valores(*alunos):
    for aluno in alunos:
        print(aluno)

gui = Estudante ("Guilherme", 56451)
gi = Estudante ("Giovanna", 17323)
mostrar_valores(gui, gi) 
>>> Guilherme (56451) DIO
    Giovanna (17323) DIO

gui.nome = "Novo nome" # Alterando variavel de instancia
mostrar_valores(gui, gi)
>>> Novo nome (56451) DIO # Alterou somente a do objeto
    Giovanna (17323) DIO

Estudante.escola("Nova escola") # Alterando a variavel de classe
mostrar_valores(gui, gi) 
>>> Guilherme (56451) Nova escola # Alterou de todos os objetos
    Giovanna (17323) Nova escola
```

------------------------------------------------------------------------------------

## Métodos de classe e métodos estático

- **Métodos de classe**: Métodos de classe estão ligados à classe e não ao objeto. Eles têm acesso ao estado da classe, pois recebem um parâmetro que aponta para a classe e não para a instância do objeto.

- **Métodos estáticos**: Um método estático não recebe um primeiro argumento explícito. Ele também é um método vinculado à classe e não ao objeto da classe. Este método não pode acessar ou modificar o estado da classe. Ele está presente em uma classe porque faz sentido que o método esteja presente na classe.

#### Diferença entre eles

- Um método de classe recebe um primeiro parâmetro que aponta para a classe, enquanto um método estático não.
- Um método de classe pode acessar ou modificar o estado da classe enquanto um método estático não pode acessá-lo ou modificá-lo.

#### Quanto utilizar método de classe ou estático
- Geralmente usamos o método de classe para criar *métodos de fábrica*.
  - Por exemplo, dentro da classe `Pessoa`: um método de fábrica para criar uma instância de `Pessoa` com base na data de nascimento. Vejamos no exemplo:
- Geralmente usamos métodos estáticos para criar funções utilitárias.
  - Por exemplo, dentro de classe `Pessoa`: uma função utilitária para verificar se a pessoa é maior de idade 

>Métodos de fábrica são métodos que retornam uma nova instância da classe.

### Exemplo - Método de classe
Vimos anteriormente que o método de classe é muito utilizado para criação de métodos de fábrica. Então vamos visualizar um exemplo prático: Criar pessoas com `nome` e `idade` a partir da data de nascimento.
```py
class Pessoa:
    
    def __init__(self, nome=None, idade=None): # Mecessario incluir o =None nos parametros do construtor
        self.nome = nome,
        self.idade = idade

    def criar_por_data_nascimento(self, ano, mes, dia, nome):
        idade = 2025 - ano
        return Pessoa(nome, idade)
    
teste = Pessoa().criar_por_data_nascimento(2002, 8, 31, "Mateus")
print(teste.nome, teste.idade)  
```
- `def __init__`: Já é sabido que podemos criar objetos a partir do construtor. Mas podemos tornar essa instancição mais dinâmica, através dos métodos de fábrica. Para que isso seja possível, é necessário atribuir o valor padrão `None` no construtor.
- `def criar_pessoa`: Esse é o método de fábrica do nosso exemplo. Irá retornar uma pessoa com base na data de nascimento e nome informados. Repare que ele utiliza o construtor de `Pessoa` para retornar a instância
- `teste = Pessoa().criar_pessoa`: Aqui, estamos instanciando um objeto através do método de fábrica, em seguida, exibindo suas informações. 

#### Porém, há um erro nessa abordagem! 🚨
- Repare que nesse trecho `Pessoa().criar_pessoa` estamos criando dois objetos de uma vez. Um objeto sem nenhum argumento `Pessoa()` para conseguir acessar o método `criar_pessoa`. Com isso, teremos dois objetos alocados na memória.

#### Solução correta ✅
- Devemos incluir o decorador `@classmethod` na assinatura do método `criar_pessoa`. Isso vai transformá-lo em um método de classe. Além disso, existe uma convenção de trocar `self` por `cls` quando é um método de classe. Isso porquê `self` é uma referência ao objeto, enquanto `cls` é uma referência à classe.
  - Como `cls` é uma referência à classe, não precisamos mais utilizar o construtor explícito de `Pessoa(nome, idade)`, basta utilizarmos o `cls(nome, idade)` que ele vai ativar o construtor da classe.
```py
@classmethod
def criar_pessoa(cls, ano, mes, dia, nome): # Troca self por cls
    idade = 2025 - ano
    cls(nome, idade) # utiliza cls no lugar do construtor explicito
```
- Com isso, não precisamos mais instanciar uma pessoa vazia para acessar o método, basta utilizar o nome da classe, exemplo: `Classe.método` 
```py
teste = Pessoa().criar_pessoa(2002, 8, 31, "Mateus") ❌ Troque isso
teste = Pessoa.criar_pessoa(2002, 8, 31, "Mateus") ✅ Por isso
```

**Código completo**
```py
class Pessoa:
    
    def __init__(self, nome=None, idade=None):
        self.nome = nome,
        self.idade = idade

    @classmethod
    def criar_pessoa(cls, ano, mes, dia, nome):
        idade = 2025 - ano
        return Pessoa(nome, idade)
    
teste = Pessoa.criar_pessoa(2002, 8, 31, "Mateus")
print(teste.nome, teste.idade)
```

### Exemplo - Método estático
Vimos anteriormente que o método estáticos é muito utilizado para funções utilitárias. Ainda no exemplo de pessoa, vamos criar um método estático para verificar se uma pessoa é maior de idade:
- Como já vimos o uso do decorador no exemplo acima, não tem muito segredo. Para criar um método estático, devemos usar o decorado `@staticmethod`
  - A função retorna `True` se a idade repassada for maior ou igual a 18
  - Repare como o método estático não carrega o parâmetro `self` na sua assinatura. Isso porquê o método estático não precisa do contexto à instância do objeto, ele é um método "independente".
- A sintaxe para chamar a função é muito parecida com o método de classe: `Classe.metodo_estatico`
```py
class Pessoa:
    
    def __init__(self, nome=None, idade=None):
        self.nome = nome,
        self.idade = idade

    #Método estatico
    @staticmethod
    def maior_idade(idade):
        return idade >= 18
    
print(Pessoa.maior_idade(18)) # True
print(Pessoa.maior_idade(17)) # False
```

>Dica: Se você precisar de acesso ao contexto da classe, utilize método de classe. Se você não precisa de contexto da classe, nem do objeto, utilize método estático.

----------------------------------------------------------------------------

## Interfaces

Em POO, Interfaces são um tipo especial de contrato ou esqueleto que define métodos e comportamentos que uma classe deve implementar, mas não fornece a implementação desses métodos. Ou seja, uma interface só diz o que uma classe deve fazer, mas não como ela deve fazer. A implementação do "como fazer" fica a cargo da classe que implementa a interface.

>Importante: Interfaces definem O QUE uma classe deve fazer, não COMO.
- Uma interface é uma forma de definir um padrão de implementação para todos que desejam implementar.

### Python tem interface?
O conceito de interface é definir um contrato, onde são declarados os métodos (o que deve ser feito) e suas respectivas assinaturas. Em Python utilizamos classes abstratas para criar contratos. **Classes abstratas não podem ser instanciadas.**

## Classes abstratas

Por padrão, o Python não fornece classes abstratas. O Python vem com um módulo que fornece a base para definir as classes abstratas, e o nome do módulo é `ABC` (Abstract Base Class). 

O `ABC` funciona decorando métodos da classe base como abstratos e, em seguida, registrando classes concretas como implementações da base abstrata. 

Um método se torna abstrato quando decorado com `@abstractmethod`.

### Exemplo
Nesse exemplo, vamos criar uma classe abstrata `ControleRemoto` com os métodos abstratos `ligar` e `desligar`. Essa classe representa um controle genérico, sem muitas especificações. As classes que herdarão (ou implementarão, se consideramos a classe como uma interface) terão que implementar esses métodos.

Vamos seguir essa estrutura:
- Vale ressaltar que ainda não estamos aplicando o conceito de classe abstrata, apenas mostrando a estrutura do código.
```py
class ControleRemoto:
    def ligar(self):
        pass

    def desligar(self):
        pass

class ControleTV(ControleRemoto):
    pass

class ControleArCondicionado(ControleRemoto):
    pass
```

#### Aplicando classes abstratas
- Antes de tudo, devemos realizar a importação do módulo `ABC` na primeira linha do código. Não se apegue a sintaxe pois veremos isso mais a frente no curso. `from abc import ABC` é a linha responsável por importar o módulo que nos permitirá criar classes abstratas
```py
from abc import ABC
```
- Em seguida, devemos informar que a nossa classe abstrata `ControleRemoto` herda de `ABC`. Além disso, devemos fazer com que os métodos `ligar` e `desligar` recebam o decorador `@abstractmethod` em suas assinaturas. A partir daí, a classe se torna abstrata e todas as outras classes que a implementam/herdam devem, obrigatoriamente, implementar seus métodos.
  - Em alguns casos, é necessário incluir o `abstractmethod` ao lado do import do `ABC` na 1° linha do código.
- Os métodos não possuem nenhuma lógica pois são métodos abstratos. Eles carregam somente a assinatura e a implementação fica a caráter de quem implementa a classe.
- Se executar o código como está (sem implementar o método abstrato em outras classes) o compilador irá informar um erro.
- Vale ressaltar que tentar instanciar a classe abstrata `ControleRemoto` também vai dar erro. Classes abstratas não podem ser instanciadas.
```py
from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    
    @abstractmethod
    def ligar(self): pass

    @abstractmethod
    def desligar(self): pass

class ControleTV(ControleRemoto):
    pass

class ControleArCondicionado(ControleRemoto):
    pass

controle_tv = ControleTV()
controle_tv.ligar() # ❌ Vai dar erro

controle_abstrato = ControleRemoto() # ❌ Vai dar erro - classe abstrata não podem ser instanciada
```
- Com a classe abstrata definida, é hora de realizar a implementação do método nas classes-filhas. Não tem nada especial, apenas retornamos uma mensagem específica para cada classe:
```py
class ControleTV(ControleRemoto):
    
    def ligar(self):
        print("Ligando TV....")
        print("TV LIGADA")

    
    def desligar(self):
        print("Desligando TV....")
        print("TV DESLIGADA")

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando Ar-condicionado....")
        print("AR-CONDICIONADO LIGADO")

    
    def desligar(self):
        print("Desligando Ar-condicionado....")
        print("AR-CONDICIONADO DESLIGADO")

# Agora os metodos podem ser executados
controle_tv = ControleTV()
controle_tv.ligar()
controle_tv.desligar()

controle_ar = ControleArCondicionado()
controle_ar.ligar()
controle_ar.desligar()
```

> A classe abstrata ajuda no polimorfismo, pois cada classe irá implementar o método de maneira individual, visto que a classe abstrata define somente a assinatura

#### abstractproperty
É possível utilizar `property` em classe abstratas. Para isso, devemos utilizar o decorador `@abstractmethod` e `@property` na definição da propriedade na classe abstrata. Assim como os métodos, a implementação de propriedades também é obrigatória para as classes-filhas. 

No exemplo abaixo, vamos criar uma propriedade `marca` na classe abstrata. É uma propriedade simples, apenas para retornar a marca do controle.

> Ao implementar a propriedade, as classes-filhas ainda devem manter o decorador `@property` na assinatura.

```py
from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    
    # Definição da propriedade na classe abstrata
    @property
    @abstractmethod
    def marca(self): pass

class ControleTV(ControleRemoto):

    # Implementação da propriedade na classe-filha
    @property
    def marca(self):
        print("SAMSUNG")

class ControleArCondicionado(ControleRemoto):

    # Implementação da propriedade na classe-filha
    @property
    def marca(self):
        print("BRASTEMP")

controle_tv = ControleTV()
controle_tv.marca # SAMSUNG

controle_ar = ControleArCondicionado()
controle_ar.marca # BRASTEMP
```

#### Código inteiro
Abaixo uma versão completa do código para ilustrar exemplos de classes abstratas con Python:
```py
from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractmethod
    def marca(self): pass

class ControleTV(ControleRemoto):
    
    def ligar(self):
        print("Ligando TV....")
        print("TV LIGADA")

    
    def desligar(self):
        print("Desligando TV....")
        print("TV DESLIGADA")

    @property
    def marca(self):
        print("SAMSUNG")

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando Ar-condicionado....")
        print("AR-CONDICIONADO LIGADO")

    
    def desligar(self):
        print("Desligando Ar-condicionado....")
        print("AR-CONDICIONADO DESLIGADO")

    @property
    def marca(self):
        print("BRASTEMP")

controle_tv = ControleTV()
controle_tv.ligar()
controle_tv.desligar()
controle_tv.marca

controle_ar = ControleArCondicionado()
controle_ar.ligar()
controle_ar.desligar()
controle_ar.marca
```