# Decoradores, Iteradores e Geradores com Python

Conhecer os decoredores e como utilizá-los em Python.

## Decoradores - Parte 1

Antes de aprender sobre decoradores, vamos relembrar alguns ponto importante sobre funções, pois irá nos ajudar no entendimento:
> Funções em Python são objetos de primeira classe. Isso significa que as funções podem ser passadas e usadas como argumentos.
- No exemplo abaixo, estamos repassando uma função como argumentod o método `mensagem_para_guilherme`.
  - Se o argumento repassado for a função `dizer_oi`, o retorno será a mensagem dessa função
  -  Se o argumento repassado for a função `incentivar_aprender`, o retorno será a mensagem dessa função
```py
def dizer_oi(nome):
    return f"0i {nome}"

def incentivar_aprender(nome):
    return f"0i {nome}, vamos aprender Python juntos!"

def mensagem_para_guilherme (funcao_mensagem):
    return funcao_mensagem("Guilherme")

mensagem_para_guilherme(dizer_oi)
>>> Oi Guilherme
mensagem_para_guilherme(incentivar_aprender)
>>> Oi Guilherme, vamos aprender Python juntos!
```

#### Inner functions

É possível definir funções dentro de outras funções. Tais funções são chamadas de funções internas. Essas funções podem ou não serem executadas dentro de uma função-pai.
- Vemos que `filho_1` e `filho_2` são inner funcions.
```py
def pai():
    print("Escrevendo da pai()")

    def filho_1():
        print("Escrevendo da filho_1()")

    def filho_2():
        print("Escrevendo da filho_2()")

    filho_1()
    filho_2()

pai()
>>> Escrevendo da pai()
    Escrevendo da filho_1()
    Escrevendo da filho_2()
```

#### Retornando funções de funções
Além disso, é possível retornar funções, ou seja, apontar uma referência à função.
- A função `calcular` recebe como parâmetro a operação que será realizada
- Dentro de `calcular`, existem as inner funcions `somar` e `subtrair`, ambas recebem dois valores como argumento e realizam a operação com eles.
- Em seguida, é realizada uma verificação do tipo de operação usada como parâmetro `+` ou `-`, em seguida, uma referência a função será retornada de acordo com a operação escolhida
- `resultado = calcular("+")(1, 3)`: Aqui, estamos chamando a função `calcular` com o parâmetro `+`, o que indica uma operação de soma (ou seja, a função `somar`). Os números entre `(1, 3)` são os argumetnos da inner function (as funções `somar` ou `subtrair`  que esperam esses valores)  
```py
def calcular(operacao):
    def somar(a,b):
        return a + b

    def subtratir(a, b):
        return a - b

    if operacao == "+":
        return somar
    else:
        return subtrair

resultado = calcular("+")(1, 3)
print(resultado) # 4
```

### Decoradores simples

Agora que entendemos que funções são como qualquer outro objeto em Python, podemos seguir em frente e ver a mágica que é o decorador Python.

Um decorador em Python é uma função que modifica o comportamento de outra função ou método. 

Eles são uma forma de modificar o comportamento de uma função ou método sem alterar o código dentro dela. Eles são essencialmente funções que recebem outra função como argumento e retornam uma nova função que, geralmente, é "decorada" com um comportamento adicional.

>Neste exemplo, temos uma função simples que exibe a mensagem "Olá, mundo"
```py
def ola_mundo():
    print("Olá, mundo")

ola_mundo()
>>> Olá, mundo
```

Agora, imagine que queremos adicionar um comportamento extra, como exibir uma mensagem antes e depois de executar uma função. Podemos fazer isso com um decorador
- O decorador irá receber uma função como parâmetro e envolvê-la em outra função (no exemplo, `envelope`, mas pode ser chamada de `wrapper`). Essa função de dentro (inner function) irá exibir uma mensagem antes de executar, executar a função e exibir uma mensagem após executar. Em seguida, iremos retornar um referência à função de dentro (`envelope`)  
- Em seguida, podemos atribuir à função `ola_mundo` o decorador `meu_decorador`, repassando a própria função `ola_mundo` como parâmetro
- Ao executar a função, vemos que o comportamento definido no decorador foi implantado à função. 
```py
def meu_decorador(funcao):
    def envelope():
        print("Faz algo antes de executar a função")
        funcao()
        print("Faz algo depois de executar a função")

    return envelope

def ola_mundo():
    print("Olá, mundo")

ola_mundo = meu_decorador(ola_mundo)
ola_mundo()

>>> Faz algo antes de executar a função
    Olá, mundo
    Faz algo depois de executar a função
```
>O decorador serve para adicionar uma personalização de comportamento dentro de outra função

### Decorator pattern
O Decorator Pattern é um padrão estrutural de design que permite adicionar funcionalidades a objetos de forma dinâmica e flexível. No padrão, você tem uma interface comum, e "decoradores" são usados para adicionar comportamento extra aos objetos sem alterar a classe original.

No Python, o decorador segue uma lógica parecida, mas é usado em funções, enquanto o padrão de design geralmente é aplicado em objetos e suas classes. O decorador em Python pode ser considerado uma forma simplificada do Decorator Pattern

#### Açúcar sintático

*Açúcar sintático* é um termo utilizando quando temos uma função verbosa, mas podemos substitui-la utilizando algum caractere.

Vimos anteriormente que a atribuição de um decorador pode ser um pouco confusa. Isso porquê, a função que queremos "decorar", recebe o decorador com a própria função como argumento:
```py
funcao = decorador(funcao)
```

No caso dos decoradores, o Python permite que você use decoradores de maneira mais simples com o símbolo `@`. 
- Com isso, podemos remover a atribuição explícita a função: `ola_mundo = meu_decorador(ola_mundo)`
```py
def meu_decorador(funcao):
    def envelope():
        print("Faz algo antes de executar a função")
        funcao()
        print("Faz algo depois de executar a função")

    return envelope

@meu_decorador # Usando a funçao meu_decorador
def ola_mundo():
    print("Olá, mundo")

# ola_mundo = meu_decorador(ola_mundo) -> PODEMOS REMOVER ESSA ATRIBUIÇÃO
ola_mundo()
```

---------------------------------------------------------------

## Decoradores - Parte 2

Vimos o decorador simples, sem nenhum parâmetro. Mas o que acontece se a função que queremos "decorar" possuir argumento: Para esse exemplo, imagine que `ola_mundo(nome)` possui um parâmetro `nome`, para ser incorporado na mensagem: 
```py
def ola_mundo(nome):
    print(f"Olá {nome}")
```

Se executarmos o decorador do jeito que está, o compilador vai gerar um erro:
```py
def meu_decorador(funcao):
    def envelope():
        print("Faz algo antes de executar a função")
        funcao()
        print("Faz algo depois de executar a função")

    return envelope

@meu_decorador
def ola_mundo(nome):
    print(f"Olá, {nome}")

ola_mundo()

>>> line 4, in envelope
    funcao()
TypeError: ola_mundo() missing 1 required positional argument: 'nome'
```

### Funções decorada com argumentos
Podemos usar `*args` e `**kwargs` na função interna, com isso ela aceitará um número arbitrário de argumentos posicionais e de palavras-chave.

#### **Exemplo**
Como exemplo, vamos criar um decorador `duplicar`, que simplementes vai executar uma função 2 vezes.
- Repare como a função `envelope` agora recebe os parâmetros `*args` e `**kwargs`. Ambos são repassados para a função decorada.
```py
def duplicar(funcao):
    def envelope(*args, **kwargs):
        funcao(*args, **kwargs)
        funcao(*args, **kwargs)
    
    return envelope

@duplicar
def aprender(tecnologia):
    print(f"estou aprendendo {tecnologia}")

aprender("Python")
```

#### Aplicando no exemplo - Olá mundo
Agora, vamos aplicar a modificação no exemplo `ola_mundi`
```py
def meu_decorador(funcao):
    def envelope(*args, **kwwargs):
        print("Faz algo antes de executar a função")
        funcao(*args, **kwwargs)
        print("Faz algo depois de executar a função")

    return envelope

@meu_decorador
def ola_mundo(nome):
    print(f"Olá, {nome}")

ola_mundo("João")
```

>Vale ressaltar que você pode apenas utilizar o parâmetro `nome` na função interna do `meu_decora`, mas se a função decorada (`ola_mundo`) recebesse um novo parâmetro iria causar um erro no código. O uso de `*args*` e `**kwargs` deixa o fluxo mais dinâmico
```py
def meu_decorador(funcao):
    def envelope(nome):
        print("Faz algo antes de executar a função")
        funcao(nome)
        print("Faz algo depois de executar a função")

    return envelope
```
- Repare que se houver alguma mudança em `ola_mundo`, o programa vai dar erro
```py
# Funciona ✅
@meu_decorador
def ola_mundo(nome):
    print(f"Olá, {nome}")

ola_mundo("João")

# NÃO Funciona ❌
@meu_decorador
def ola_mundo(nome, novo_parametro):
    print(f"Olá, {nome} {novo_parametro}")

ola_mundo("João", "Novo parâmetro")
```

### Retornando valores de funções decoradas
O decorador pode decidir se retorna o valor da função decorada ou não. Para que o valor seja retornado, a função de `envelope` deve retornar o valor da função decorada.

Quando decoramos uma função em Python, o decorador pode interceptar ou modificar o valor retornado. Para garantir que a função decorada se comporte como esperado, o decorador deve repassar esse valor de volta com um return.

Se não fizermos isso, o valor retornado pela função será descartado e substituído por `None`.

#### Exemplo
- No exemplo abaixo, vamos simplemente retornar o parâmetro em caixa alta. Para isso, devemos incluir o retorno da função decorada (no caso, `aprender`) dentro do decorador (no caso, `duplicar`). Isso é feito nesse trecho: `return funcao(*args, **kwargs)`
```py
def duplicar(funcao):
    def envelope(*args, **kwargs):
        funcao(*args, **kwargs) # Executa a função original
        return funcao(*args, **kwargs) # Retorna o valor dela
    
    return envelope

@duplicar
def aprender(tecnologia):
    print(f"estou aprendendo {tecnologia}")
    return tecnologia.upper() # Para que isso funcione, o decorador deve "expor" esse valor retornando a função

tecnologia = aprender("Python")
print(tecnologia)
>>> Estou aprendendo Python
    TECNOLOGIA
```
#### Se isso não fosse feito, o retorno seria "perdido":
- Se você esquecer de tornar o valor dentro do decorador, como no exemplo abaixo, o valor da função decorada será perdido:
```py
def duplicar(funcao):
    def envelope(*args, **kwargs):
        funcao(*args, **kwargs)  # não retorna nada
    return envelope

# Valor perdido
tecnologia = aprender("Python")
print(tecnologia)  # Saída: None
```

### Introspeccção
Introspecção é a capacidade de um objeto saber sobre seus próprios atributos em tempo de execução. Isso permite ao Python, descobrir o nome de uma função com `func.__name__`, ou acessar sua docstring com `func.__doc__`.

Como exemplo, vamos verificar o retorno do nome das duas funções `print` (função built-in do Python) e `ola_mundo` (função criada nos exemplos):
```py
print(print.__name__) #print
print(ola_mundo.__name__) #envelope
```
> Isso acontece porque o `@meu_decorador` substitui a função `ola_mundo` pela função `envelope`, que está dentro do decorador. Ou seja, `ola_mundo` agora aponta para `envelope`, e não mais para a função original.

A introspecção mostra o nome, a docstring, as anotações e outros atributos da função `envelope`, não da original `ola_mundo`. Isso pode ser um problema para:
- Documentação automática
- Ferramentas de depuração
- Análise de código
- Logging
- Testes

#### Solução: `functools.wraps` ✅
A função functools.wraps resolve isso. Ela copia os metadados da função original (func) para a função decoradora (wrapper):
```py
import functools

def meu_decorador(funcao):
    @functools.wraps(funcao) # incluindo o functools.wrap
    def envelope(*args, **kwwargs):
        print("Faz algo antes de executar a função")
        funcao(*args, **kwwargs)
        print("Faz algo depois de executar a função")
        return funcao(*args, **kwwargs)

    return envelope

@meu_decorador
def ola_mundo(nome):
    print(f"Olá, {nome}")
    return nome.upper()

print(print.__name__) # print
print(ola_mundo.__name__) # ola_mundo
```

> O `@functools.wraps(func)` garante que a função `envelope` finja ser a função original, no que diz respeito à introspecção.

### Casos de uso de decoradores
- Autenticação: Imagine que você está criando uma API onde certas funções precisam de autenticação. Você pode usar um decorador para verificar se o usuário está autenticado antes de executar a função
```py
def autenticar(func):
    def wrapper(usuario, *args, **kwargs):
        if not usuario["autenticado"]:
            print("Usuário não autenticado!")
            return
        return func(usuario, *args, **kwargs)
    return wrapper

@autenticar
def acessar_dados(usuario):
    print("Acessando dados confidenciais...")

usuario = {"nome": "João", "autenticado": True}
acessar_dados(usuario)
```
- Logging: Outro uso comum é medir o tempo de execução de funções
```py
import time

def medir_tempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"Tempo de execução: {fim - inicio} segundos.")
        return resultado
    return wrapper

@medir_tempo
def fazer_alguma_coisa():
    time.sleep(2)  # Simula um processo demorado

fazer_alguma_coisa()
```