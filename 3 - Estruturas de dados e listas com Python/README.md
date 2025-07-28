# Trabalhando com listas em Python

Conhecer a estrutura de dados listas em Python, bem como seus métodos úteis.

------------------------------------------------------------------------------------------------------------------

## Lista: Criação e acesso aos dados

Listas em Python podem armazenar de maneira sequencial qualquer tipo de objeto. Podemos criar listas das seguintes maneiras: 
- utilizando o construtor list
- utilizando a função range
- colocando valores separados por vírgula dentro de colchetes. 

Listas são objetos mutáveis, portanto podemos alterar seus valores após a criação.

#### Criando listas
Nos exemplos abaixo, vemos que existe diversas maneiras de criar listas.
1. Criando uma lista colocando valores separados por vírgula dentro de colchetes. Esse método é o mais usual
2. 
```py
1.lista_com_colchetes = ["Laranja", "Maçã", "Uva"]
2.lista_vazia = []
3.lista_com_construtor = list("python") #Nesse caso, ele irá armazenar cada letra da palavra python dentro da lista
4.lista_com_range = list(range(10)) #Nesse caso, irá adicionar os números de 0 à 9
5.lista_diversos = ["Ferrari", "F8", 420000, 2020, 2900, "São Paulo", True]
```

#### Acesso direto
A lista é uma sequência, portanto podemos acessar seus dados utilizando índices. Contamos o índice de determinada sequência a partir do zero.

Imagine que os índices da lista são pequenos espaços onde poderemos alocar nossas variáveis. O 0 é o primeiro índice.
```
|0|1|2|3|4|5|
```

Para acessar diretamente uma posição, basta utilizarmos a sintaxe: `lista[i]`, onde:
- `lista` é a lista que você irá realizar o acesso
- `[i]`: é a posição/índice do elemento

**Exemplo**
```py
         #  [0]        [1]    [2]
frutas = ["Laranja", "Maçã", "Uva"]
frutas[0] # Laranja
frutas[1] # Maçã
```

>Vale ressaltar que as sequências em Python suportam indexação negativa. A contagem começa em -1
- Não importa quantos elementos existem na lista, `-1` sempre irá capturar o último elemento
```py
         #  [0]        [1]    [2]
frutas = ["Laranja", "Maçã", "Uva"]
frutas[-1] # Uva
frutas[-2] # Maçã
```

#### Listas aninhadas

Listas podem armazenar todos os tipos de objetos Python, portanto podemos ter listas que armazenam outras listas. Com isso podemos criar estruturas bidimensionais (tabelas), e acessar informando os índices de linha e coluna. Esse conceito é compreendido como matriz.

- As linhas correspondem aos elementos na horizontal. No exemplo abaixo, `a|b|c` correspondem a uma linha. `1|2|3` correspondem a outra e assim sucessivamente.
- As colunas correspondem aos elementos na vertical. No exemplo abaixo, `a|1|d` correspondem a uma coluna.

```txt
| a | b | c |
| 1 | 2 | 3 |
| d | e | f |
```

- Para criar uma matriz...
- Para acessar os elementos da matriz, podemos seguir o mesmo conceito de `matriz[posicao]`, a diferença é que agora podemos repassar também a linha/coluna para acessar um índice diretamente, ou seja, `matriz[linha][coluna]` (o primeiro indice sempre é a linha). 
  - `matriz[0]`: Captura a primeira linha
  - `matriz[0][0]`: Captura o elemento que está na primeira linha e na primeira coluna
  - `matriz[0][-1]`: Captura o elemento que está na primeira linha e última coluna
  - `matriz[-1][-1]`: Captura o elemento que está na última linha e última coluna
```py
matriz = [
  [1, "a", 2], 
  ["b", 3, 4],
  [6, 5, "c"]
]

matriz[0] #[1, "a", 2]
```

#### Fatiamento
Além de acessar elementos diretamente, podemos extrair um conjunto de valores de uma sequência. Para isso basta passar o índice inicial e/ou final para acessar o conjunto. Podemos ainda informar quantas posições o cursor deve "pular" no acesso.

>O fatiamento de listas é semelhante ao fatiamento de strings. 

```py
lista = ["p", "y", "t", "h", "o", "n"]

lista[2:] # ["t", "h", "o", "n"]
lista[:2] # ["p", "y"]
lista[1:3] # ["y", "t"]
lista[0:3:2] # ["p", "t"]
lista[::] # ["p", "y", "t", "h", "o", "n"]
lista[::-1] # ["n", "o", "h", "t", "y", "p"]
```

#### Iterar listas

A forma mais comum para percorrer os dados de uma lista é utilizando o comando `for`.
- Para ficar mais fácil entender esse laço, podemos ler o comando como: `para cada item presente em sequencia`, execute o comando dentro do bloco.
```py
carros = ["gol", "celta", "palio"]

# Leia-se: para cada carro em carros
for carro in carros:
  print(carro)
```

#### Função enumerate

Às vezes é necessário saber qual o índice do objeto dentro do laço for. Para isso podemos usar a função enumerate.

Para usar o `enumerate`, devemos seguir essa estrutura:
```py
for indice, item in enumerate(sequencia)
```
**Exemplo**
- O `enumerate` espera um iterável como parâmetro, nesse caso a lista
- Ele retorna um contador/indice (que inicia em 0) e o item da iteração
```py
carros = ["gol", "celta", "palio"]

for indice, carro in enumerate(carros):
  print(f"{indice}: {carro}")
```

### Compressão de lista
A compreensão de lista oferece uma sintaxe mais curta quando você deseja: criar uma nova lista com base nos valores de uma lista existente (filtro) ou gerar uma nova lista aplicando alguma modificação nos elementos de uma lista existente.

#### Criar uma nova lista com base em uma existente 
> Por exemplo, imagine que você tenha uma lista de número diversos e gostaria de filtrá-los para uma nova lista somente de números pares.

**Filtro versão 1**
Sem utilizar a compressão de lista, podemos fazer isso dessa maneira:
- Repare como temos que criar uma nova lista vazia (pares) para adicionar os números posteriormente
```py
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
  if numero % 2 == 0:
    pares.append(numero)
```

**Filtro versão 2**
Utilizando a compressão de lista, podemos fazer isso sem a necessidade de criar um laço explicito. De início essa maneira parece mais complicada, mas vamos destrichar:
- A 1° parte da compressão é o retorno da operação (`numero`), ou seja, o que vai compor a nova lista. Essa parte é obrigatória
- A 2° parte da compressão é a iteração na lista original (repare que é exatamente o mesmo `for` do exemplo anterior, `for numero in numeros`). Essa parte é obrigatória
- A 3° parte da compressão é uma condição que irá filtrar os elementos da sequencia original. Nesse caso, somente os números pares vão corresponder a essa condição. 
  - Vale ressaltar que essa parte da condição é opcional, depende do tipo de operação que você vai realizar. Para filtrar valores, é recomendado utiliza-la, já para modificar não existe muita utilidade.
```py
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
# [numero = item que será retornado pós compressão para compor a nova lista
# for numero in numeros = iteração sobre a lista original
# if numero % 2 == 0 = condição que irá filtrar os números pares para compor a nova lista 
```

#### Modificar valores

>Agora, imagine que você tem uma lista de números variados e precisa criar uma nova lista de números, onde cada elemento será elevado ao quadrado.
- Sem compressão, novamente temos que declarar uma lista vazia (quedrado) e declaramo o laço explicitamente:
**Modificando valores - versão 1**
```py
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
  quadrado.append(numero ** 2)
```

**Modificando valores - com compressão**
Utilizando a compressão:
- Repare como o retorno da operação (`numero ** 2`) é justamente o elemento iterado elevado ao quadrado.
- Além disso, repare como nesse caso não estamos realizando nenhuma condição (utilizando `if`) pois nesse caso não estamos filtrando nenhum valor, apenas modificando os valores originais e atribuindo a outra lista
```py
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]
```

-------------------------------------------------------------------------------------------------------------------

## Métodos da classe list

Abaixo uma lista contendo os principais métodos da classe list

#### [].append
- Esse método adiciona valores ao fim da lista. Recebe como parâmetro entre () o valor que será adicionado
```py
lista = []

lista.append(1) # Adicionando um inteiro
lista.append("Mateus") # Adicionando uma string
lista.append([40, 30, 20]) # Adicionando outra lista

print(lista)
>>> [1, "Python", [40, 30, 20]]
```

#### [].clear
- Esse método limpa uma lista, excluindo todos os valores existentes.
```py
lista = [1, "Python", [40, 30, 20]]

print(lista) # Antes do método clear
>>> [1, "Python", [40, 30, 20]]

lista.clear()
print(lista) # Depois do método clear
>>> []
```

#### [].copy
- O método `copy` retorna uma cópia idêntica a lista original, porém em uma instância diferente. Ou seja, NÃO é a mesma lista, pois apontam para espaços de memória diferentes.
- Esse método é útil pois a lista, como todo objeto em Python, é mutável. Com isso, o que é feito numa lista copiada NÃO é refletido para lista original.
```py
lista = [1, "Python", [40, 30, 20]]
lista_copia = lista.copy()

print(lista_copia)
>>> [1, "Python", [40, 30, 20]]

# Verificando o identificador de cada objeto
print(id(lista))
>>> 140149040385088

print(id(lista_copia))
>>> 140149040388352
```

#### [].count
- O método `count` retorna quantas vezes um determinado valor aparece na lista. Recebe como parâmetro o valor que será contado
```py
cores = ["vermelho", "azul", "verde", "azul"]

cores.count("vermelho") # 1
cores.count("azul") # 2
cores.count("verde") # 1
```

#### [].extend
- O método `extend` permite adicionar uma nova sequencia de valores à uma lista. Porém, diferentemente do método `append`, essa sequência será incorporada a lista original.
  - Por exemplo, fazer isso `lista.append([10, 11, 12])` irá adicionar uma nova sequencia a lista original
  - Fazer isso `lista.extend([10, 11, 12])` irá adicionar somente os valores a uma sequencia
- Vale ressaltar que ele adiciona valores duplicados a lista
```py
linguagens = ["python", "js", "c"]

print(linguagens)
>>> ["python", "js", "c"]

linguagens.extend(["java", "csharp"])

print(linguagens)
>>> ["python", "js", "c", "java", "csharp"]
```

#### [].index
- Esse método retorna o indice da primeira ocorrência do valor repassado como parâmetro
```py
linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.index("java")
>>> 3

linguagens.index("python")
>>> 0
```

#### [].pop
> Por padrão, uma lista em Python vem estrutura como uma pilha/stack. Para facilitar, imagine uma pilha de livros, onde o primeiro livro adicionado é o último a ser removido. Esse comportamento é conhecido como *LIFO* (Last In Firts Out - Ultimo a entrar, primeiro a sair) onde o último elemento a ser adicionado a lista é o primeiro a ser removido
- O método `.pop()` retira o último elemento da lista. Também é possível repassar o índice como parâmetro para remover algum elemento específico.
```py
linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.pop()
>>> csharp

linguagens.pop()
>>> java

linguagens.pop()
>>> c

linguagens.pop(0) 
>>> python
```

#### [].remove
- Esse método remove um elemento da lista com base no valor/objeto especificado. Se existir elementos duplicados, apenas a primeira ocorrência será removida
```py
linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.remove("c")

print(linguagens)
>>> ["python", "js", "java", "csharp"]
```

#### [].reverse
- Esse método irá inverter os elementos da lista.
```py
linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.reverse()

print(linguagens)
>>> ["csharp", "java", "c", "js", "python"]
```

#### [].sort
- Esse método irá ordenar a lista. Existem alguns parâmetros para diferentes tipos de ordenação:
  - `sort()`: Sem nenhum parâmetro irá ordenar a lista alfabeticamente em ordem CRESCENTE
  - `sort(reserve=True)`: Com o reserve = true, irá ordernar a lista alfabeticamente em orderm DECRESCENTE
  - `sort(key=lambda x: len(x))`: Ordena as palavras com base na quantidade de caracteres em ordem CRESCENTE
    - O parâmetro `key` recebe uma função *lambda* como parâmetro. Não iremos entrar em detalhes por agora, mas de forma simples lambda é uma função anônima.
  - `sort(key=lambda x: len(x), reverse=True)`: Ordena as palavras com base na quantidade de caracteres em ordem DECRESCENTE
```py
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort() # ["c", "csharp", "java", "js", "python"]

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True) # ["python", "js", "java", "csharp", "c"]

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x)) # ["c", "js", "java", "python", "cs

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True) # ["python", "csharp" "java", "js", "c"]
```

#### [].len
- Esse método é utilizado para retornar o tamanho, tanto dos elementos quanto da lista em si.
```py
linguagens = ["python", "js", "c", "java", "csharp"]

len(linguagens) # Nesse caso retorna o tamanho da lista, ou seja, a quantidade de elementos
>>> 5
```

#### sorted()
- O método `sorted` é um método built-in do Python que também é utilizada para ordenar objetos. Ele não é exatamente um método da lista, mas pode ordenar objetos iteráveis.
```py
linguagens = ["python", "js", "c", "java", "csharp"]

sorted (linguagens, key=lambda x: len(x)) # ["c", "js", "java", "python","csharp"]
sorted (linguagens, key=lambda x: len(x), reverse=True) # ["python", "csharp", "java", "js", "c"]
```

--------------------------------------------------------------

<br><br>

# Trabalhando com tuplas em Python

Como a estrutura de tuplas é extremamente semelhante às listas, irei focar apenas nas diferenças entre elas.

------------------------------------------------------------------------------------------------------------------

## Tuplas: Criação e acesso aos dados

Tuplas são estruturas de dados muito parecidas com as listas, a principal diferença é que tuplas são IMUTÁVEIS enquanto listas são MUTÁVEIS. 

>Ou seja, as tuplas NÃO PODEM ser modificadas após a sua criação.

Podemos criar tuplas através da classe `tuple`, ou colocando valores separados por vírgula de parenteses.

>Podemos dizer que essa é a principal diferença em termos de sintaxe entre uma tupla e uma lista. Tuplas utilizam o () no momento de criação, listas utilizam o []

```py
frutas = ("laranja", "pera", "uva",)
letras = tuple("python") # ['p', 'y', 't', 'h', 'o', 'n']
numeros = tuple([1, 2, 3, 4])
pais = ("Brasil",)
```

>É uma boa prática incluir uma vírgula (`,`) no momento de criação de uma tupla, após inserir o último elemento. Isso porque as vexes o interpretador pode confundir uma tupla com uma precedência (ambos usam os parênteses)

Os tópicos abaixo são exatamente iguais entre tuplas e listas. Portanto, verifique as anotações acima para entender os conceitos:
- Acesso direto
- Matrizes/Tuplas aninhadas
- Fatiamento
- Iterar tuplas 
- Enumerate

### Métodos da tupla

Como a tupla é um objeto imutável, não faz sentido existir métodos para adicionar/remover elementos. Existem alguns métodos para tupla e seu funcionamento é exatamente igual aos métodos da lista, portanto, irei lista-los abaixo:
- `().count`: Contar a quantidade de vezes que um elemento aparece em uma tupla
- `().index`: Retorna a posição da primeira ocorrencia de um determinado elemento
- `().len`: Retorna o tamanho da tupla ou de seus elementos