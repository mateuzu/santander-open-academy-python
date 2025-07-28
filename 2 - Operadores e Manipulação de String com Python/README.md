# Tipos de operadores com Python

Essa aula é destinada a explicação sobre os operadores em Python. sendo eles:
- Aritméticos
- Comparação
- Atribuição
- Lógicos
- Identidade
- Associação

------------------------------------------------------------------------------------------------------------------

## Operadores aritméticos

>Os operadores aritméticos executam operações matemáticas, como adição, subtração com operandos.

#### Adição, subtração e multiplicação

Os operadores de adição, subtração e multiplicação são bem comuns. Normalmente, são os mesmos operadores utilizados em outras lingugaens
```py
# Adição
print(1+1)
>>> 2

# Subtração
print(10 - 2)
>>> 8

# Multiplicação
print(4 * 3)
>>> 12
```

#### Divisão e divisão inteira
Para divisão, temos 2 maneiras com sintaxe parecidas mas com resultados ligeiramente diferentes:
- A divisão normal (com uma barra `/`) realiza a divisão dos operantes ao mesmo tempo que transforma o resultado em um *float*
- A divisão inteira (com duas barras `//`) realiza a divisão dos operadores enquanto mantém a parte inteira. Vale ressaltar que em alguns casos, a divisão inteira irá retornar um resultado "incorreto", pois ele exclui os valores decimais. 
    - Por exemplo, `2 / 5` é igual a `2.5`, porém com a divisão inteira ele retorna apenas o `2`, excluindo o `.5` do resultado.
```py
# Divisão normal
print(12 / 2)
>>> 6.0

# Divisão inteira
print(12 // 2)
>>> 6

# Importante ressaltar que ele remove os decimais do resultado
print(5 // 2)
>>> 2
```


#### Módulo e exponenciação
- O módulo refere-se ao resto da divisão entre dois valores
```py
# Módulo
print(10 % 3)
>>> 1

print(2 ** 3)
>>> 8
```

### Precedência dos operadores

Na matemática, existe uma regra que define a ordem em que as operações devem ser realizadas em uma expressão. Essa ordem é crucial, pois, dependendo de como as operações são feitas, o valor final da expressão pode ser diferente. Em linguagens de programação, como o Python, a precedência de operações segue a seguinte ordem:
1. Parênteses: Qualquer operação dentro de parênteses é resolvida primeiro.
2. Exponenciação: A exponenciação (**) é resolvida antes da multiplicação, divisão, soma e subtração.
3. Multiplicação, Divisão e Módulo: Essas operações têm a mesma precedência e são resolvidas de esquerda para direita.
4. Soma e Subtração: Também têm a mesma precedência e são resolvidas de esquerda para direita.

>Note que soma e substração, por padrão, são as últimas a serem resolvidas em uma expressão matemática. Porém, os parênteses podem ser usados para alterar a ordem das operações. Por exemplo, colocando uma soma dentro de parênteses, ela pode ser realizada antes de uma multiplicação, mesmo que a multiplicação tenha maior precedência.

>Quando há duas expressão da mesma hierarquia na expressão (divisão e multiplicação, por exemplo) ela é resolvida seguindo a ordem natural das operações.

- É importante se atentar a isso, pois a ordem em que uma operação é executada altera diretamente seu resultado.
```py
# Resolve 1° a multiplicação
print(10 - 5 * 2)
>>> 0

# Resolve 1° a operação dentro do ()
print((10 - 5) * 2)
>>> 10

# Resolve primeiro a potência
print(10 ** 2 * 2)
>>> 200

# Resolve primeiro a operação dentro do ()
print(10 ** (2*2))
>>> 10000

# Resolve na ordem de esquerda para direita (divisão, depois a multiplicação)
print(10 / 2 * 4)
>>> 20.0
```

**Boa prática** 💡
- Mesmo que o interpretador consiga executar uma expressão matemática utilizando as regras de precedência, é recomendado incluir os parenteses nas operações que serão executadas primeiro. Isso ajuda outros desenvolvedores a entender o código
- O resultado da operação será o mesmo, mas deixa o código mais organizado
```py
# Troque isso
x = 10 * 2 + 6 / 3 - 2 ** 2


# Por isso
x = (10 * 2) + (6 / 3) - (2 ** 2)
```

------------------------------------------------------------------------------------------------------------------

## Operadores de comparação

Os operadores de comparação, como o próprio nome sugere, são operadores utilizados para comparar dois valores. 

Exixtem 4 tipos de operadores de comparação, são eles:
- `>` Menor que
    - `>=` Menor ou igual que
- `<` Maior que
    - `<=` Maior ou igual que
- `==` Igualdade
- `!=` Diferença

>Vale ressaltar que os operadores de comparação retornar um valor booleano. Sendo verdadeiro quando a condição é atendida (4 > 3, por exemplo) e falso quando não é atendida (2 = 1, por exemplo)

```py
saldo = 450
saque = 200

# Igualdade
print(saldo = saque)
>>> False

# Diferença
print(saldo != saque)
>>> True

# Maior que / Maior ou igual que
print(saldo > saque)
>>> True
print(saldo >= saque)
>>> True

# Menor que / Menor ou igual que
print(saldo < saque)
>>> False
print(saldo <= saque>)
>>> False
```
------------------------------------------------------------------------------------------------------------------

## Operadores de atribuição

Os operadores de atribuição são operadores utilizados para definir o valor inicial ou sobrescrever o valor de uma variável.

> As atribuições normalmente seguem uma estrutura de `variavel operador valor`

Existem algumas maneiras de atribuir valores às variaveis:
- Atribuição simples: Utilizando o `=`, esse operador atribui um valor definido a variavel
```py
saldo = 500
print(saldo)
>>>500
``` 

- Atribuição com adição: Utilizando o `+=`, esse operador adiciona um valor a variavel somando ao seu valor atual
    - Fazer `x += 10` é o mesmo que fazer: `x = x + 10`
```py
saldo = 500
saldo += 50

print(saldo)
>>> 550
```

- Atribuição com subtração: Utilizando o `-=`, esse operador subtrai um valor da variavel
    - Fazer `x -= 10` é o mesmo que fazer: `x = x - 10`
```py
saldo = 500
saldo -= 50

print(saldo)
>>> 450
```

- Atribuição com multiplicação: Utilizando o `*=`, esse operador multiplica o valor da variavel
    - Fazer `x *= 10` é o mesmo que fazer: `x = x * 10`
```py
saldo = 500
saldo *= 2 

print(saldo)
>>> 1000
```

- Atribuição com divisão: Utilizando o `/=` ou `//=`, esse operador divide o valor da variavel
    - Fazer `x /= 10` é o mesmo que fazer: `x = x / 10`
```py
saldo = 500
saldo /= 5 

print(saldo)
>>> 100.0

# Divisão inteira
saldo = 500
saldo //= 5

print(saldo)
>>> 100
```

- Atribuição com módulo: Utilizando o `%=`, esse operador atribui ao valor da variavel o resto da divisão
    - Fazer `x %= 10` é o mesmo que fazer: `x = x % 10`
```py
saldo = 500
saldo %= 480 

print(saldo)
>>> 20
```

- Atribuição com exponenciação: Utilizando o `**=`, esse operador exponencia o valor atual da variavel
    - Fazer `x **= 2` é o mesmo que fazer: `x = x ** 2`
```py
saldo = 80
saldo **= 2  

print(saldo)
>>> 6400
```

------------------------------------------------------------------------------------------------------------------

## Operadores lógicos

Os operadores lógicos são operadores utilizados em conjunto com os operadores de comparação, para montar uma expressão lógica. Quando um operador de comparação é utilizado, o resultado retornado é um booleano, dessa forma podemos combinar operadores de comparação com os operadores lógicos, exemplo:
```bash
operador_comparação + operador_lógico + operacor_comparação
```
Existem 3 tipos de operadores lógicos
- `and`: Operador E. Precisa que todas as condições sejam VERDADEIRAS para que seu resultado seja verdadeiro
    - O operador `and` retorna True apenas quando todas as condições envolvidas forem `True`. Se alguma das condições for `False`, o resultado é `False`.
```py
saldo = 1000
saque = 200
limite = 100

# 1° condição = V           2° condição = F              
saldo >= saque      and     saque <= limite
>>> False # Retorna false porque uma condição é falsa
```

- `or`: Operador OU. Precisa que somente uma das condições seja verdadeira para que seu resultado seja verdadeiro.
    - O operador `or` retorna True se qualquer uma das condições for `True`. Caso todas as condições sejam `False`, ele retorna `False`.
```py
saldo = 1000
saque = 200
limite = 100

# 1° condição = V           2° condição = F              
saldo >= saque      or      saque <= limite
>>> True # Retorna verdadeiro porque uma condição é verdadeira
```
- `not`: Operador NÃO (ou negação). Inverte o valor lógico de uma expressão booleana, ou seja, ele transforma `True` em `False` e `False` em `True`. Por exemplo, 1000 > 1500 seria falso, mas com o operador `not` se torna verdadeiro.
```py
not 1000 > 1500
>>> True

not True
>>> False

not False
>>> True
```

### Parênteses

Assim como nos operadores aritméticos, podemos usar os parênteses para determinar a precedência em que uma condição será executada ou simplesmente para manter o código mais organizado:
```py
saldo = 1000
saque = 200
limite = 100
conta_especial = True

# Troque isso
saldo >= saque and saque <= limite or conta_especial and saldo >= saque
>>> True

# Por isso
(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
>>> True
```
>Note que `conta_especial` é um atributo do tipo booleano atribuido como `True`. Por conta disso, não precisamos inclui-lo na condição dessa forma `conta_especial == True`, mas sim apenas `conta_especial`. Já se quisermos verificar se ele é `False`, podemos simplesmente usar o operador `not`: `not conta_especial`

------------------------------------------------------------------------------------------------------------------

## Operadores de identidade

Os operadores de identidade são operadores utilizados para comparar se os dois objetos testados ocupam a mesma posição na memória.

>Operadores de identidade em Python não comparam os valores dos objetos, mas sim se ambos os objetos referem-se à mesma localização na memória, ou seja, se são o mesmo objeto na memória.

O operador de identidade é o operador `is` e deve ser utilizado seguindo a sintaxe:
```bash
variavel_a is variavel_b
```
- É possível utilizar operador `not` para negar a operação

Quando dizemos que dois objetos "ocupam a mesma posição na memória", estamos dizendo que as variáveis ou referências de objetos apontam para o mesmo local na memória RAM. Em Python, tudo é um objeto, e uma variável é simplesmente uma referência a esse objeto.

- Se você criar dois objetos que têm o mesmo valor, mas são objetos diferentes, eles ocuparão lugares diferentes na memória. Mesmo que eles tenham valores iguais, eles não serão o mesmo objeto.
- Se você tiver duas variáveis que referenciam o mesmo objeto, elas estarão apontando para o mesmo endereço de memória, e nesse caso, o operador is retornará True.

```py
curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso
>>> True

curso is not nome_curso
>>> False

saldo is limite
>>> True
```

------------------------------------------------------------------------------------------------------------------

## Operadores de associação

Os operadores de associação são operadores utilizados para verificar se um objeto está presente em uma sequência (a sequencia pode ser uma lista, um set ou uma sequencia de caracteres, ou seja, uma string).

O operador de associação é o operador `in` e deve ser utilizado seguindo a sintaxe:
```py
"valor" in sequencia
```
- É possível utilizar operador `not` para verificar se um valor/elemento NÃO está em uma sequência

>Vale ressaltar que o operador `in` é *case-sensitive*, então ele diferencia letras maiusculas de minusculas. Portanto, `Laranja` e `laranja` **NÃO** são a mesma coisa.

```py
curso = "Curso de Python" # Sequencia de caracteres
frutas = ["Laranja", "Uva", "Limão"] # Sequencia de string
saques = [1500, 100] # Sequencia de numeros

# Verifica se o valor Python está presente na stirng curso
"Python" in curso
>>> True

# Verifica se a palavra maça esta presente na lista de frutas
"Maçã" in frutas
>>> False

# Verifica se a palavra maça NÃO esta presente na lista de frutas
"Maçã" not in frutas
>>> True # Como a palavra NÃO ESTÁ, o resultado é verdadeiro

# Verifica se 200  esta presente na lista de frutas
200 in saques
>>> False
```
