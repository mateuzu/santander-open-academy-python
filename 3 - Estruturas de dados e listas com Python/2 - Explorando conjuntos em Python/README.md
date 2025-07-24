# Explorando conuuntos em Python

Conhecer e entender o funcionamento da estrutura de dados set em Python, bem como seus métodos úteis.

--------------------------------------------------------------------------------------------

## Conjuntos

Um set é uma coleção que não possui objetos repetidos, usamos sets para representar conjuntos matemáticos ou eliminar itens duplicados de um iterável.

Como o `set(iterable)` espera um iterável como argumento, podemos passar listas, strings e tuplas.

>Vale ressaltar que o set NÃO garante a ordem dos elementos, então o retorno pode ser diferente para o mesmo exemplo.

```py
set([1, 2, 3, 1, 3, 4]) # {1, 2, 3, 4}
set("abacaxi") # {"b", "a", "c", "x", "i"}
set(("palio", "gol", "celta", "palio")) # {"gol", "celta", "palio"}
```

**Criando conjuntos**
- Um set pode ser criado através do `set()` ou através de valores entre `{}` separados por virgula
```py
set("abacaxi")
linguagens = {"Python", "Java", "Java"}

print(linguagens)
>>> {"Java", "Python"} # Não garante a ordem
```

#### Acessando os dados
Como o set não garante a ordem dos elementos eles não suportam indexação e nem fatiamento, caso queira acessar os seus valores é necessário **converter o conjunto para lista**.

```py
numeros = {1, 2, 3, 4}
numeros[0] # ❌ No set isso não funciona

numeros = list(numeros) # Converte o set em list
numeros[0] # ✅ Depois de transformar em list, é possível acessar
```

#### Iterar os conjuntos e enumerate

A forma mais comum para percorrer os dados de um conjunto é utilizando o comando for. A sintaxe é a mesma que vimos para lista/tupla

```py
carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)
```

O enumerate também é utilizado da mesma forma:
```py
carros = {"gol", "celta", "palio"}

for indice, carro in carros enumerate(carros):
    print(f"{indice}: {carro}")
```

--------------------------------------------------------------------------------------------

## Métodos da classe set

>Quandos falamos de set/conjuntos, estamos falando de conjuntos matemáticos. Logo, toda operação que é possível realizar nos conjuntos matemáticos, também é possível realizar no Python

#### {}.union
- O método `union` irá realizar a união de dois conjuntos diferentes

```py
conjunto_a = {1,2}
conjunto_b = {3,4}

conjunto_a.union(conjunto_b) # {1, 2, 3, 4}
```

#### {}.intersection
- Esse método traz a intersecção (ou seja, a correspondência) entre dois conjuntos
```py
conjunto_a = {1,2, 3}
conjunto_b = {2,3, 4}

conjunto_a.intersection(conjunto_b) # {2, 3} -> ambos conjuntos possuem os valores 2 e 3
```

#### {}.difference
- Esse método retorna a diferença entre dois conjuntos. Ou seja, tudo que está presente no conjunto X mas não está no Y
```py
conjunto_a = {1,2, 3}
conjunto_b = {2,3, 4}

conjunto_a.difference(conjunto_b) # {1} -> Existe no conjunto_a mas não existe no conjunto_b
conjunto_b.difference(conjunto_a) # {4} -> Existe no conjunto_b mas não existe no conjunto_a
```

#### {}.symmetric_difference
- Esse método retorna a diferença simétrica entre dois conjuntos. A diferença simétrica retorna os elementos que NÃO estão na intersecção (que existem nos dois conjuntos). Podemos considerar que a diferença simétrica são todos os elementos diferentes no conjunto (que não se repetem entre dois conjuntos)
```py
conjunto_a = {1,2, 3}
conjunto_b = {2,3, 4}

conjunto_a.symmetric_difference(conjunto_n) # {1, 4} -> 2 e 3 existem em ambos conjuntos, então o retorno são os elementos diferentes
```

#### {}.issubset
- Esse método verifica se um conjunto A é um subconjunto de B. Compreendemos como subconjuntos se TODOS os elementos de conjunto A existem em B, nesse caso, A é um subconjunto de B
```py
conjunto_a = {1,2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3} # Conjunto B possui os elementos de conjunto A (1, 2, 3)

conjunto_a.issubset(conjunto_b) # True -> todos os elementos de A existem em B
conjunto_b.issubset(conjunto_a) # False -> nem todos os elementos de B existem em A
```

#### {}.issuperset
- Esse método faz o contrário do `issubset`, verifica se um conjunto é *superconjunto* de outro. Compreendemos como superconjunto se um conjunto A possuir TODOS os elementos de conjunto B. Nesse caso, A é um superconjunto de B
```py
conjunto_a = {1,2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3} # Conjunto B possui os elementos de conjunto A (1, 2, 3)

conjunto_a.issuperset(conjunto_b) # False -> A não é superconjunto de B
conjunto_b.issuperset(conjunto_a) # True -> todos os elementos de A existem em B, então B é superconjunto de A
```  

#### {}.isdisjoint
- Esse método verifica um conjunto é disjunto de outro conjunto. Compreendmos como disjunto se um conjunto A NÃO possuir nenhum elemento de B e B NÃO possuir nenhum elemento de A. Nesse caso, os conjuntos são disjuntos (ou seja, não possuem intersecção, nenhum elemento se repete)
```py
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9} # Conjunto A e B não possuem intersecção/correspondecia
conjunto_c = {1, 0}

conjunto_a.isdisjoint(conjunto_b) # True -> Conjunto A e B não possuem nenhum elemento que se repetem
conjunto_a.isdisjoint(conjunto_c) # False -> O elemento 1 se repete tanto em A quanto em C, então não são disjuntos
```

#### {}.add
- Esse método adiciona um valor ao set, caso ele NÃO exista na sequencia.
```py
sorteio = {1, 23}

sorteio.add(25) # {1, 23, 25}
sorteio.add(41) # {1, 23, 25, 41}
sorteio.add(25) # # {1, 23, 25, 41} -> 25 já existe, não é adicionado novamente
```

#### {}.clear
- Limpa todos os elementos do set
```py
sorteio = {1, 23}

print(sorteio) # {1, 23}
sorteio.clear()

print(sorteio) # {}
```

#### {}.copy
- Esse método vai copiar todos os elementos de um set. Como já vimos anteriormente, essa cópia ocupa outro espaço na memória
```py
sorteio = {1, 23}
sorteio_copia = sorteio.copy()
```

#### {}.discart
- Esse método irá descartar um descartar um valor do set, caso ele exista na sequencia. Se não existir, não irá acontecer nenhum erro, simplesmente não vai excluir
```py
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros.discard(1)
numeros.discard(45) # o 45 não existe na sequencia

print(numeros) #{2, 3, 4, 5, 6, 7, 8, 9,0)}
```

#### {}.pop
- Esse método vai remover o PRIMEIRO elemento presente na sequencia (diferente da lista que elimina os últimos elementos, o set elimina os elementos da frente)
```py
numeross = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 8}
print(numeros) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

numeros.pop() #0
numeros.pop() #1

print(numeros) #{2, 3, 4, 5, 6, 7, 8, 9}
```

#### {}.remove
- Esse método vai remover um elemento com base no valor. É parecido com o `discart`, mas se o elemento NÃO existir na sequencia o `remove` irá lançar um erro.
```py
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(numeros) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

numeros.remove(0) # 0 -> remove o número 0

print(numeros) # {1, 2, 3, 4, 5, 6, 7, 8, 9}
```

#### {}.len
- Retorna o tamanho do conjunto
```py
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
len(numeros) # 10 -> pois existe números duplicados
```

#### in
- É possível usar o operador `in` para verificar se um elemento/valor está presente no conjunto
```py
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

1 in numeros # True
10 in numeros # False
```