# Estruturas condicionais e de repetição

Essa aula é destinada a explicação sobre identação em blocos, estruturas condicionais e de repetição em Python.

------------------------------------------------------------------------------------------------------------------

## Identação e blocos

Identar código é uma forma de manter o código fonte mais legível e manutenível. Mas em Python ela exerce um segundo papel, através da indentação o interpretador consegue determinar onde um bloco de comando inicia e onde ele termina.

Em outras linguagens é comum utilizarmos caracteres que delimitam aonde o bloco de código começa e termina. No caso do Java, por exemplo, utilizmaos o `{` e `}` para iniciar e terminar um bloco, respectivamente. 

```java
void sacar(double valor){ //Inicio do bloco do método 
    if(this.valor >= valor){ //Inicio do bloco de if 
        this.saldo -= valor;
    } //Fim do bloco do if 
} //Fim do bloco do método 
```

No caso do Python, esse comportamente é um tanto diferente. Existe um caractere que determina o inicio do bloco '`:`', mas o seu término é definido através da identação do código, por conta disso, a identação é obrigatória para que o código seja executado.

>💡Existe uma convenção em Python, que define as boas práticas para escrita de código na linguagem. Nesse documento é indicado utilizar 4 espaços em branco por nível de indentação, ou seja, a cada novo bloco adicionamos 4 novos espaços em branco.

```py
def sacar(self, valor: float) -> None: # Inicio do blodo co método
    if self.saldo >= valor: # Inicio do bloco if
        self.saldo -= valor
    
    # Fim do bloco do if

# Fim do bloco do método
```

**Isso mão funciona em Python ❌**
```py
def sacar(self, valor: float) -> None: # Inicio do blodo co método
if self.saldo >= valor: # Inicio do bloco if
self.saldo -= valor

# Fim do bloco do if
# Fim do bloco do método
```

------------------------------------------------------------------------------------------------------

## Estruturas condicionais

A estrutura condicional permite o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas.

Vamos dividir as estruturas condicionais em 3 níveis:
1. if/else/elif
2. if aninhado
3. if ternário

### if, else e elif

#### if

Para criar uma estrutura condicional simples, composta por um único desvio, podemos utilizar a palavra reservada `if`. O comando irá testar a expressão lógica, e em caso de retorno verdadeiro as ações presentes no bloco de código do `if` serão executadas.
```py
saldo = 2000.0
saque = float(input("Informe o valor do saque:"))

if saldo >= saque:
    print("Realizando saque")

if saldo < saque
    print("Saldo insuficiente")
```

#### if/else

Para criar uma estrutura condicional com dois desvios, podemos utilizar as palavras reservadas `if` e `else`. Como sabemos se a expressão lógica testada no `if` for verdadeira, então o bloco de código do `if` será executado. Caso contrário o bloco de código do `else` será executado.
```py
saldo = 2000.0
saque = float(input("Informe o valor do saque:"))

if saldo >= saque:
    print("Realizando saque")
else:
    print("Saldo insuficiente")
```

#### if/elif/else
Em alguns cenários queremos mais de dois desvios, para isso podemos utilizar a palavra reservada `elif`. O `elif` é composto por uma nova expressão lógica, que será testada e caso retorne verdadeiro o bloco de código do `elif` será executado. Não existe um número máximo de `elifs` que podemos utilizar, porém evite criar grandes estruturas condicionais, pois elas aumentam a complexidade do código.

```py
opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))
    #...
elif opcao == 2:
    print("Exibindo o extrato...")
else:
    sys.exit("Opção inválida")
```

### if aninhado

Podemos criar estruturas condicionais aninhadas, para isso basta adicionar estruturas if/elif/else dentro do bloco de código de estruturas if/elif/else.
```py
if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")
```

> Vale ressaltar que com mais condições aninhadas, mais complexo será para um desenvolvedor realizar a leitura do código.

### if ternário

O if ternário permite escrever uma condição em uma única linha. Ele é composto por três partes:
1. a primeira parte é o retorno caso a expressão retorne verdadeiro; 
2. a segunda parte é a expressão lógica
3. a terceira parte é o retorno caso a expressão não seja atendida.
```py
# Sucesso = 1 parte: retorno caso a expressão retorne verdadeiro
# if saldo >= saque = 2 parte: expressão lógica
# else "Falha" = 3 parte: retorno caso a expressão não seja atendida
status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar saque!")
```

------------------------------------------------------------------------------------------------------

## Estruturas de repetição

São estruturas utilizadas para repetir um trecho de código um determinado número de vezes. Esse número pode ser conhecido previamente ou determinado através de uma expressão lógica.

**Exemplo sem repetição**
```py
# Receba um número e exiba os 2 números seguintes
a = int(input("Informe um número inteiro: "))
print(a)

a += 1
print(a)

a += 1
print(a)
```

**Exemplo com repetição**
```py
# Receba um número e exiba os 2 números seguintes
a = int(input("Informe um número inteiro: "))
print(a)

repita 2 vezes:
    a += 1
    print(a)
```

No exemplo com repetição estamos utilizando uma sintaxe de pseudo-código, ou seja, NÃO existe essas palavras reservadas no Python (`repita, vezes`). Esse exemplo foi apenas para ilustrar como o código se comporta ao utilizar estruturas de repetição.

No Python, existem 3 estruturas de repetição:
- for-in, for-else, for-range
- while, while-else
- Recursos: break e continue

### for

O comando for é usado para percorrer um objeto iterável. Faz sentido usar for quando sabemos o número exato de vezes que nosso bloco de código deve ser executado, ou quando queremos percorrer um objeto iterável. O for segue uma estrutura com 2 partes:
1. O item que está sendo iterado nesse momento. Por exemplo, em uma sequência de palavras, o item que está sendo iterado é uma letra.
   - Vale ressaltar que essa variável pode ser nomeada de qualquer maneira. Mas é recomendado utilizar um nome descritivo, algo que represente uma unidade da sequência que será percorrida. 
2. O objeto interável que será percorrido. Para esse exemplo, imagine a palavra "Mateus"
- Na primeira volta, `item` irá representar `M`. Na segunda, `item` representa `A` e assim sucessivamente.
```py
nome = "MATEUS"
for letra in nome

letra = M # 1 repetição
letra = A # 2 repetição
letra = T # 3 repetição
letra = E # 4 repetição
letra = U # 5 repetição
letra = S # 6 repetição
```

No exemplo abaixo, a estrutura vai se repetir na string `texto` (em Python uma string é um objeto iterável). Dessa forma, cada elemento da posição será uma letra da frase. 
- Em seguida, vamos verificar se cada letra da `texto` está presente (utilizando o operador `in`) na constante `VOGAIS`. Se estiver, essa letra será exibida.
  - O comando `letra.upper()` irá deixar cada letra em maisculo para realizar a comparação. 
```py
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
```

#### for else
O `for` tem uma "variação" que permite adicionar a cláusula `else` no final do bloco para que ele seja executado ao final do laço.
```py
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print() #Quebra de linha
    print("Executa no final do laço")
```

#### range
Range é uma função built-in do Python, ela é usada para produzir uma sequência de números inteiros a partir de um ínicio (inclusivo) para um fim (exclusivo). Se usarmos range(0, 1)
será produzido:
`i , i + 1 ,i+2,i+3,...,j-1 .`
Ela recebe 3 argumentos:
1. stop (obrigatório): Determina o fim da sequência. Esse n° NÃO será incluido no resultado
2. start (opcional): Determina o inicio da sequência. Por padrão, ele sempre inicia com 0
3. step opcional: Determina o incremento para cada número da sequência. Por padrão, sempre adiciona 1 para cada número (1, 2, 3, 4, 5...).
```py
#OBS: Utilizamos o list() para converter o range em uma lista

list(range(6)) # Determinando o fim da sequência
>>> [0, 1, 2, 3, 4, 5]

list(range(1, 6)) # Determinando o inicio e fim da sequencia
>>> [1, 2, 3, 4, 5]

list(range(1, 6, 2)) # Determinando o inicio, fim e o incremento da sequencia. Nesse caso, será de 2 em 2
>>> [1, 3, 5]
```
>Quando dizemos que o fim é exlusivo é porque ele remove o último elemento do resultado. 

#### for range
Podemos utilizar o `range` junto com `for` para percorrer uma sequência de números:
```py
for numero in range(0, 11):
    print(numero, end=" ")
>>> 0 1 2 3 4 5 6 7 8 9 20

# Exibindo a tabuada do 5
for numero in range(0, 51, 5):
    print(numero, end=" ")
>>> 0 5 10 15 20 25 30 35 40 45 50
```

### while
O comando while é usado para repetir um bloco de código várias vezes. Faz sentido usar while quando não sabemos o número exato de vezes que nosso bloco de código deve ser executado.

O while tem uma estrutura parecida com if, pois recebe uma condição booleana e realiza uma verificação. :
```py
while condicao:
    # bloco que será executado enquanto a condição for verdadeira
```

No exemplo abaixo, o laço irá se repetir enquanto a opção for diferente de 0 
```py
opcao = -1

while opsao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato ... ")
```

#### while-else
Assim como o for, é possível utilizar o while com a clasula `else`:
```py
opcao = -1

while opsao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato ... ")
else:
    print("Sistema encerrado")
```

### break
O `break` é uma clásula que pode ser utilizada junto com os laços `while` e `for` e permite interromper a execução a partir de uma condição.
- No exemplo abaixo, o laço será interrompido caso o número digitado seja o 10
```py
while(True): # While true indica que o laço sempre será executado
    numero = int(input("Informe o número: "))

    if numero == 10: 
        break # Interrompe a execução caso o número digitado seja igual a 10

    print(numero)
```

### continue

O `continue` é uma clausula que pode ser utilizada junto com os laços `while` e `for`, é útil quando queremos "desviar" de uma situação específica dentro de um laço. Assim como o break, é executado quando uma condição for verdadeira 
- Por exemplo, mostrar os números de 1 a 15, porém sem mostrar o número 12:
```py
for numero in range(1, 16):
    if numero == 12:
        continue
    
    print(numero, end=" ")
>>> 1 2 3 4 5 6 7 8 9 10 11 13 14 15
```
