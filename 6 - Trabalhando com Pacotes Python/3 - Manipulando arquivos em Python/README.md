# Manipulando arquivos com Python

Objetivo: Vamos aprender a importância dos arquivos, como abrir, ler, escrever e gerenciar arquivos em Python. Vamos trabalhar com os formatos `txt` e `csv`.

Contéudo
- Introdução a manipulação de arquivos
- Abrindo e fechando arquivos
- Lendo de um arquivo
- Escrevendo em um arquivo
- Gerenciando arquivos e diretórios
- Tratamento de exceções em manipulação de arquivos
- Boas práticas na manipulação de arquivos
- Trabalhando com arquivos CSV

## Introdução a manipulação de arquivos

Os arquivos são essenciais para qualquer tipo de programação, pois fornecem um meio de armazenar e recuperar dados. Através da manipulação de arquivos, podemos persistir os dados além da vida útil de um programa específico.

>**Conceito de arquivo em informática**: Um arquivo é um container no computador onde as informações são armazenadas em formato digital. Existem dois tipos de arquivos que podemos manipular em Python: arquivos de texto e arquivos binários.

--------------------------------------------------------

## Abrindo e fechando arquivos

Para manipular arquivos em Python, primeiro precisamos abri-los. Usamos a função `open()` para isso. Quando terminamos de trabalhar com o arquivo, usamos a função `close()` para liberar recusos.
- O `open(nome_arquivo, modo_abertura)`: Esse método recebe como parâmetro o nome do arquivo que será aberto, bem como o modo de abertura. Veremos isso mais a frente
- O `close()` vai liberar os recursos computacionais necessários para manipular um arquivo. Então é de suma importância lembrar fechar os arquivos

#### Modos de abertura de arquivo
Existem diferentes modos para abrir um arquivo, como: 
- `r`: somente leitura ('read')
- `w`: gravação ('write') - O arquivo é aberto para escrita e seu conteúdo anterior é APAGADO.
- `a`: anexar* ('append') - O arquivo é aberto para escrita e seu conteúdo anterior é MANTIDO.

>Anexar significa colocar conteúdo em um arquivo já existente.

O modo de abertura deve ser escolhido de acordo com a operação que iremos realizar no mesmo.

```py
# para ler um arquivo
file = open("arquivo.txt", "r") 

# para escrever um arquivo
file = open("arquivo.txt", 'w')

# para adicionar conteudo a um arquivo existente
file = open('arquivo.txt', 'a')
```

----------------------------------------------------------------

## Lendo um arquivo

Python fornece várias maneiras de ler um arquivo. Podemos usar `read()`, `readline()` ou `readlines()` dependendo de nossas necessidades.

Vamos utilizar esse arquivo como base:
```txt
O que é Lorem Ipsum?
Lorem Ipsum é simplesmente uma simulação de texto da indústria tipográfica e de impressos. O Lorem Ipsum tem sido a simulação de texto padrão da indústria tipográfica e de impressos desde o século XVI, quando um impressor desconhecido pegou uma galera de tipos e os embaralhou para criar um livro de espécimes de tipos. Ele sobreviveu não apenas a cinco séculos, mas também ao salto para a composição eletrônica, permanecendo essencialmente inalterado. Foi popularizado na década de 1960 com o lançamento das folhas Letraset contendo passagens do Lorem Ipsum e, mais recentemente, com softwares de editoração eletrônica como o Aldus PageMaker, incluindo versões do Lorem Ipsum
``` 

>Em alguns casos, é necessário utilizar o caminho inteiro do arquivo no método `open()`. Além disso, é importante utilizar o modo de abertura correto. Como estamos lendo um arquivo, devemos utilizar o `r`.

- O método `read()` vai ler todo o conteúdo de um arquivo, convertê-lo em uma string e retornar ele todo de uma vez:
```py
file = open('arquivo.txt', 'r')

arquivo_string = file.read() # lendo todo o conteúdo do arquivo de uma vez

print(arquivo_string)
>>> O que Ã© Lorem Ipsum?
Lorem Ipsum Ã© simplesmente uma simulaÃ§Ã£o de texto da indÃºstria tipogrÃ¡fica e de impressos. O Lorem Ipsum tem sido a simulaÃ§Ã£o de texto padrÃ£o da indÃºstria tipogrÃ¡fica e de impressos desde o sÃ©culo XVI, quando um impressor desconhecido pegou uma galera de tipos e os embaralhou para criar um livro de espÃ©cimes de tipos. Ele sobreviveu nÃ£o apenas a cinco sÃ©culos, mas tambÃ©m ao salto para a composiÃ§Ã£o eletrÃ´nica, permanecendo essencialmente inalterado. Foi popularizado na dÃ©cada de 1960 com o lanÃ§amento das folhas Letraset contendo passagens do Lorem Ipsum e, mais recentemente, com softwares de editoraÃ§Ã£o eletrÃ´nica como o Aldus PageMaker, incluindo versÃµes do Lorem Ipsum

file.close() # fechando o arquivo
```

- O método `readline()` lê uma linha por vez. Quando não há mais linhas no arquivo, ele retorna uma linha vazia. 
```py
file = open('arquivo.txt', 'r')
linha = file.readline()
print(linha)
>>> O que Ã© Lorem Ipsum?

file.close()
```


- O método `readlines()` retorna uma lista onde cada elemento é uma linha do arquivo.
```py
file = open('arquivo.txt', 'r')
linhas = file.readlines()
print(linhas)
['O que Ã© Lorem Ipsum?\n', 'Lorem Ipsum Ã© simplesmente uma simulaÃ§Ã£o de texto da indÃºstria tipogrÃ¡fica e de impressos. O Lorem Ipsum tem sido a simulaÃ§Ã£o de texto padrÃ£o da indÃºstria tipogrÃ¡fica e de impressos desde o sÃ©culo XVI, quando um impressor desconhecido pegou uma galera de tipos e os embaralhou para criar um livro de espÃ©cimes de tipos. Ele sobreviveu nÃ£o apenas a cinco sÃ©culos, mas tambÃ©m ao salto para a composiÃ§Ã£o eletrÃ´nica, permanecendo essencialmente inalterado. Foi popularizado na dÃ©cada de 1960 com o lanÃ§amento das folhas Letraset contendo passagens do Lorem Ipsum e, mais recentemente, com softwares de editoraÃ§Ã£o eletrÃ´nica como o Aldus PageMaker, incluindo versÃµes do Lorem Ipsum']

file.close()
```
  - O `readlines()` é comumente utilizado com laços de repetição, como: `for line in file.readlines()` ou `while len(linha := file.readlines())`
```py
# LAÇO FOR
linhas = file.readlines()

for linha in linhas:
  print(linha)


# LAÇO WHILE
while len(linha := linhas):
  print(linha)
```

---------------------------------------------------------------------------------

## Escrevendo em um arquivo

Podemos usar `write()` ou `writelines()` para escrever em um arquivo. Lembre-se, no entanto, de abrir o arquivo no modo correto, nesse caso o `w`.

>OBS: Se você utilizar o modo de abertura `w` e utilizar um arquivo inexistente no método `open()`, o python irá criar esse arquivo. 

- O método `write()` irá escrever a string parametrizada no arquivo.
```py
file = open('novo_arquivo.txt', 'w') # Esse arquivo não existe, então o python irá criar
file.write("Olá, mundo!")
file.close()
```
- O método `writelines()` espera um iterável como argumento. Podemos então repassar uma lista/tupla/iterador de strings para escrever várias palavras/frases de uma vez:
  - A string também é um iterável, então podemos repassar uma string no método `writelines()`, a diferença é que ele vai escrever uma letra de cada vez
  - É importante ressaltar que uma lista não possui espaços de um elemento para outro. Então, devemos colocar esse espaço manualmente para que o resultado não fique grudado. Isso serve também para a quebra de linha, devemos utilizar o caractere `\n` para indicar uma nova linha
```py
arquivo.writelines(["Assim", "fica", "sem", "espaço", "entre", "as", "palavras"])

arquivo.writelines(["Agora ", "tem ", "um ", "espaço ", "entre ", "as ", "palavras"])

arquivo.writelines(["\n", "isso ", "vai ", "estar ", "em " , "outra ", "linha"])
```

------------------------------------------------------------------------------------

## Gerenciando arquivos e diretórios

Python também oferece funções para gerenciar arquivos e diretórios. Podemos criar, renomear e excluir arquivos e diretórios usando os módulos `os` e `shutil`. Ambos os módulos são grandes e possuem diversas operações, mas vamos focar apenas nas operações mais usuais:
- Criar um diretório
- Renomear um arquivo
- Remover um arquivo
- Mover um arquivo

### Capturando o diretório atual

Antes de mostrar os comandos de gerenciamento de arquivos/diretórios, vamos visualizar como podemos capturar o diretório atual.

Normalmente, criamos um arquivo (ou até mesmo um diretório) dentro de um diretório maior (diretório-pai) onde o código está sendo executado. 
```bash
diretorio-pai/
  # Queremos criar arquivos/diretorios dentro de diretorio-pai
  diretorio-filho/
    arquivo.txt
```

Para que possamos fazer isso, precisamos saber o caminho do diretório-pai.

> Existem 2 formas de fazer isso: Manualmente ou dinamicamente

#### **Informando o caminho manualmente**
Aqui, criamos uma constante `ROOT_PATH` para armazenar o diretorio-pai atual, para criar os recursos dentro dele. Essa maneira é ruim por 2 motivos:
  - Deve ser informado manualmente, então está sujeita a erros de digitação. Além disso, alguns sistemas operacionais utilizam `/`, enquanto outros utilizam `\`. Isso pode causar confusão se feito de maneiro manual
  - Caso o diretório mude, essa variável precisará ser alterada também.
```py
ROOT_PATH = 'C://diretorios/diretorio-pai'
```
#### Capturando o caminho de maneira dinâmica
Aqui, criamos a constante `ROOT_PATH` para armazenar o diretorio-pai atual, para criar os recursos dentro dele, semelhante ao sistema anterior.
- `from pathlib import Path`: Realizando o import do módulo `pathlib`
- `Path(__file__)`: O `__file__` retorna o diretório atual, mas nesse caso queremos um diretório 'acima' do atual, ou seja, o diretório-pai. Para isso, utilizamos `.parent`. 
 
```py
from pathlib import Path
ROOT_PATH = Path(__file__).parent # captura um diretório 'acima' do diretório atual
```

>Agora, independente da maneira utilizada para capturar o diretório, temos uma constante `ROOT_PATH` contendo o valor dele e iremos utilizar na criação de diretórios/arquivos. Além disso, essa constante também será utilizada na abertura de arquivos com o método `open()`

#### Criar diretório
O comando abaixo vai criar um novo diretório com o nome parametrizado, nesse caso `diretorio`.
- `os.mkdir(ROOT_PATH / 'diretorio')`: Aqui, estamos usando a constante com o diretório atual + `/` (essa barra é utilizada para informar que queremos criar algo DENTRO do diretório em `ROOT_PATH`) + `diretorio` que é o nome desse subdiretório

>OBS: Daqui pra frente, todos os exemplos seguirão uma estrutura semelhante utilizando `ROOT_PATH`. Para não ficar repetitivo, não vou explicar todos de um a um.

```py
import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent
os.mkdir(ROOT_PATH / 'diretorio')
``` 

#### Renomear arquivo
O comando abaixo vai renomear um arquivo/diretório
- Assim como no exemplo anterior, estamos utilizando `ROOT_PATH`
```py
import os
import shutil

os.rename(ROOT_PATH / "novo_arquivo.txt", ROOT_PATH / "alterado.txt")
```

#### Remover um arquivo
O comando abaixo vai remover um arquivo/diretório
```py
import os
import shutil

os.remove(ROOT_PATH / "alterado.txt")
```

#### Mover um arquivo
O comando abaixo vai mover um arquivo para outro diretório
- `ROOT_PATH / 'arquivo_mover.txt'`: O 1° argumento é a localização atual do arquivo
- `ROOT_PATH / 'novo_diretorio' / 'arquivo_mover.txt'`: O 2° argumento é a nova localização do arquivo, para onde ele será movido. Repare que nesse exemplo estamos utilizando o diretório atual, criando um subdiretório novo (`novo_diretorio`) e repassando o arquivo (`arquivo_mover.txt`) para dentro dele 
```py
import os
import shutil

shutil.move(ROOT_PATH / 'arquivo_mover.txt', ROOT_PATH / 'novo_diretorio' / 'arquivo_mover.txt')
```
<br>

> A titulo de curiosidade, segue um exemplo de como podemos abrir arquivos (para ler, escrever ou anexar) utilizando `open()` + a constante `ROOT_PATH`
```py
try:
  with open(ROOT_PATH / 'log.txt', 'a', encoding='utf-8') as arquivo:
    pass
except IOError ex:
  print(f"Erro ao abrir arquivo {ex}")
```

------------------------------------------------------------------------

## Tratamento de exceções em manipulação de arquivos

Tratar erros é uma parte importante da manipulação de arquivos. Python oferece uma variedade de exceções que nos permitem lidar com erros comuns.

#### O que é uma exceção?
Uma exceção em programação é um evento inesperado que ocorre durante a execução de um programa, interrompendo o fluxo normal de execução. Em outras palavras, uma exceção acontece quando algo dá errado, por exemplo, quando o código tenta dividir por zero, acessar um índice fora de um array ou tentar abrir um arquivo que não existe.

Em Python, exceções são tratadas com o uso de blocos `try` e `except` para capturar e lidar com essas situações de erro, sem que o programa trave ou pare de funcionar abruptamente.

**Exceções mais comuns**
- `FileNotFoundError`: Lançada quando o arquivo que está sendo aberto não pode ser encontrado no diretório especificado.
- `PermissionError`: Lançada quando ocorre uma tentativa de abrir um arquivo sem as permissões adequadas para leitura ou gravação.
- `IOError`: Lançada quando ocorre um erro geral de E/S (entrada/saída) ao trabalhar com o arquivo, como problemas de permissão, falta de espaço em disco, entre outros.
- `UnicodeDecodeError`: Lançada quando ocorre um erro ao tentar decodificar os dados de um arquivo de texto usando uma codificação inadequada.
- `UnicodeEncodeError`: Lançada quando ocorre um erro ao tentar codificar dados em uma determinada codificação ao gravar em um arquivo de texto.
- `IsADirectoryError`: Lançada quando é feita uma tentativa de abrir um diretório em vez de um arquivo de texto.

```py
# exceção de arquivo não encontrado
try:
    arquivo = open('arquivo_inexistente', 'r')
except FileNotFoundError as e:
    print("Arquivo não encontrado!")
    print(e)

ROOT_PATH = Path(__file__).parent

# exceção de diretório
try:
    arquivo = open(ROOT_PATH / "diretorio_inexistente")
except IsADirectoryError as exc:
    print(f"Não foi possível abrir o arquivo: {exc}")
```

Vale ressaltar que é possível tratar várias exceções em um bloco só.
- É uma boa prática finalizar o bloco com `except Exception` para capturar qualquer outra exceção que seja diferente das listadas 💡
- Além disso, é importante utilizar o `as` para atribuir à variável para que possamos utiliza-la no tratamento. 
```py
try:
  arquivo = open (ROOT_PATH / "novo-diretorio" "novo.txt", "r")
except FileNotFoundError as exc:
  print("Arquivo não encontrado!")
  print(exc)
except IsADirectoryError as exc:
  print(f"Não foi possível abrir o arquivo: {exc}")
except IOError exc:
  print(f"Erro ao abrir o arquivo: {exc}")
except Exception as exc:
  print(f"Algum problema ocorreu ao tentar abrir o arquivo: {exc}")
```

----------------------------------------------------------------------

## Boas práticas na manipulação de arquivos

Abaixo as principais boas práticas ao realizar manipulação de arquivos com Python

#### Bloco with
Use o gerenciamento de contexto (context manager) com a declaração `with`. Ο gerenciamento de contexto permite trabalhar com arquivos de forma segura, garantindo que eles sejam fechados corretamente, mesmo em caso de exceções.
- O comando `with` vai garantir o fechamento do arquivo, mesmo em caso de exceções.
- O `as arquivo` atribui a abertura do arquivo para variável para que possamos utilizá-la posteriormente. É o mesmo que fazer `arquivo = open('arquivo.txt', 'r')`
```py
with open('arquivo.txt', 'r') as arquivo:
  # Faça operações de leitura/gravação no arquivo
```

#### Verificar se o arquivo foi aberto
É recomendado verificar se o arquivo foi aberto corretamente antes de executar operações de leitura ou gravação nele.

- A grande sacada é envolver o comando `with` dentro de um `try/except` com `IOError` sendo capturado. Dessa forma, podemos garantir que um arquivo foi ou não aberto, visto que o `IOError` trata de erros ao abrir arquivos.
```py
try:
  with open('arquivo.txt', 'r') as arquivo:
    # Faça operações de leitura/gravação no arquivo
except IOError as e:
  print("Não foi possível abrir o arquivo " + e)
```

#### Use a codificação correta
Certifique-se de usar a codificação correta ao ler ou gravar arquivos de texto. O argumento `encoding` da função `open()` permite especificar a codificação.
```py
with open('arquivo.txt', 'r', encoding='utf-8') as arquivo:
    # Operações de leitura com codificação UTF-8

with open('arquivo.txt', 'w', encoding='utf-8') as arquivo:
    # Operações de gravação com codificação UTF-8
```

> Mas afinal, o que é codificação e por que isso é importante?

Codificação, em termos de computação, refere-se ao processo de converter texto (caracteres) em um formato que o computador possa entender e manipular. O que queremos é representar palavras e símbolos de forma que o sistema consiga "ler" e "escrever" esses caracteres, já que os computadores funcionam com números binários.

Em essência, codificação mapeia cada caractere (letra, número, símbolo) para um número específico. Esses números podem ser representados em binário, ou seja, como sequências de 0s e 1s. O objetivo é garantir que o computador saiba como representar, armazenar e transferir texto de forma consistente.

>UTF-8 (8-bit Unicode Transformation Format) é uma codificação específica usada para representar texto. É uma das formas mais populares de codificação, especialmente porque é compatível com Unicode, que é um sistema de codificação universal que suporta caracteres de praticamente todas as línguas do mundo, além de símbolos especiais, emojis, etc.

Cada codificação possui conjuntos de caracteres "exclusivos". Por exemplo, `ÿ` é um caracterer que existe em utf-8 mas não existe em outras codificações (`ascii`, por exemplo). Se tentarmos abrir um arquivo `utf-8` que possua caracter exclusivo, com outro tipo de codifcação, o código vai gerar um erro `UnicodeDecodeError`
```py
# arquivo.txt de exemplo: ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ Arquivo utf-8

# isso vai gerar um erro, pois a codificação ascii não possui o caracter 'ÿ'
with open('arquivo.txt', 'r', encoding='ascii') as arquivo:
  pass

```
----------------------------------------------------------------------

## Trabalhando com arquivos CSV

Vamos aprender sobre arquivos CSV, um formato de arquivo amplamente utilizado para armazenar dados tabulares. CSV é a sigla para 'Comma Separated Values', em português, 'Valores Separados por Vírgula'. Vale ressaltar que é possível alterar o caracter de separação, mas os mais comuns são `,` ou `;` 

> CSV é um arquivo de texto com formato para segmentar seus dados

Arquivos CSV (Comma Separated Values) são um formato simples e popular para armazenar dados em forma de tabelas. Cada linha do arquivo corresponde a uma linha de dados, e os valores dentro de cada linha são separados por um delimitador, sendo os mais comuns a vírgula (,) ou ponto e vírgula (;), dependendo da configuração regional do sistema ou da necessidade de evitar conflitos com outros caracteres nos próprios dados.

#### Estrutura Básica de um Arquivo CSV
Um arquivo CSV consiste em uma sequência de linhas, onde cada linha representa um registro de dados. Dentro de cada linha, os dados dos campos são separados por um delimitador, que normalmente é a vírgula (em regiões que usam ponto como separador decimal) ou o ponto e vírgula (em regiões onde a vírgula é usada como separador decimal).
```csv
nome,idade
João,28
Maria,34
Carlos,25
```

Python fornece um módulo chamado `csv` para lidar facilmente com arquivos CSV. Antes de visualizar os métodos, vamos visualizar algumas boas práticas:

#### Práticas recomendadas
- Usar `csv.reader` e `csv.writer` para manipular arquivos CSV.
- Fazer o tratamento correto das exceções.
- Ao gravar arquivos CSV definir o argumento `newline=''` no método `open`.

#### Lendo arquivos CSV
Para ler um arquivo CSV podemos seguir uma estrutura semelhante a um arquivo txt (com `readlines()`). Como o arquivo CSV possui dados tabelados, é recomando realizar a leitura junto com um laço `for` 
```py
import csv

with open('exemplo.csv', 'r') as file:
  reader = csv.reader(file) # csv.reader
  for linha in reader:
    print(linha)
```

#### Escrevendo arquivos CSV
Da mesma forma podemos utilizar o módulo 'csv' para escrever em arquivos CSV. 

Para escrever uma linha utilizamos o método `writerow`, passando um iterável como parâmetro.
- A 1° linha é destinada ao cabeçalho/titulo do arquivo
- Em seguida, os valores repassados irão seguir a ordem do cabeçalho, ou seja:
  - O primeiro valor será da coluna `nome`, o segundo da coluna `idade`
```py
writer.writerow(["nome", "idade"]) # cabeçalho
writer.writerow(["Ana", 30])
```

> Se `newline=''` não for especificado, as novas linhas incorporadas nos campos entre aspas não serão interpretadas corretamente, e nas plataformas que usam fim de linha \r\n na escrita, um \r extra será adicionado. Sempre deve ser seguro especificar newline='', já que o módulo csv faz seu próprio tratamento de nova linha

```py
import csv

with open('exemplo.csv', 'w', newline='') as file:
  writer = csv.writer(file) # csv.writer
  writer.writerow(["nome", "idade"]) # Cabeçalho do arquivo
  writer.writerow(["Ana", 30])
  writer.writerow(["João", 25])
```

>Existe uma query language para consultar dados de arquivos csv

Clique [aqui](https://docs.python.org/pt-br/3.13/library/csv.html) Documentação do módulo `csv` do Python

#### Dicas 💡
Algumas dicas interessantes ao lidar com arquivos csv

#### Usando índices
É possível acessar os dados do arquivo pelo índice da tabela. Como podemos conter diversas colunas em um arquivo, é recomendado mapeá-las em algum trecho do código para que os desenvolvedores saibam o índice de cada coluna:
- `COLUNA_ID = 0`: Definindo o índice da coluna id
- `COLUNA_NOME = 1`: Definindo o índice da coluna nome 

```py
COLUNA_ID = 0
COLUNA_NOME = 1

try:
  with open(ROOT_PATH / "usuarios.csv" | newline="") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      print(row[COLUNA_ID], row[COLUNA_NOME])
except IOError as exc:
  print(f"Erro ao criar o arquivo. {exc}")
```

Além disso, vimos que a primeira linha sempre é o cabeçalho/titulo do arquivo, então devemos realizar uma verificação para pular o cabeçalho. Faremos isso percorrendo o arquivo com o laço `for i, row in enumerate(reader):`
- `if i == 0:continue`: Se o índice for igual a 0 (ou seja, a primeira linha) iremos pular utilizando o `continue`
```py
COLUNA_ID = 0
COLUNA_NOME = 1

try:
  with open(ROOT_PATH / "usuarios.csv" | newline="") as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
      if i == 0:
        continue # Pulando o cabeçalho
      print(f"ID: {row[COLUNA_ID]}")
      print(f"Nome: {row[COLUNA_NOME]}")
except IOError as exc:
  print(f"Erro ao criar o arquivo. {exc}")
```

#### DictReader
O `DictReader` é uma alternativa muito útil para o problema anterior. Ele é útil pois permite ler os arquivos em forma de dicionários. 

Com ele, podemos acessar os dados repassando o nome da coluna como chave, sem a necessidade de criar constantes para armazenar o índice da coluna:
- Além disso, não existe a necessidade de "pular" manualmente o cabeçalho, pois o `DictReader` já consegue realizar essa diferenciação entre cabeçalho e conteúdo. 
```py
try:
  with open(ROOT_PATH / "usuarios.csv" | newline="") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      print(f"ID: {row['id']}")
      print(f"Nome: {row['nome']}")
except IOError as exc:
  print(f"Erro ao criar o arquivo. {exc}")
```

<br>

------------------------------------------------------------------------------------

<br>

## Desafio

Em nossa aplicação financeira, identificamos a necessidade de rastrear e auditar as ações dos usuários para garantir a segurança e a integridade das operações. O console tem sido útil até agora, mas a quantidade crescente de atividades torna difícil acompanhar todas as operações em tempo real.
Portanto, decidimos que é vital registrar essas informações em um arquivo para análise posterior e backup contínuo.

## Objetivo
Modificar o atual decorador de log, que imprime informações no console, para que ele salve essas informações em um arquivo de log, possibilitando uma revisão mais fácil e uma análise mais detalhada das operações dos usuários.

#### Requisitos
O decorador deve registrar o seguinte para cada chamada de função:
1. Data e hora atuais
2. Nome da função
3. Argumentos da função
4. Valor retornado pela função
5. O arquivo de log deve ser chamado log.txt.
6. Se o arquivo log.txt já existir, os novos logs devem ser adicionados ao final do arquivo.
7. Cada entrada de log deve estar em uma nova linha.

#### Minha implementação
Abaixo as mudanças realizadas no gerador `log_operacao` para atender os requisitos do desafio.
- `ROOT_PATH = Path(__file__).parent`: Capturando o diretório-pai para criar o arquivo dentro dele
- `resultado`, `data_hora`, `nome_operacao`: Variáveis capturando os valores necessário para inserir em `log.txt`
- `try`: Criando o bloco `try` para abrir o arquivo
- `with open(ROOT_PATH / 'log.txt', 'a', encoding='utf-8') as arquivo`: Abrindo o arquivo com o bloco `with` repassando alguns argumentos:
  - `ROOT_PATH / 'log.txt'`: Diretório-pai + `/` (para que o arquivo seja criado dentro do diretório) + `log.txt` (nome do arquivo)
  - `'a'`: Modo de abertura do arquivo, nesse caso estamos usando o `append` para conseguir adicionar outras linhas sempre que o gerador executar
  - `encoding='utf-8'`: Determinando o encode do arquivo
  - `as arquivo`: Atribuindo a abertura do arquivo à variável `arquivo` 
- `arquivo.writelines()`: Realizando a gravação do registro de log com as informações solicitadas (data, função, argumentos e retorno)
- `expcet IOError`: Capturando exceção `IOError` ao tentar abrir o arquivo
  - `print(ex)`: Tratando o erro exibindo uma mensagem no console.
```py
ROOT_PATH = Path(__file__).parent
# DESAFIO DECORADOR + DESAFIO ARQUIVO
def log_operacao(funcao):
    @functools.wraps(funcao)
    def wrapper(*args, **kwargs):
        resultado = funcao(*args, **kwargs)
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        nome_operacao = funcao.__name__
        try:
            with open(ROOT_PATH / 'log.txt', 'a', encoding='utf-8') as arquivo:
                arquivo.writelines(f"[{data_hora}] Função '{nome_operacao}' executada com argumentos {args} e {kwargs}. Retornou {resultado}\n")
        except IOError as ex:
            print(f"Erro ao abrir arquivo: {ex}")

        print("\n========== REGISTRO DE LOG ==========")
        print(f"Data operação: {data_hora} - Nome: {nome_operacao}")

    return wrapper
```

Além disso, realizei a implementação dos métodos `__repr__` nas classes `ContaCorrente` e `PessoaFisica`. Esse método é utilizado para retornar uma representação do objeto (semelhante ao `__str__`) porém esse é mais utilizado em logs
```py
class ContaCorrente:
  def __repr__(self):
        return f"<{self.__class__.__name__}: ('{self.agencia}', '{self.numero}', '{self.cliente.nome}')>"

class PessoaFisica:
  def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: ({self.cpf})>"
```

#### Resultado
```txt
[04/08/2025 18:46:49] Função 'criar_conta' executada com argumentos (1, [<PessoaFisica: (1)>], [<ContaCorrente: ('0001', '1', 'te')>]) e {}. Retornou None
[04/08/2025 18:46:56] Função 'depositar' executada com argumentos ([<PessoaFisica: (1)>],) e {}. Retornou None
[04/08/2025 18:47:07] Função 'depositar' executada com argumentos ([<PessoaFisica: (1)>],) e {}. Retornou None
[04/08/2025 18:47:13] Função 'sacar' executada com argumentos ([<PessoaFisica: (1)>],) e {}. Retornou None
```