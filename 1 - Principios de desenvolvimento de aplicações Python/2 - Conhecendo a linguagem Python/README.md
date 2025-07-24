# Conhecendo a linguagem

## Tipos de dados
Os tipos servem para definir as caracteristicas comportamentos de um valor (objeto) para o interpretador.

Por exemplo:
- Com esse tipo eu sou capaz de realizar operações matemáticas.
- Esse tipo para ser armazenado em memória irá consumir 24 bytes.

#### Tipos built-in
Os tipos built-in são:

| | |
|-|-|
|Texto|str|
|Numérico|int, float, complex|
|Sequência*|list, tuple, range|
|Mapa*|dict|
|Coleção*|set, frozenset|
|Booleano|bool|
|Binário|bytes, bytearray, memoryview|
- Sequência: Uma sequencia de valores não ordenados (pode ser texto, números, etc)
- Coleção: Semelhante a sequência de valores, porém não permite elementos duplicados
- Mapa: Conjunto de chave-valor

#### Tipos numéricos
- **int**: Números inteiros são representados pela classe int e possuem precisão ilimitada. São exemplos válidos de números inteiros: 1, 10, 100, -1, -10, -100...99001823
- **float**: Os números de ponto flutuante são usados para representar os números racionais e sua implementação é feita pela classe float. São exemplos válidos de números de ponto flutuante: 1.5, -10.543, 0.76...999278.002
- **complex**:

#### Tipos booleanos e strings
- **bool**: É usado para representar verdadeiro ou falso, e é implementado pela classe bool. Em Python o tipo booleano é uma subclasse de int, uma vez que qualquer número diferente de 0 representa verdadeiro e 0 representa falso. São exemplos válidos de booleanos: True e False
- **strings**:Strings ou cadeia de caracteres são usadas para representar valores alfanúmericos, em Python as strings são definidas utilizando a classe str. São exemplos válidos de string: "Python", 'Python', """Python""", '''Python''', "p" (repare que é possível declarar uma string utilizando aspas simples ou duplas)

## Modo interativo

O interpretador Python pode executar em modo que possibilite o desenvolvedor a escrever código, e ver o resultado na hora.

Existem duas formas de iniciar o modo interativo, ambos através do terminal
- `python`
- `python -i <nome_arquivo.py>`: Permite manipular as variaveis/funções existentes no arquivo aberto

```py
$ python
Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 19 + 11
30
>>> "Mateus" + " Ferreira"
'Mateus Ferreira' 
```
- Para sair do modo interativo: `exit()`

#### Função dir
Sem argumentos, retorna a lista de nomes no escopo local atual. Com um argumento, retorna uma lista de atributos válidos para o objeto. 

Exemplos:
- `dir()`: Nesse caso, vamos mostrar todos os módulos que o escopo local utiliza. Para fins de teste, vamos importar o módulo `math` para visualizar como ele é adicionado
```bash
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
>>> import math #Importando o math no escopo local para que possamos visualiza-lo no comando dir()
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'math']
```
- `dir(100)`: Nesse caso, vamos mostrar todos os métodos que podem ser utilizados pela classe `int` (pois estamos passando um int como parâmetro).
```bash
>>> dir(100)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
```

#### Função help
Invoca o sistema de ajuda integrado. É possível fazer buscas em modo interativo ou informar por parâmetro qual o nome do módulo, função, classe, método ou variável. 
Basicamente, é uma documentação offline.

Exemplos:
- `help()`: Aqui, vamos visualizar toda a documentação da classe `int`  
```bash
>>> help()

Welcome to Python 3.11's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the internet at https://docs.python.org/3.11/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> int
Help on class int in module builtins:

class int(object)
 |  int([x]) -> integer
 |  int(x, base=10) -> integer
 |
 |  Convert a number or string to an integer, or return 0 if no arguments
 |  are given.  If x is a number, return x.__int__().  For floating point
 |  numbers, this truncates towards zero.
 |
-- Mais  --
```

>Para usar a função help e dir em um objeto customizado, é importante que este tenha uma documentação organizada.

## Variáveis e constantes

Em linguagens de programação podemos definir valores que podem sofrer alterações no decorrer da execução do programa. Esses valores recebem o nome de variáveis, pois eles nascem com um valor e não necessariamente devem permanecer com o mesmo durante a execução do programa.

```py
age, name = (23, 'Mateus')
print(f'Meu nome é {name} e eu tenho {age} anos(s) de idade')
>>> Meu nome é Mateus e eu tenho 23 ano(s) de idade.
```

Perceba que não precisamos definir o tipo de dados da variável, o Python faz isso automaticamente para nós. Por isso não podemos simplesmente criar uma variável sem atribuir um valor. Para alterar o valor da variável basta fazer uma atribuição de um novo valor:
```py
age, name = (23, 'Mateus')
print(f'Meu nome é {name} e eu tenho {age} anos(s) de idade')
>>> Meu nome é Mateus e eu tenho 23 ano(s) de idade.

age = 40
name = 'Novo nome'
print(f'Meu nome é {name} e eu tenho {age} anos(s) de idade')
>>> Meu nome é Novo Nome e eu tenho 40 ano(s) de idade.
```

#### Constante
Assim como as variáveis, constantes são utilizadas para armazenar valores. Uma constante nasce com um valor e permanece com ele até o final da execução do programa, ou seja, o valor é imutável.

Não existe uma palavra reservada para informar ao interpretador que o valor é constante. Em algumas linguagens por exemplo: Java e C utilizamos `final` e `const`, respectivamente para declarar uma constante.

Em Python usamos a convenção que diz ao programador que a variável é uma constante. Para fazer isso, você deve criar a variável com o nome todo em letras maíusculas:
- Exemplos de constantes:
```py
ABS_PATH = '/home/user/Documents/python_course'
DEBUG = True
STATES = [
    'SP',
    'RJ',
    'MG'
]
AMOUNT = 30.2
```

>Vale ressaltar que isso NÃO impede a modificação do valor. O interpretador considera isso como uma variável normal, portanto ele troca o valor normalmente. Isso é apenas uma conveção que os desenvolvedores adotaram para conseguir identificar constantes no código e evitar modifica-las 

#### Boas práticas
- O padrão de nomes deve ser snake case (todo espaço em branco é substituído por _)
- Escolher nomes sugestivos
    - Não use abreviações. Prefira nomes grandes e declarativos do que abreviações sem sentido
- Nome de constantes todo em maísculo

```py
nome = 'Mateus'
idade = 22

print(nome, idade)

nome, idade = ("Nome alterado", 20) # É possível atribuir valor a duas variaveis ao mesmo tempo

print(nome, idade)

limite_saque_diario = 1000
padrao_snake_case = 'Esse é o padrão Snake Case'

ESTADOS_BRASILEIROS = ["SP", "RJ", "ES", "MG"]

print(ESTADOS_BRASILEIROS)

---------------------------RESULTADO---------------------------
Mateus 22
Nome alterado 20
['SP', 'RJ', 'ES', 'MG']
```

## Conversão de tipos

Em alguns momentos é necessário será necessário converter o tipo de uma variável para manipular de forma diferente. Por exemplo:
Variáveis do tipo `string`, que armazenam números e precisamos fazer alguma operação matemática com esse valor.

>Basicamente, o padrão para formatar um número é utilizando o construtor do tipo desejado. Sendo assim, para converter um valor `x` para inteiro, basta: `int(x)`

#### Inteiro para float
```py
preco = 10
print(preco)
>>> 10

# Inteiro para float
preco = float(preco)
print(preco)
>>> 10.0
```


#### Float para inteiro
```py
preco = 10.0
print(preco)
>>> 10.0

# Float para inteiro
preco = int(preco)
print(preco)
>>> 10
```

#### Conversão por divisão
- `int -> float`: Podemos simplesmente dividir o valor inteiro para convertê-lo em float
- `int -> int`: Para preservar o valor inteiro em uma divisão entre 2 inteiros, podemos utilizar 2 barras `//` 
```py
preco = 10
print(preco)
>>> 10

print(preco / 2)
>>> 5.0

print(preco // 2)
>>> 5
```

#### Numérico para string
```py
preco = 10.50
idade = 28

print(str(preco))
>>> 10.5

print(str(idade))
>>> 28

texto = f"idade {idade} preco {preco}"
print(texto)
>>> idade 28 preco 10.5
```

#### String para número
```py
preco = "10.50"
idade = "28"

print(float(preco))
>>> 10.50

print(int(idade))
>>> 28
```

#### Erro de conversão

Nem sempre da para realizar a conversão de tipos. 
Por exemplo, conversão de string para float podem resultar em erro.

## Função de entrada e saída

#### Função input
A função builtin `input` é utilizada quando queremos ler dados da entrada padrão (teclado). Ela recebe um argumento do tipo string, que é exibido para o usuário na saída padrão (tela). A função lê a entrada, converte para string e retorna o valor.

- Nesse exemplo abaixo, ele exibe a mensagem Informe seu nome: e espera um valor como resposta. Esse valor será atribuído a variavel `nome`
```py
nome = input("Informe seu nome: ")
>>> Informe seu nome 
```

#### Função print
A função builtin print é utilizada quando queremos exibir dados na saída padrão (tela). Ela recebe um argumento obrigatório do tipo `varargs` de objetos e 4 argumentos opcionais (sep, end, file e flush). Todos os objetos são convertidos para string, separados por sep e terminados por end. A string final é exibida para o usuário.
- No exemplo abaixo, vamos mostrar alguns exemplos de saída utilizando a função print:
    - 1°: Nesse exemplo, apenas chamamos as duas string (nome e sobrenome) para saida no console. O resultado padrão é a separação entre as strings por um espaço em branco
    - 2°: Nesse exemplo, vamos modificar o final da saída com o parâmetro `end`. Por padrão, o final de uma saída é uma quebra de linha. Nesse caso, vamos adicionar `...`, juntamente com a quebra de linha
    - 3°: Nesse exemplo, vamos modificar o separador padrão com o parâmetro `sep`. Por padrão, o separador é um espaço em branco (separando uma palavra da outra). No exemplo, vamos trocar o espaço em branco pelo #
```py
nome = "Mateus"
sobrenome = "Ferreira"

#1°
print(nome, sobrenome)
>>> Mateus Ferreira

#2°
print(nome, sobrenome, end="...\n")
>>> Mateus Ferreira...

#3°
print(nome, sobrenome, sep="#")
>>> Mateus#Ferreira
```