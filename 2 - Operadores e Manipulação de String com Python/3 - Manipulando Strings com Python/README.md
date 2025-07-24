# Manipulando String com Python

Conhecer métodos úteis para manipular objetos do tipo string, como interpolar valores de variáveis e entender como funciona o fatiamento.

------------------------------------------------------------------------------------------------------------------

## Conhecendo métodos úteis da classe string

A classe String do Python é famosa por ser rica em métodos e possuir uma interface muito fácil de trabalhar.
Em algumas linguagens manipular sequências de caracteres não é um trabalho trivial, porém, em Python esse trabalho é muito simples.

Abaixo irei mostrar alguns dos principais métodos da classe string

#### Maiuscula, minuscula e titulo

No Python, é possível manipular as letras entre maiusculas e minusculas de forma muito simples.
- O método `upper()` deixa todas as letras maiusculas
- O método `lower()` deixa todas as letras minusculas
- O método `title()` deixa todas as letras minusculas, exceto a primeira.
```py
curso = "pYtHon"

print(curso.upper())
>>> PYTHON

print(curso.lower())
>>> python

print(curso.title())
>>> Python
```

#### Eliminando espaços em branco

Para eliminar espaços em branco de uma string:
- `strip()`: Elimina os espaços em branco da esquerda e direita
- `lstrip`: Elimina os espaços em branco somente da esquerda
- `rstrip()`: Elimina os espaços em branco somente da direita
```py
curso = "      Python "

print(curso.strip())
>>> "Python"

print(curso.lstrip())
>>> "Python "

print(curso.rstrip())
>>> "    Python"
```

#### Junções e centralização
Imagine que você precise centralizar ou combinar o conteúdo da sua string com caracteres adicionais:
- `center(quantidade_caracter, caracter)`: Centraliza o conteúdo da sua string entre caracteres.
  - O 1° parâmetro é a quantidade total de caracteres. Por exemplo, `Python` tem 6 caracteres, se o parametro for igual a 10, o Python sabe que precisa incluir 4 caracteres, de modo que a palavra fique centralizada.
  - O 2° parâmetro é o caractere que será utilizado para centralizar. Por padrão, o Python utiliza espaços em branco
- `"caractere".join(string)`: Junta o conteúdo da string com o caractere especificado
  - Esse método vai passar elemento a elemento (no caso, a cada letra) e inserir o caractere especificado entre eles.
```py
curso = "Python"

print(curso.center(10, "#"))
>>> "##Python##"

print(".".join(curso))
>>> "P.y.t.h.o.n"
```

>Com o `join` podemos evitar o uso do for, pois ele já realiza uma iteração na string. Por exemplo:
```py
#Fazer isso
print(".".join(curso))

#É o mesmo que fazer isso
for letra in curso:
    print(letra, end=".")
``` 

------------------------------------------------------------------------------------------------------------------

## Interpolação de variáveis
Em Python temos 3 formas de interpolar variáveis em strings: 
1. a primeira é usando o sinal `%`
2. a segunda é utilizando o método `format`
3. a última é utilizando f strings.

A primeira forma não é atualmente recomendada e seu uso em Python 3 é raro, por esse motivo iremos focar nas 2 últimas.

>OBS: É possível realizar a concatenação de string utilizando o `+` (por exemplp, `print("Olá " + "Mundo")`). Porém, é recomendado utilizar uma dessas 3 maneiras

#### Old style %
Essa maneira de interpolação consiste em utilizar os placeholders para indicar a posição em que as variaveis irão ocupar. Em seguida, realizar a substituição repassando as variáveis na ordem correta utilizando o `%`. 
- `%s` para valores de string
- `%d` para valores inteiros
- `%f` para valores de ponto flutuante
```py
nome = "Guilherme"
idade 28
profissao = "Progamador"
linguagem = "Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))
>>> Olá, me chamo Guilherme. Eu tenho 28 anos de idade, trabalho como Progamador e utilizo e estou matriculado no curso de Python.
```
>É importante se atentar a ordem de substituição das variaveis, pois se elas forem do mesmo tipo o Python irá substitui-las normalmente. 

#### Método format
Uma evolução do `%` é o método format, que fornece diversas maneiras de concatenar string

1. **Padrãos**: Essa maneira consiste em utilizar as `{}` para indicar a posição de uma variavel no texto. Em seguida, substitui-las na ordem correta com o método `.format`
```py
nome = "Guilherme"
idade 28
profissao = "Progamador"
linguagem = "Python"

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))
```

2. **Com índice**: Essa maneira é muito parecida com a versão anterior, porém é possível especificar a posição da variável que será inserida na string. Em seguida, substitui-las usando o método `format` e repassar as variáveis na ordem da posição. 
   - Repare no exemplo abaixo, o método `format` está com variáveis em uma ordem diferente do exemplo anterior.
   - É importante ressaltar que essa estrutura é *0 based*, ou seja, o primeiro índice é o 0.
   - Essa maneira tem uma vantagem, pois é possível repetir a variável apenas repassando a posição que ela vai ocupar novamnete.
```py
nome = "Guilherme"
idade 28
profissao = "Progamador"
linguagem = "Python"

print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}.".format(linguagem, profissao, idade, nome))
```

3. **Com nome**: Essa maneira consiste em repassar o nome das variáveis que irão compor a string entre as `{}`. Em seguida, substitui-las repassando o nome da varivael (que está entre `{}`) e a variável
```py
nome = "Guilherme"
idade 28
profissao = "Progamador"
linguagem = "Python"

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))
```

4. **Usando dicionário**:
```py
nome = "Guilherme"
idade 28
profissao = "Progamador"
linguagem = "Python"

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(**pessoa))
```

#### f-string
O `f-string` é muito semelhante ao `format`, porém sem a necessidade de chamar o método no final. Dessa maneira, passamos apenas o nome da variavel entre as `{}` que automaticamente será substituído pelo valor.
- É necessário incluir o `f"..."` para indicar que ela será formatada
```py
nome = "Guilherme"
idade 28
profissao = "Progamador"
linguagem = "Python"

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

>>> Olá, me chamo Guilherme. Eu tenho 28 anos de idade, trabalho como Progamador e utilizo e estou matriculado no curso de Python.
```

Outro ponto interessante do `f-string` é a possibilidade de formatar casas decimais:
```py
PI = 3.14159

print(f"Valor de PI: {PI:.2f}") # Formata em 2 casas decimais
>>>>> "Valor de PI: 3.14"

print(f"Valor de PI: {PI:10.2f}") # Formata em 2 casas decimais, porém adiciona 10 espaços em branco
>>>> "Valor de PI: 3.14"
```

------------------------------------------------------------------------------------------------------------------

## Fatiamento de string

Fatiamento de strings é uma técnica utilizada para retornar substrings (partes da string original), informando: inicio (start), fim (stop) e passo (step): [start: stop[, step]].

Algumas informações sobre o fatiamento:
- É *0 based*, então os primeiros índices começam no 0
- Se eu não repassar o start (por exemplo, `[:9]`) ele vai considerar desde o ínicio
- Se eu repassar o start, mas não repassar o fim (por exemplo, `[10:]`) ele vai considerar desde o start até o final da string
- Se eu não repassar o start e nem o stop, ele retorna uma cópia da string original
- Ele trabalha com número negativos, ou seja, para capturar a última letra basta utilizar o índice `[-1]`, para o penúltimo `[-2]` e assim sucessivamente
- Por padrão, o step é de 1 em 1 (ou seja, percorre todos elementos). Porém, é possível modificar pare 2 em 2, ou 3 em 3, por exemplo.
```py
nome "Guilherme Arthur de Carvalho"

nome [0] # Recortando por indice, nesse caso a primeira letra
>>> "G"

nome[:9] # Recortando do primeiro elemento  (:) até o 9
>>>>> "Guilherme"

nome [10:] # Recortando do 10 elemento até o final
>>>>> "Arthur de Carvalho" 

nome [10:16] # Recortando do 10 elemento até o 16
>>>> "Arthur"

nome [10:16:2] # Recortando do 10 elemento até o 16, porém de 2 em 2 elementos
>>>> "Atu"

nome[:] # Retorna uma cópia da string
>>>>"Guilherme Arthur de Carvalho

nome[::-1] # Retorna a string original espelhada
>>>"ohlavrac ed ruhtra emrehliuG
```

------------------------------------------------------------------------------------------------------------------

## String de múltiplas linhas ou String tripla

Strings de múltiplas linhas são definidas informando 3 aspas simples ou duplas durante a atribuição. Elas podem ocupar várias linhas do código, e todos os espaços em branco são incluídos na string final.

>Repare que é possível combinar com métodos de interpolação de string, nesse caso o `f-string` 

```py
nome = "Guilherme"

mensagem = f"""
    Olá meu nome é {nome},
   Eu estou aprendendo Python
        Essa mensagem tem diferntes recuos.
"""

>>>
    Olá meu nome é Guilherme,
   Eu estou aprendendo Python
        Essa mensagem tem diferntes recuos.
```