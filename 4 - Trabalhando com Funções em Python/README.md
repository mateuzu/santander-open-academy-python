# Dominando Funções Python

Entender como funcionam as funções em Python.

## Funções Python - Parte 01

Função é um bloco de código identificado por um nome e pode receber uma lista de parâmetros, esses parâmetros podem ou não ter valores padrões. Os parâmetros são valores de entrada que podem ser utilizados na função (por exemplo, numa função que realiza a soma de dois números, ambos serão os parâmetros de entrada da função). Além disso, a função pode retornar valores (um ou vários) que são conhecidos como a saída da função.

Usar funções torna o código mais legível e possibilita o reaproveitamento de código.

> Programar baseado em funções, é o mesmo que dizer que estamos programando de maneira estruturada.

Para declarar uma função em Python, utilizamos o operador `def nome_funcao(parametrps)` (ainda usamos o operador `:` como delimitador e a identação como estruturação). Vemos abaixo alguns exemplos:
1. `def exibir_mensagem()`: Essa função não recebe nenhum parâmetro e apenas exibe a mensagem `"Olá mundo!"`
2. `def exibir_mensagem_2(nome)`: Essa função recebe um parâmetro `nome` e exibe uma mensagem `"Seja bem vinco {nome}"`, concatenando com o parametro de entrada. Ou seja, o nome que informarmos no momento de execução, será exibido nessa mensagem. Nesse caso, se o parâmetro `nome` não for repassado, a função irá causar um erro.
3. `def exibir_mensagem_3(nome="Anônimo")`: Parecida com a anterior, porém nessa função definimos um valor padrão para o parâmetro `nome`. Sendo assim, se nenhum argumento for repassado, a função irá utilizar o valor padrão.
- Para executar a função, basta chamar digitando o nome delas
```py
1. def exibir_mensagem():
    print("Olá mundo!")

2. def exibir_mensagem_2(nome):
    print (f"Seja bem vindo {nome}!")

3. def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")

# Chamando as funções
exibir_mensagem() # -> Olá mundo!

exibir_mensagem_2() # -> Dá erro pois a função exibir_mensagem_2 espera um parâmetro 'nome' e não utiliza nenhum valor padrão
exibir_mensagem_2(nome="Guilherme") # -> Seja bem vindo Guilherme!

exibir_mensagem_3() # -> Seja bem vindo Anônimo! -> Aqui não dá erro pois definimos 'Anônimo' como um valor padrão, se não passamos outro nome ele será utilizado
exibir_mensagem_3("Chappie") # Seja bem vindo Chappie! -> Utiliza o nome passado como parâmetro
```

#### Retornando valores
Para retornar um valor, utilizamos a palavra reservada `return`. Toda função Python retorna None por padrão. Diferente de outras linguagens de programação, em Python uma função pode retornar mais de um valor.

Por exemplo, imagine que temos duas funções:
1. Calcula a soma dos números em uma lista
2. Retorna o antecessor e sucessor de um número

Repare como a função `retorna_antecessor_e_sucessor` retornar dois valores, enquanto a `calcular_total` retorna apenas um:
- Vale ressaltar que quando uma função retorna dois valores, o retorno será uma tupla contendo o resultado. Isso acontece porque a tupla é imutável
```py
def calcular_total (numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor (numero):
    antecessor = numero -1
    sucessor = numero + 1
    return antecessor, sucessor

calcular_total([10, 20, 34]) # 64
retorna_antecessor_e_sucessor (10) # (9, 11) -> tupla
```

#### Argumentos nomeados

Funções também podem ser chamadas usando argumentos nomeados da forma `chave=valor`. Abaixo, vamos mostrar diferentes maneiras de repassar os parâmetros de uma função:
1. Valores de forma sequencial: Essa maneira consiste em declarar os valores diretamente na chamada da função. 
    - Uma desvantagem é que essa função pode gerar problemas se o usuário inverter algum valor.
2. Chave/Valor: Essa maneira, precisamos passar a chave (que é o parâmetro que a função espera) e seu respectivo valor. Dessa maneira, mantemos os valores corretos independente da ordem. 
    - Uma desvantagem é que se o nome do parâmetro for alterado, é preciso alterar a chave também, se não vai dar erro.
3. Dicionário: Essa maneira consiste em passar um dicionário com as chaves correspondentes ao que a função espera e seus respectivos valores
```py
def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

# Valores declarados de forma sequencial
1. salvar_carro("Fiat", "Palio", 1999, "ABC-1234") # Carro inserido com sucesso! Fiat/Palio/1999/ABC-1234
   # PROBLEMA: salvar_carro("Palio", "Fiat", 1999, "ABC-1234") ->  Se inverter a ordem, o resultado será diferente: Carro inserido com sucesso! Palio/Fiat/1999/ABC-1234

# Chave valor
2. salvar_carro(marca="Fiat", modelo="Palio", ano 1999, placa="ABC-1234") # Carro inserido com sucesso! Fiat/Palio/1999/ABC-1234
    # PROBLEMA: Se o parametro da função mudar de modelo para nome, é necessário alterar a chave também

# Dicionário / kwargs
3. salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"}) #Carro inserido com sucesso! Fiat/Palio/1999/ABC-1234
```

#### Args e kwargs
Podemos combinar parâmetros obrigatórios com `args` e `kwargs`. Quando esses são definidos (*`args` e **`kwargs`), o método recebe os valores como tupla e dicionário respectivamente.
- *args: agrupa múltiplos argumentos posicionais em uma tupla.
- **kwargs: agrupa múltiplos argumentos nomeados em um dicionário.

>Vimos no exemplo acima: `salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})` aqui estamos usando o `kwargs` e repassando um dicionário para a função

O método abaixo `exibir_poema`... Os parâmetros dele são:
- `data_extenso`: A data do poema por extenso
- `*args`: Uma lista de versos do poema
- `*kwargs*`: Um dicionário com informações do poema (autor, ano, etc)
```py
def exibir_poema (data_extenso, *args, **kwargs):
    texto = "\n".join(args) # Une todos os versos (args) com quebras de linha
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema (
    "Sexta-feira, 26 de Agosto de 2024", 
    "Zen of Python", 
    "Beautiful is better than ugly.", 
    autor="Tim Peters", ano=1999)
```

> Agora, como ele sabe qual valor é referente a qual parâmetro?
1. O 1° valor é destinado ao parâmetro `data_extenso`
2. `args` são declarados como tuplas e como já vimos anteriormente, para declarar uma tupla basta declarar valores separador por `,` dentro de um parênteses. Nesse caso, não precisamos do `()`, mas o Python sabe que todos valores após `data_extenso` que estão separados por `,` serão os valores de `args`
3. O Python sabe que acaba o `args` e começa `kwargs` no momento em que os valores separados por vírgula é substituído pelo mapeamento de chave/valor.

>Vale ressaltar que esses parâmetros não precisam ter o nome `args` e `kwargs`. Você pode usar qualquer nome desde que seja apropriado.
```py
def exibir_poema (data_extenso, *lista, **dicionario):
    texto = "\n".join(lista)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in dicionario.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)
```

**Curiosidade útil**
Você pode também desempacotar uma lista ou dicionário ao chamar uma função que usa *args e **kwargs:
```py
versos = ["Linha 1", "Linha 2"]
info = {"autor": "Autor X", "ano": 2024}

exibir_poema("Hoje", *versos, **info)
```

------------------------------------------------------------------------------------------------------------------------------------------------

## Funções Python - Parte 2

### Parâmetros especiais

Por padrão, argumentos podem ser passados para uma função Python tanto por posição quanto explicitamente pelo nome. Para uma melhor legibilidade e desempenho, faz sentido restringir a maneira pelo qual argumentos possam ser passados, assim um desenvolvedor precisa apenas olhar para a definição da função para determinar se os itens são passados por posição, por posição e nome, ou por nome.

| Tipo de parâmetro                   | Como é passado na chamada?         | Exemplo de chamada   |
| ----------------------------------- | ---------------------------------- | -------------------- |
| **Posicional**                      | Pela ordem                         | `f(10, 20)`          |
| **Nomeado (ou keyword)**            | Pelo nome do parâmetro             | `f(x=10, y=20)`      |
| **Híbrido (posicional ou nomeado)** | Pode ser por ordem **ou** por nome | `f(10)` ou `f(x=10)` |


No Python, é possível forçar isso: O parâmetro obrigatoriamente tem que ser por posição, ou por nome (em alguns casos, pode ser híbrido, posição e nome). Para fazer isso, podemos seguir a estrutura:
```bash
def f(posicional_1, posicional_2, /, posicional_or_nome, *, nome_1, nome_2):
      -------------------------     -------------------     --------------
      |                             |                       |
      |                             |                       | - Apenas nome
      |                             | - Posicional ou nome
      | - Apenas posicional
```
- `/` → Tudo antes disso só pode ser passado por posição
- `*` → Tudo depois disso só pode ser passado por nome
- O que está entre `/` e `*` pode ser passado por posição ou por nome (híbrido)

#### Positional ony
No exemplo abaixo, vemos como definir alguns parâmetros obrihgatoriamente posicionais:
- Nesse caso, os parâmetros à esquerda de `/` (modelo, ano, placa) TEM que ser repassados sem chave/nome, somente por posição.
- Os que estão à direita de `/` (marca, motor, combustivel) pode ser repassados pela posição ou pela chave/valor, fica a critério do desenvolvedor.
- Essa abordagem é útil quando você quer esconder os parâmetros da função. Por exemplo, se futuramente os parâmetros serão renomeados, é útil usar essa abordagem
```py
def criar_carro (modelo, ano, placa, /, marca, motor, combustivel): 
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # válido -> os atributos modelo, ano e placa tem que ser repassados de maneira posicional, sem utilizar chave/nome
criar_carro(modelo="Palio", ano 1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # inválido -> os atributos modelo, ano e placa foram nomeados, então essa função vai dar erro
```

#### Keyword only
No exemplo abaixo, vemos como definir os parâmetros obrigatoriamente nomeados:
- Nesse caso, os parâmetros que estão à direita de `*` (nesse exemplos são todos) TEM que ser repassados de maneira nomeada.
- Essa abordagem é útil quando você quer garantir que o valor será repassado para o parâmetro correto e você não pretende alterar os parâmetros
```py
def criar_carro(*, modelo, ano, placa, marca, motor, combustivel): 
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat",motor="1.0", combustivel="Gasolina") # válido
criar_carro ("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # inválido
```

#### Hybrid
No exemplo abaixo, vemos como definir os parâmetros de maneira híbrida, sendo que alguns serão posicionais e outro serão nomeados:
- Os parâmetros à esquerda de `/` (modelo, ano, placa) TEM que ser repassados sem chave/nome, somente por posição.
- Os parâmetros que estão à direita de `*` (motor, combustivel) TEM que ser repassados de maneira nomeada.
- O parâmetro que está entre `/` e `*` (marca) podem ser repassados tanto por posição, como por nome. 
```py
def criar_carro (modelo, ano, placa, /, marca, *, motor, combustivel): 
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # válido
criar_carro("Palio", 1999, "ABC-1234", "Fiat", motor="1.0", combustivel="Gasolina") # válido
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # inválido
```

### Objetos de primeira classe
Em Python tudo é objeto, dessa forma funções também são objetos o que as tornam objetos de primeira classe. Com isso podemos atribuir funções a variáveis, passá-las como parâmetro para funções, usá-las como valores em estruturas de dados (listas, tuplas, dicionários, etc) e usar como valor de retorno para uma função (closures).

> Um objeto de primeira classe é um objeto que pode ser repassado como argumento de função, atribuído a variáveis e retornado de funções. 

Por exemplo, imagine que temos dois funções:
- `somar(a, b)`: Essa função recebe dois números e realiza a soma
- `exibir_resultado(a, b, funcao)`: Essa função recebe dois números E uma função. Em seguida, exibe o resultado
- Ao chamar a função `exibir_resultado` iremos passar a função `somar` como PARÂMETRO. A função parametrizada `somar` será utilizada internamente em `exibir_resultado` para calcular o valor da soma e atribuir o valor a variável `resultado`
```py
def somar(a, b):
    return a + b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b) # função 'somar' será utilizada internamente para calcular a soma de a + b
    print(f"O resultado da operação é = {resultado}")

exibir_resultado (10, 10, somar) # O resultado da operação é = 20
```

Isso é útil pois podemos criar funções para realizar outras operações e utilizá-las em `exibir_resultado` sem a necessidade de modificar o código:
- Agora, temos a função `subtrair` que vai substrair dois valores.
- Em seguida, repassamos a função `substrair` na chamada de `exibir_resultado`. Isso é totalmente possível e não dá nenhum erro
```py
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b) # função 'somar' será utilizada internamente para calcular a soma de a + b
    print(f"O resultado da operação é = {resultado}")

exibir_resultado (10, 10, somar) # Passando a soma: O resultado da operação é = 20
exibir_resultado (10, 10, substrair) # Passando a subtrair: O resultado da operação é = 0
```

>OBS: Também é possível atribuir funções à variáveis
```py
def somar(a, b):
    return a + b

op = somar # Apontando a função somar para variável op

print(op[2, 20]) # 22 -> no momento de chamar a variavel, podemos passar os parametros através de []
```

### Escopo local e escopo global

Python trabalha com escopo local e global, dentro do bloco da função o escopo é local. Portanto alterações ali feitas em objetos imutáveis serão perdidas quando o método terminar de ser executado. Para usar objetos globais utilizamos a palavra-chave global, que informa ao interpretador que a variável que está sendo manipulada no escopo local é global.<br>
**Essa NÃO é uma boa prática e deve ser evitada.**

No exemplo abaixo, vamos visualizar uma função que utiliza uma variável global.
- `salario` é uma variável global pois está na raiz do programa, fora do escopo de alguma função
- `global salario` para utilizar a variável salario, devemos informar ao Python que ela foi declarada fora do escopo da função. Para isso, devemos utilizar a palavra `global`.
```py
salario = 2000 # Essa é uma variável global pois está na 'raiz' do programa, fora do escopo de função

def salario_bonus (bonus):
    global salario # Para referenciar a variavel global salario, devemos utilizar a palavra 'global'
    salario += bonus
    return salario
    
salario_bonus (500) # 2500
```

>Apenas para fins de exemplo sobre escopos, a variável `local` no exemplo abaixo só existe dentro do método `salario_bonus`:
- A variável `local` não pode ser acessada fora do escopo da função, pois ela só existe dentro dele. Então, se eu tentar modificar o valor dela fora do escopo, o Python vai criar outra variável com o mesmo nome
```py
salario = 2000

def salario_bonus (bonus):
    local = 10
    global salario
    salario += bonus
    return salario

local = 20 # Essa variavel não pode ser acessada fora do escopo da função, pois ela só existe dentro dele
```


