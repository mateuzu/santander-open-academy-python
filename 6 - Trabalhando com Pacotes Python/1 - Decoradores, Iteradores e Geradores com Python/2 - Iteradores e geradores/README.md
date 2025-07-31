# Iteradores e geradores em Python

Vamos aprender sobre iteradores e geradores em Python. Esses são conceitos poderosos que nos permitem trabalhar com sequências de maneira eficiente.

Essa seção irá fornecer uma visão geral sobre como trabalhar de maneira mais eficiente com objetos iteráveis, ou seja, que possuem uma sequência de valores. 

Por ser uma sequência de valores, esses objetos podem ser muito grandes. Quando isso acontece, devemos ter um cuidado especial para lidar com eles, caso contrário, poderemos encontrar alguns problemas como:
- Demora de execução
- Uso intensivo de memória
- Overflow

## Iteradores

Em Python, um iterador é um objeto que contém um número contável de valores que podem ser iterados, o que significa que você pode percorrer todos os valores. 
- Repare que a sequência pode conter diferentes tipos de valores
```py
lista = [1, 2, 3, 4, "M", "A", 40]
```

O protocolo do iterador é uma maneira do Python fazer a iteração de um objeto, que consiste em dois métodos especiais `__iter__()` e `__next__()`. Isso significa que se sua classe possuir esses métodos, ela também poderá ser percorrida.

Um exexmplo muito utilizado no mercado de trabalho é para ler arquivos grandes. 
>Imagine que você precise ler um arquivo excel muito grande para processá-lo, ou salvar em um banco de daods. Com o uso de iteradores, encontramos as seguintes vantagens:
- Economizar memória evitando carregar todas as linhas do arquivo.
- Iterar linha a linha do arquivo.

### **Exemplo - FileIterator para arquivos grandes**
Abaixo um exemplo de um iterador para leitura de arquivos. Como ainda não vimos como lidar com arquivos em Python, vamos concetrar as explicações nos métodos `__iter__` e `__next__` .
- `__iter__`: Esse método retorna a instância do objeto de iteração. Nesse caso, o objeto de iteração será a própria classe `FileIterator`, então retornamos o `self`
- `__next__`: Esse método retorna o próximo item da sequência. Nesse exemplo, estamos tratando uma linha de cada vez. Se a linha for diferente de vazia, ela será retornada, senão o arquivo será fechado.
- `raise StopIteration`: Quando não existir mais elementos/valores dentro da sequência, devemos lançar o `StopIteration`. O `StopIteration` é utilizado para informar as estruturas de repetição que não há mais elementos dentro do iterador, então o laço deverá ser finalizado.
- `for line in FileIterator`: Aqui, estamos usando o laço `for` repassando a nossa classe `FileIterator`. Podemos considerar essa linha como "para cada linha presente no LeitorArquivo, exiba essa linha". O `FileIterator` espera o nome do arquivo como parâmetro do construtor. 
```py
class FileIterator:
    def __init__(self, filename):
        self.file = open(filename)

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readLine()
        if line != '':
            return line
        else:
            self.file.close()
            raise StopIteration

# Uso do FileIterator
for line in FileIterator('arquivo_grande.txt'):
    print(line)
```

**Resumo**
- `__iter__()` → retorna o próprio objeto iterador.
- `__next__()` → retorna o próximo item ou lança StopIteration quando acaba.

### Montando um iterador
Como o exemplo acima envolve manipulação de arquivos, algo que ainda não vimos no curso, vamos fazer um iterador mais simples.

O nosso iterador de exemplo irá receber uma lista de números e retornar o dobro de cada elemento, exemplo:
```
lista_original = [2, 4, 6, 8]
saida_esperada = [4, 8, 12, 16] 
```
Agora, vamos definir a classe `DobrarNumero`:
- Normalmente, o ideal é adicionar no construtor tudo aquilo que o iterator precisará para trabalhar. No noso caso, precisamos de uma lista de números e um contador (veremos a função do contador mais a frente)
```py
class DobrarNumero:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0
```
- Agora, precisamos definir os métodos `__iter__` e `__next__`. Como vimos anteriormente, o método `__iter__` define o iterador, então podemos simplesmente retornar uma instância de `DobrarNumero` com o `self`
```py
def __iter__(self):
        return self
``` 
- O método `__next__` busca o próximo elemento da lista. É importante que esse método tenha uma lógica bem precisa para não haver loops infinitos ou exceções. 
  - O propósito do nosso iterador é retornar o elemento da lista original multiplicado por 2, então precisamos capturar esse número. Além disso, precisamos saber em qual posição/volta o iterador está, para isso usamos a variável `contador` (inicializada no construtor com o valor de 0)
  - A cada volta na sequência, o contador será incrementado, o número na posição do contador será capturado e, em seguida, será retornado sendo multiplicado por 2.
  - Porém, essa abordagem poderá lançar uma exceção se **o valor de contador for maior que o tamanho da lista** (contador = 3, porém a lista só possui 2 números). Isso faria com que o código tentasse capturar um número em uma posição inexistente. Gerando o `IndexError`.
  - Já sabemos que precisamos parar o loop quando não houver mais elementos a serem percorridos. Já sabemos também que o `IndexError` será lançado quando tentarmos acessar uma posição inexistente. Então, vamos aliar as duas estruturas dentro de um `try-exception`
  - O comando `try` vai tentar executar o código que está dentro do seu bloco (nesse caso, o código de capturar o número e retornar seu dobro). 
  - O comando `exception` irá capturar a exceção lançada `IndexError`. Podemos fazer qualquer tratamento dentro do bloco do `exception`, como: exibir uma mensagem, interromper a execução, etc. Nesse caso, vamos lançar `StopIteration` para indicar que o laço acabou
```py
# o método __next__ irá buscar pelo proximo elemento
    def __next__(self):
        try:
            numero = self.numeros[self.contador] * 2
            self.contador += 1
            return numero * 2
        except IndexError:
            raise StopIteration
```
> É de suma importância lançar o `StopIteration` para encerrar o laço.

Por fim, podemos utilizar o `DobrarNumero` dentro de um laço `for`. Confira o código completo:
```py
class DobrarNumero:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):
        return self
    
    # o método __next__ irá buscar pelo proximo elemento
    def __next__(self):
        try:
            numero = self.numeros[self.contador] * 2
            self.contador += 1
            return numero * 2
        except IndexError:
            raise StopIteration
        
for i in DobrarNumero(numeros=[2, 4, 6, 8]):
    print(i)
```

---------------------------------------------------------------------

## Geradores
Os geradores são tipos especiais de iteradores, ao contrário das listas ou outros iteráveis, não armazenam todos os seus valores na memória. A principal característica de um gerador é a economia e otimização de memória que ele proporciona ao código.

>Imagine que você tem uma lista com 1000 clientes que precisa ser processada no código, então em algum momento você precisará declará-la. Ao ser declarada, por padrão o Python irá alocar a lista em um espaço na memória para comportar essa lista. Mas quando usamos os geradores, não é necessário retornar a lista inteira de uma vez (ou seja, você pode retornar um cliente de cada vez). Assim, você consegue economizar muita memória

São definidos usando funções regulares, mas, ao invés de retornar valores usando `return`, utilizam `yield`. Mas o que o `yield` faz:
- Suspende a função e retém seu estado.
- Retorna o valor.
- Na próxima chamada, a função continua de onde parou.

>Quando chamamos um gerador, ele executa uma vez e "pausa" mantendo o estado do método e esperando a próxima execução.

As características dos geradores são:
- Uma vez que um item gerado é consumido, ele é esquecido e não pode ser acessado novamente.
- O estado interno de um gerador é mantido entre chamadas. Isso significa que se você possuir uma variável dentro de um gerador, o valor dela será mantido, assim como todo o contexto do bloco.
- A execução de um gerador é pausada na declaração `yield` e retomada daí na próxima vez que ele for chamado.

### **Exemplo - Recuparr dados de uma API**
Imagine que você foi solicitado para criar um sistema que recupere dados de uma API. Esse sistema deve conter as seguintes regras:
- Solicitar dados por páginas (paginação).
- Fornecer um produto por vez entre as chamadas.
- Quando todos os produtos de uma página forem retornados, verificar se existem novas páginas.
- Tratar o consumo da API como uma lista Python.

>Como esse exemplo envolve assuntos que ainda não vimos (API, json, request, response, etc), vamos nos concentrar em entender a estrutura do código.

Podemos fazer isso utilizando geradores:
- A função irá fazer um *loop* enquanto `page` for maior ou igual que `max_pages` (se essa variável não for repassada como argumento, o valor padrão é 100)
- Para cada `page`, iremos capturar os dados da API para a página correspondente. Em seguida, iremos armazenar esses dados presentes na variável `data`
- Na variável `data`, iremos percorrer cada `product` presente nessa variável. Iremos retornar cada um produto por vez com o `yield product`
- Em seguida, verificamos se o dado possui uma propriedades `next_page`. Se não houver, indica que a API não tem uma próxima página para ser processada (ou seja, os dados acabaram). Então, usamos o `break` para interromper
- Por fim, se houver uma propriedade `next_page` em `data`, a variável `page` é incrementada para continuar o processamento.
- O uso do gerador é feito com o uso do laço `for` utlizando a função `fetch_products` com a `api_url` sendo passada como parâmetro. Para cada produto procesado, iremos exibir o nome dele
```py
import requests

def fetch_products(api_url, max_pages=100):
    page = 1
    while page <= max_pages:
        response = request.get(f"{api_url}?page={page}")
        data = response.json()
        for product in data['products']:
            yield product
        if 'next_page' not in data:
            break
        page += 1

# Uso do gerador
for produto in fetch_products("https://api.example.com/products"):
    print(product['name'])
```

### Montando um gerador
Neste exemplo, vamos construir um gerador simples com a memsa ideia do iterador anterior: multiplicar cada elemento de uma lista por 2.
- Repare como o retorno é utilizando `yield`
```py
def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2

for i in meu_gerador(numeros=[2, 4, 6, 8]):
    print(i)
```

>Mas como saber que o gerador "pausou" a execução?
- No exemplo abaixo, vamos chamar o gerador com o método `next()`, fora de qualquer laço de repetição. Podemos perceber que cada vez que o gerador é chamado, uma etapa da função é executada
```py
def gerador_exemplo():
    print("Início")
    yield 1
    print("Meio")
    yield 2
    print("Fim")

g = gerador_exemplo()
print(next(g))  # "Início", depois 1
print(next(g))  # "Meio", depois 2
print(next(g))  # "Fim", depois StopIteration
```

### Gerador x Iterador
Como esses recursos são muito parecidos, pode surgir uma dúvida em relação à quando devo utilizar cada um deles. Vale ressaltar que dentro da programação, nem sempre existirá uma regra bem definida sobre qual o melhor momento para utilização de um determinado recurso. Tudo dependo do contexto do código. Mas no caso dos geradores x iteradores, podemos seguir uma regra:
- Gerador: Você deve usar o gerador quando o código for simples. Criar um gerador para fazer o controle de fluxo em uma sequência ou gerar valores de maneira otimizada são bons casos de uso para o gerador.
- Iterador: Você deve usar o iterador quando o código for mais complexa. Criar uma classe que tem uma lógica diferente de percorrer os elementos é um bom exemplo para uso de iterador personalizado. Vimos nos exemplos um laço simples (de 1 em 1), mas existem diversas maneiras diferentes de percorrer elementos em uma sequência, como: arvore binária, pilhas, filas, etc.

| Situação                                             | Use                    |
| ---------------------------------------------------- | ---------------------- |
| Você quer iterar sobre algo complexo, personalizado  | Iterador personalizado |
| Você quer algo simples, leve e "sob demanda"         | Gerador com `yield`    |
| Precisa economizar memória ao processar muitos dados | Geradores              |
