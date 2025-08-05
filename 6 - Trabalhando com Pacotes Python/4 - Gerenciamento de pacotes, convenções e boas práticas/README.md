# Gerenciamento de pacotes, convenções e boas práticas

Objetivo: Aprender a trabalhar com gerenciamento de pacotes em Python, e boas práticas de codificação seguindo as convenções da PEP 8.

Contéudo
- Gerenciamento de pacotes
- Boas práticas em Python

## O que são pacotes e uso do pip
Pacotes são módulos que podem ser instalados e utilizados em seus programas Python. Eles permitem que você utilize código que foi escrito por outras pessoas, economizando tempo e esforço.
- Agrupamentos de módulos relacionados que podem ser instalados para reutilização.

> Um pacote é uma solução que contém determinados trechos de código de maneira unificada, que permite reutilizar em mais de um projeto.

#### O papel do pip

`Pip` é o gerenciador de pacotes do Python. Ele nos permite instalar, atualizar e remover pacotes facilmente. Ele se comunica com o PyPI (Python Package Index), que é onde a maioria dos pacotes Python são armazenados.

>O site do PyPi permite encontrar, instalar, publicar e verificar a documentação de diversos pacotes Python. Clique [aqui](https://pypi.org/) para ver mais

#### Comandos pip
Como um programador que está aprendendo Python e deseja gerenciar os pacotes do seu projeto, é importante conhecer alguns dos principais comandos do pip.

- `pip`: Mostra todos os comandos disponíveis do pip
- `pip install pacote`: Instala o pacote
- `pip unistall pacote`: Desinstala o pacote
- `pip list`: Lista todos os pacotes instalados 
- `pip install --upgrade pacote`: Atualiza a vesão de um pacote  
```bash
pip install pacote
pip unistall pacote
pip list
pip install --upgrade pacote
```

>É possível realizar a instalação de vários pacotes de uma vez, basta informar o nome deles separados por um espaço em branco: `pip install pacote pacote1 pacote2`

### Ambientes vituais

Ambientes virtuais, como os criados por venv, nos permitem manter as dependências isoladas por projeto, garantindo que bibliotecas, versões e configurações não entrem em conflito entre diferentes aplicações Python.

Isso é especialmente importante quando trabalhamos em múltiplos projetos que utilizam bibliotecas iguais, mas em versões diferentes.

#### 📌 Exemplo prático:
Suponha que você tenha dois projetos que utilizam o framework Django:

- `ecommerce`: utiliza Django 1.10
- `contact-app`: utiliza Django 4.2

Naturalmente, se o Django 1.10 estiver instalado globalmente no sistema, o projeto contact-app (que precisa de recursos da versão 4.2) não funcionará corretamente. E o oposto também é verdadeiro: se a versão 4.2 estiver instalada, o ecommerce pode quebrar, pois depende de uma versão mais antiga.

Sem ambientes virtuais, você teria que constantemente instalar e desinstalar pacotes manualmente para alternar entre os projetos:
```bash
pip uninstall django
pip install django==1.10
# Trabalha com ecommerce

pip uninstall django
pip install django==4.2
# Trabalha com contact-app
```
Além de ser trabalhoso, esse processo é propenso a erros e pode afetar outros projetos em andamento.


#### ✅ A Solução: Ambientes Virtuais
Ambientes virtuais resolvem esse problema criando isolamentos independentes de dependências. Cada ambiente funciona como uma “caixa separada”, com seus próprios pacotes, sem interferir no sistema ou em outros projetos.

Dessa forma:
- `ecommerce` pode ter seu próprio ambiente com Django 1.10
- `contact-app` pode ter outro ambiente com Django 4.2

Ambos podem coexistir na mesma máquina, sem conflitos.

#### Criando ambientes virtuais
Antes de criar um ambiente virtual, vamos verificar quais pacote estão instalados atualmente com `pip list`:
```bash
$ pip list
Package                   Version
------------------------- -----------
altair                    5.5.0
attrs                     25.3.0
azure-core                1.34.0
azure-storage-blob        12.25.1
blinker                   1.9.0
cachetools                5.5.2
certifi                   2025.4.26
cffi                      1.17.1
charset-normalizer        3.4.2
click                     8.1.8
colorama                  0.4.6
cryptography              44.0.3
dotenv                    0.9.9
gitdb                     4.0.12
GitPython                 3.1.44
idna                      3.10
isodate                   0.7.2
Jinja2                    3.1.6
jsonschema                4.23.0
jsonschema-specifications 2025.4.1
MarkupSafe                3.0.2
narwhals                  1.38.0
numpy                     2.2.5
packaging                 24.2
pandas                    2.2.3
pillow                    11.2.1
pip                       22.3.1
protobuf                  6.30.2
pyarrow                   20.0.0
pycparser                 2.22
pydeck                    0.9.1
pymssql                   2.3.4
python-dateutil           2.9.0.post0
python-dotenv             1.1.0
pytz                      2025.2
referencing               0.36.2
requests                  2.32.3
rpds-py                   0.24.0
setuptools                65.5.0
six                       1.17.0
smmap                     5.0.2
streamlit                 1.45.0
tenacity                  9.1.2
toml                      0.10.2
tornado                   6.4.2
typing_extensions         4.13.2
tzdata                    2025.2
urllib3                   2.4.0
watchdog                  6.0.0
```

**Criar um ambiente virtual** 
- O comando `python -m venv nome_ambiente` é responsável por criar um ambiente virtual com o nome especificado.
  - `python -m venv .env`: É uma variação do comando anterior
  - Normalmente, o `nome_ambiente` é o nome do projeto
- `source nome_ambiente/bin/activate`: Esse comadno é utilizado para ativar o ambiente criado
```bash
python3 -m venv nome_ambiente
# OUTRA OPÇÃO 
python -m venv .env

# Para ativar o ambiente
source .env/Scripts/activate
```

Agora com o novo ambiente criado, vamos executar novamente o comando `pip list`:
- Vemos que nesse ambiente não temos nenhum pacote instalado (somente os pacteos do próprio `pip`)
- É possível confirmar que estamos em um ambiente virtual com a presença de `(.env)`
```bash
$ source .env/Scripts/activate
(.env) 

$ pip list
Package    Version
---------- -------
pip        22.3.1
setuptools 65.5.0

[notice] A new release of pip available: 22.3.1 -> 25.2
[notice] To update, run: python.exe -m pip install --upgrade pip
(.env)
```

>Para desativar um ambiente virtual, basta usar o comando `deactivate`

#### Pacotes aninhados
Vale ressaltar que existe pacotes que dependem de outros pacotes. Esses são chamados de pacotes aninhados. 

Isso quer dizer que ás vezes podemos instalar um pacote, mas quando utilizamos `pip list`, alguns pacotes adicionais (que não foram explicitamente instalados) são exibidos. Isso é complementa normal

Por exemplo: Vamos instalar o pacote `Django` e verificar o `pip list`:
- Vemos que além do `Django` (e dos pacotes do pip) existem outros pacotes que foram instalados automaticamente: `asgiref`, `tzdata` e `sqlparse`
```bash
$ pip install Django
Installing collected packages: tzdata, sqlparse, asgiref, Django
Successfully installed Django-5.2.4 asgiref-3.9.1 sqlparse-0.5.3 tzdata-2025.2

$ pip list
Package    Version
---------- -------
asgiref    3.9.1
Django     5.2.4
pip        22.3.1
setuptools 65.5.0
sqlparse   0.5.3
tzdata     2025.2
```

Vale ressaltar que o `pip` não consegue fazer remoção em árvore (excluir um pacote pai e todos seus pacotes aninhados). Então ao desinstalar `Django`, os pacotes aninhados continuarão no ambiente.

Para resolver isso, temos algumas ferramentas interessantes.

## Gerenciamento dependência com pipenv
Pipenv é uma ferramenta de gerenciamento de pacotes que combina a gestão de dependências com a criação de ambiente virtual para seus projetos e adiciona/remove pacotes automaticamente do arquivo Pipfile conforme você instala e desinstala pacotes.

#### Comandos pipenv
Para utilizar o `pipenv`, devemos realizar a instalação do pacote com o comando `pip install pipenv`.

>Vale ressaltar que o `pipenv` deve ser instalado no ambiente global, para que ele possa fazer o gerenciamento de todos os pacotes da máquina.

>Não é comum nem recomendado instalar o pipenv dentro do ambiente virtual que ele mesmo vai gerenciar. Ele deve ser instalado globalmente, fora dos ambientes virtuais

Você pode visualizar todos os comandos utilizando `pipenv`:
```bash
$ pipenv

Options:
  --where                         Output project home information.
  --venv                          Output virtualenv information.
  --py                            Output Python interpreter information.
  --envs                          Output Environment Variable options.
  --rm                            Remove the virtualenv.
  --bare                          Minimal output.
  --man                           Display manpage.
  --support                       Output diagnostic information for use in
                                  GitHub issues.
  --site-packages / --no-site-packages
                                  Enable site-packages for the virtualenv.

  --python TEXT                   Specify which version of Python virtualenv
                                  should use.
  --clear                         Clears caches (pipenv, pip).
  -q, --quiet                     Quiet mode.
  -v, --verbose                   Verbose mode.
  --pypi-mirror TEXT              Specify a PyPI mirror.
  --version                       Show the version and exit.
  -h, --help                      Show this message and exit.


Usage Examples:
   Create a new project using Python 3.7, specifically:
   $ pipenv --python 3.7

   Remove project virtualenv (inferred from current directory):
   $ pipenv --rm

   Install all dependencies for a project (including dev):
   $ pipenv install --dev

   Create a lockfile containing pre-releases:
   $ pipenv lock --pre

   Show a graph of your installed dependencies:
   $ pipenv graph

   Check your installed dependencies for security vulnerabilities:
   $ pipenv check

   Install a local setup.py into your virtual environment/Pipfile:
   $ pipenv install -e .

   Use a lower-level pip command:
   $ pipenv run pip freeze

Commands:
  check         Checks for PyUp Safety security vulnerabilities and against
                PEP 508 markers provided in Pipfile.
  clean         Uninstalls all packages not specified in Pipfile.lock.
  graph         Displays currently-installed dependency graph information.
  install       Installs provided packages and adds them to Pipfile, or (if no
                packages are given), installs all packages from Pipfile.
  lock          Generates Pipfile.lock.
  open          View a given module in your editor.
  requirements  Generate a requirements.txt from Pipfile.lock.
  run           Spawns a command installed into the virtualenv.
  scripts       Lists scripts in current environment config.
  shell         Spawns a shell within the virtualenv.
  sync          Installs all packages specified in Pipfile.lock.
  uninstall     Uninstalls a provided package and removes it from Pipfile.
  update        Runs lock, then sync.
  upgrade       Resolves provided packages and adds them to Pipfile, or (if no
                packages are given), merges results to Pipfile.lock
  verify        Verify the hash in Pipfile.lock is up-to-date.
``` 

> Mas os principais comandos são:
- `pipenv install pacote`: instala um pacote
- `pipenv uninstall pacote`: desinstala um pacote
- `pipenv lock`: Esse comando gera um arquivo *lock* de dependências. 
  - Esse arquivo garante que os pacotes que serão instalados terão a mesma versão das especificadas nesse arquivo.
- `pipenv graph`: Esse comando vai listar todos os pacotes instalados, porém trazendo os pacotes aninhados
- `pipenv clean`: Desisntala todos os pacotes que não estão especificado em `pipfile.lock`
- `pipenv update pacote`: atualiza um pacote instalado
```bash
pip install pipenv
pipenv install pacote
pipenv uninstall pacote
pipenv lock
pipenv graph
pipenv clean
pipenv update pacote
```

>Na prática: O lock lê o arquivo `pipfile` para instalar as versão que ali fora definida.
- O `lock` é transportado quando você passa um projeto para ser executado em outra máquina. Na outra máquina, o python lê esse arquivo e sabe exatamente qual versão de pacotes ele deve instalar

### Exemplo com pipenv

>Vamos usar o mesmo exemplo de antes: Instalar o pacote `django` e verificar como o pipenv se comporta ao desinstalar:
- Quando instalamos um pacote, o `pipenv`:
1. Cria o Pipfile (se não existir)
2. Cria ou atualiza o Pipfile.lock com as versões exatas
3. Instala o pacote (nesse caso, o django) e todas as dependências dele
4. Garante que o ambiente está sincronizado
5. Usa um ambiente virtual (criado ou detectado)
```bash
$ pipenv install django
Courtesy Notice:
Pipenv found itself running within a virtual environment,  so it will automatically use that environment, instead of  creating its own for any project. You 
can set
PIPENV_IGNORE_VIRTUALENVS=1 to force pipenv to ignore that environment and create  its own instead.
You can set PIPENV_VERBOSITY=-1 to suppress this warning.
Creating a Pipfile for this project...
Pipfile.lock not found, creating...
Locking  dependencies...
Locking  dependencies...
Updated Pipfile.lock (ed6d5d614626ae28e274e453164affb26694755170ccab3aa5866f093d51d3e4)!
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
Installing django...
Installation Succeeded
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
Installing dependencies from Pipfile.lock (51d3e4)...
All dependencies are now up-to-date!
Upgrading django in  dependencies.
Building requirements...
Resolving dependencies...
Success!
To activate this project's virtualenv, run pipenv shell.                                                                                                    
Alternatively, run a command inside the virtualenv with pipenv run.
Installing dependencies from Pipfile.lock (8362fc)...
All dependencies are now up-to-date!
Installing dependencies from Pipfile.lock (8362fc)...
(.env) 
```

#### Pipefile
Este é o arquivo de configuração principal do projeto. Ele substitui o tradicional `requirements.txt`. Nele são armazenadas:
- As dependências do seu projeto (bibliotecas que você instala com pipenv install).
- As dependências de desenvolvimento (como ferramentas de teste ou linting, instaladas com pipenv install --dev).
- A versão do Python usada no ambiente virtual.
- A fonte de pacotes (geralmente o PyPI).
- `django = '*'`: Essa linha indica que a versão do django que deverá ser utilizada será a mais atual. 
```bash
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
django = "*"

[dev-packages]

[requires]
python_version = "3.11"
```
#### Pipefile.lock
Este arquivo é gerado automaticamente quando você instala ou altera dependências. Ele garante que todos os ambientes sejam reprodutíveis, especificando versões exatas de todas as bibliotecas e suas dependências recursivas.

>Por padrão, o arquivo `Pipefile.lock` é gerado automaticamente, mas é possível criá-lo manualmente com o comando `pipenv lock`

**O que é armazenado no `Pipfile.lock`:**
- Versões exatas e congeladas de todas as dependências (inclusive as internas).
- Hashes criptográficos dos pacotes, garantindo integridade e segurança.
- As dependências são separadas em [default] e [develop], assim como no Pipfile.

**Por que ele é importante?**
- Garante que todo mundo use as mesmas versões de pacotes (evita o famoso “funciona na minha máquina”).
- Ideal para ambientes de produção, testes e CI/CD.
- Protege contra updates quebrados de dependências indiretas.
```json
{
    "_meta": {
        "hash": {
            "sha256": "af42abefb766e975f7680f10368735353569fb4fe0114e59496a7202658362fc"
        },
        "pipfile-spec": 6,
        "requires": {
            "python_version": "3.11"
        },
        "sources": [
            {
                "name": "pypi",
                "url": "https://pypi.org/simple",
                "verify_ssl": true
            }
        ]
    },
    "default": {
        "asgiref": {
            "hashes": [
                "sha256:a5ab6582236218e5ef1648f242fd9f10626cfd4de8dc377db215d5d5098e3142",
                "sha256:f3bba7092a48005b5f5bacd747d36ee4a5a61f4a269a6df590b43144355ebd2c"
            ],
            "markers": "python_version >= '3.9'",
            "version": "==3.9.1"
        },
        "django": {
            "hashes": [
                "sha256:60c35bd96201b10c6e7a78121bd0da51084733efa303cc19ead021ab179cef5e",
                "sha256:a1228c384f8fa13eebc015196db7b3e08722c5058d4758d20cb287503a540d8f"
            ],
            "index": "pypi",
            "markers": "python_version >= '3.10'",
            "version": "==5.2.4"
        },
        "sqlparse": {
            "hashes": [
                "sha256:09f67787f56a0b16ecdbde1bfc7f5d9c3371ca683cfeaa8e6ff60b4807ec9272",
                "sha256:cf2196ed3418f3ba5de6af7e82c694a9fbdbfecccdfc72e281548517081f16ca"
            ],
            "markers": "python_version >= '3.8'",
            "version": "==0.5.3"
        },
        "tzdata": {
            "hashes": [
                "sha256:1a403fada01ff9221ca8044d701868fa132215d84beb92242d9acd2147f667a8",
                "sha256:b60a638fcc0daffadf82fe0f57e53d06bdec2f36c4df66280ae79bce6bd6f2b9"
            ],
            "markers": "python_version >= '2'",
            "version": "==2025.2"
        }
    },
    "develop": {}
}
```

| Arquivo        | Finalidade principal                                               |
| -------------- | ------------------------------------------------------------------ |
| `Pipfile`      | Lista de dependências desejadas (o que você quer instalar)         |
| `Pipfile.lock` | Registra versões exatas e seguras (o que exatamente foi instalado) |


#### Instalando e desistalando pacotes
Antes de desistalar o pacote django, vamos visualizar os pacotes instalados com o comando `pipenv graph`
- Repare que ele traz as dependências aninhadas de `django` em forma de "árvore". É muito mais simples de visualizar:
```bash
$ pipenv graph
Django==5.2.4
├── asgiref 
├── sqlparse 
└── tzdata 
```
Agora, podemos executar o comando `pipenv unistall django` para remover o pacote:
```bash
$ pipenv uninstall django
Removed django from Pipfile.
Uninstalling django...
Found existing installation: Django 5.2.4
Uninstalling Django-5.2.4:
  Successfully uninstalled Django-5.2.4
```

>Então os pacotes aninhados foram excluiídos também?
- A resposta é **não**. Podemos executar o comando `pipenv graph` novamente e verificar que os pacotes aninhados do django ainda estão lá, mas agora estão "soltos":
```bash
$ pipenv graph
sqlparse==0.5.3
tzdata==2025.2
asgiref==3.9.1
``` 

>Então não é possível exclui-las com o `pipenv`?
- É totalmente possível. O `pipenv` possui um comando que exclui todos os pacotes que não estão especificados em `Pipefile`.
- Se verificarmos o arquivo `Pipefile` após excluir o pacote django, veremos que não possui nenhum pacote:
```bash
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]

[dev-packages]

[requires]
python_version = "3.11"
```

Então, podemos executar `pipenv clean` que todas os pacotes "soltos" serão excluídos:
```bash
$ pipenv clean
Courtesy Notice:
Pipenv found itself running within a virtual environment,  so it will automatically use that environment, instead of  creating its own for any project. You 
can set
PIPENV_IGNORE_VIRTUALENVS=1 to force pipenv to ignore that environment and create  its own instead.
You can set PIPENV_VERBOSITY=-1 to suppress this warning.
Uninstalling asgiref...
Uninstalling tzdata...
Uninstalling sqlparse...
```
 
-----------------------------------------------------------------------------

## Gerenciando pacotes com Poetry

Poetry é outra ferramenta de gerenciamento de dependências para Python que permite declarar as bibliotecas de que seu projeto depende e gerencia (instala/atualiza/remove) essas bibliotecas para você. Ela também suporta o empacotamento e a publicação de projetos no PyPI.

#### Comandos do poetry
Para utilizar o `poetry`, devemos realizar a instalação do pacote com o comando `pip install poetry`.

>Assim como o `pipenv`, o poetry deve ser instalado globalmente

Com o comando `poetry`, podemos verificar todos os comandos utilizados:
```bash
$ poetry
Poetry (version 2.1.4)

Usage:
  command [options] [arguments]

Options:
  -h, --help                 Display help for the given command. When no command is given display help for the list command.
  -q, --quiet                Do not output any message.
  -V, --version              Display this application version.
      --ansi                 Force ANSI output.
      --no-ansi              Disable ANSI output.
  -n, --no-interaction       Do not ask any interactive question.
      --no-plugins           Disables plugins.
      --no-cache             Disables Poetry source caches.
  -P, --project=PROJECT      Specify another path as the project root. All command-line arguments will be resolved relative to the current working directory.
  -C, --directory=DIRECTORY  The working directory for the Poetry command (defaults to the current working directory). All command-line arguments will be resolved relative to the given directory.
  -v|vv|vvv, --verbose       Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug.

Available commands:
  about              Shows information about Poetry.
  add                Adds a new dependency to pyproject.toml and installs it.       
  build              Builds a package, as a tarball and a wheel by default.
  check              Validates the content of the pyproject.toml file and its consistency with the poetry.lock file.
  config             Manages configuration settings.
  help               Displays help for a command.
  init               Creates a basic pyproject.toml file in the current directory.  
  install            Installs the project dependencies.
  list               Lists commands.
  lock               Locks the project dependencies.
  new                Creates a new Python project at <path>.
  publish            Publishes a package to a remote repository.
  remove             Removes a package from the project dependencies.
  run                Runs a command in the appropriate environment.
  search             Searches for packages on remote repositories.
  show               Shows information about packages.
  sync               Update the project's environment according to the lockfile.    
  update             Update the dependencies as according to the pyproject.toml file.
  version            Shows the version of the project or bumps it when a valid bump rule is provided.

 cache
  cache clear        Clears a Poetry cache by name.
  cache list         List Poetry's caches.

 debug
  debug info         Shows debug information.
  debug resolve      Debugs dependency resolution.
  debug tags         Shows compatible tags for your project's current active environment.

 env
  env activate       Print the command to activate a virtual environment.
  env info           Displays information about the current environment.
  env list           Lists all virtualenvs associated with the current project.     
  env remove         Remove virtual environments associated with the project.       
  env use            Activates or creates a new virtualenv for the current project. 

 python
  python install     Install the specified Python version from the Python Standalone Builds project. (experimental feature)
  python list        Shows Python versions available for this environment. (experimental feature)
  python remove      Remove the specified Python version if managed by Poetry. (experimental feature)

 self
  self add           Add additional packages to Poetry's runtime environment.       
  self install       Install locked packages (incl. addons) required by this Poetry installation.
  self lock          Lock the Poetry installation's system requirements.
  self remove        Remove additional packages from Poetry's runtime environment.  
  self show          Show packages from Poetry's runtime environment.
  self show plugins  Shows information about the currently installed plugins.       
  self sync          Sync Poetry's own environment according to the locked packages (incl. addons) required by this Poetry installation.
  self update        Updates Poetry to the latest version.

 source
  source add         Add source configuration for project.
  source remove      Remove source configured for the project.
  source show        Show information about sources configured for the project. 
```

>Mas os principais comandos são:
- `poetry new`: Criando um novo projeto
- `poetry init`: Inicia um novo projeto de maneira interativa
- `cd novo_projeto`: Acessando o diretório do novo projeto
- `poetry add pacote`: Adicionando pacote
- `poetry remove pacote`: Removendo pacote
- `poetry show`: Lista os pacotes instalados no ambiente
  - `poetry show -t`: Lista os pacotes instalados em forma de árvore
- `poetry install`: Instala os pacotes
- `poetry update pacote`: Atualiza um pacote
```bash
pip install poetry # instalando o poetry

poetry new novo_projeto
cd novo_projeto
poetry add pacote
poetry remove pacote
poetry show
poetry install
```

### Criando um projeto
O poetry permite criar um projeto do 0 de maneira interativa com o comando `poetry init`. Esse comando é usado para criar o arquivo de configuração pyproject.toml do seu projeto Python. Esse arquivo substitui o requirements.txt e setup.py, centralizando todas as informações do projeto e suas dependências.

```bash
$ poetry init

This command will guide you through creating your pyproject.toml config.

Package name [6 - trabalhando com pacotes python]:  teste
Version [0.1.0]:  
Description []:  
Author [Mateus Ferreira <mateusf63@gmail.com>, n to skip]:  
License []:  
Compatible Python versions [>=3.11]:  

Would you like to define your main dependencies interactively? (yes/no) [yes]
        You can specify a package in the following forms:
          - A single name (requests): this will search for matches on PyPI
          - A name and a constraint (requests@^2.23.0)
          - A git url (git+https://github.com/python-poetry/poetry.git)
          - A git url with a revision         (git+https://github.com/python-poetry/poetry.git#develop)
          - A file path (../my-package/my-package.whl)
          - A directory (../my-package/)
          - A url (https://example.com/packages/my-package-0.1.0.tar.gz)

Package to add or search for (leave blank to skip): django
Found 342 packages matching django
Showing the first 10 matches

Enter package # to add, or the complete package name if it is not listed []:
 [ 0] django
 [ 1]
 > 0
0
Enter the version constraint to require (or leave blank to use the latest version): 
Using version ^5.2.4 for django

Add a package (leave blank to skip):

Would you like to define your development dependencies interactively? (yes/no) [yes] no
Generated file

[project]
name = "teste"
version = "0.1.0"
description = ""
authors = [
    {name = "Mateus Ferreira",email = "mateusf63@gmail.com"}
]
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
    "django (>=5.2.4,<6.0.0)"
]


[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"


Do you confirm generation? (yes/no) [yes] yes
```
> Vamos entender o que está acontecendo?
- OBS: Para usar um valor padrão, basta presssionar `enter`

#### Nome, versão, descrição, autor, etc:
| Pergunta                    | Resposta |
| --------------------------- | -------------------------------------------------------------- |
| Nome do pacote              | `teste`                            |
| Versão                      | usou a padrão `0.1.0`                                          |
| Descrição                   | deixou em branco                                               |
| Autor                       | aceitou o valor padrão `Mateus Ferreira <mateusf63@gmail.com>` |
| Licença                     | deixou em branco                                               |
| Versão compatível do Python | usou a padrão `>=3.11`                                      |

#### Adicionar dependências:
```bash
Would you like to define your main dependencies interactively? (yes/no) [yes]

# solicita o nome do pacote
Package to add or search for: django

Found 342 packages matching django
Showing the first 10 matches

Enter package # to add, or the complete package name if it is not listed []:
 [ 0] django
 [ 1]
 > 0
```
- A resposta é sim, então ele solicita o nome do pacote (`django`). 
- Com isso, ele mostrou os primeiros resultados encontrados no `PyPi`
- Escolhi o `django` (posição número 0)

```bash
Enter the version constraint to require (or leave blank to use the latest version):
```
- Deixamos em branco, então ele usou a versão mais recente disponível naquele momento

#### Dependências de desenvolvimento
```bash
Would you like to define your development dependencies interactively? [yes]
```
- Respondemos `no`, ou seja, não quis adicionar nenhuma dependência de desenvolvimento neste momento.

#### Geração do pyproject.toml
```bash
[project]
name = "teste"
version = "0.1.0"
description = ""
authors = [
    {name = "Mateus Ferreira", email = "mateusf63@gmail.com"}
]
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
    "django (>=5.2.4,<6.0.0)"
]

[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"
```
> Esse arquivo agora define o projeto e suas dependências, sendo o equivalente moderno do setup.py + `requirements.txt`.

#### Confirmação
- Aqui finalizamos a criação com o comando `yes`.
- Em seguida, para instalar as dependências basta usar o comando `poetry install`
```bash
Do you confirm generation? (yes/no) [yes]

$ poetry install # instalando
```

#### Gerenciando dependências
O comando `poetry show` permite visualizar todos os pacotes instalados. Com a flag `-t`, é possível visualizar em formato de árvore, útil para visualizar dependências aninhadas.

>É possível utilizar a flag `--help` para verificar possíveis parâmetros de um comando: `comando --help` 
```bash
$ poetry show -t
django 4.2.4 A high-level Python web framework that encourages rapid development and clean, pragmatic design.
|__ asgiref >=3.6.0,<4
|__ sqlparse >=0.3.1
|__ tzdata *
```

**Removendo pacote**<br>
Com o poetry, ao excluir um pacote que possui dependências aninhadas (como o django), elas também são excluídas:
```bash
$ poetry remove django
Updating dependencies
Resolving dependencies... (0.15)

Writing lock file

Package operations: installs, updates, 3 removals
  Removing asgiref (3.7.2)
  Removing django (4.2.4)
  Removing sqlparse (0.4.4)
```

<br>

## Boas práticas

Python tem uma série de convenções e melhores práticas codificadas em PEPs (Propostas de Melhoria do Python). A mais conhecida destas é provavelmente a PEP 8, que cobre o estilo de codificação.

O propósito da PEP 8 é definir um conjunto de recomendações e convenções de codificação para o código Python.

> O [PEP 8](https://peps.python.org/pep-0008/) é o guia de estilo para codificação em Python. Ele inclui convenções sobre nomes de variáveis, uso de espaços em branco, comprimento da linha e muitas outras coisas que ajudam a manter o código Python consistente e legível.

#### Principais recomendações

A PEP 8 possui diversos tópicos, mas vamos listar as mais importantes.

Algumas das principais recomendações da PEP 8 incluem: 
- usar 4 espaços para a identação
- limitar as linhas a 79 caracteres
- usar nomes de variáveis em `snake_case` para funções e variáveis, e `CamelCase` para classes.

**Exemplo**
```py
def somar(argumento_1, argumento_2):
    # Esta é uma função de exemplo seguindo a pep 8
    pass

class ContaBancaria:
    # Esta é uma classe de exemplo seguindo a pep 8
    pass
```

### Ferramentas úteis
Abaixo algumas ferramentas úteis para nos ajudar a manter o código dentro do padrão especificado na PEP 8.

#### Uso de ferramentas de checagem de estilo

Em alguns casos, o código pode ficar muito grande e difícil de checar.
Para nos ajudar a seguir as recomendações da PEP 8, podemos usar ferramentas de checagem de estilo como `flake8`. Essas ferramentas verificam nosso código e nos informam onde estamos desviando do guia de estilo.

>Ferramentas de inspeção são chamadas de *linter*

Para instalar o `flake8`, podemos usar o comando: `pip install flake8`.
- Em seguida, usamos o comando `flake8 nome_arquivo.py` para que ele faça um relatório do que está certo/errado no código.
```bash
pip install flake8
flake8 meu_codigo.py
```

>Vale ressaltar que o `flake8` apenas inspeciona o código e faz um relatório, você ainda precisará realizar as mudanças manualmente.

#### Formatação automática de código
Black é uma ferramenta de formatação de código Python que segue a filosofia "formato único". Black reformata todo o seu arquivo em um estilo consistente, simplificando a tarefa de manter o código em conformidade com a PEP 8.

Para instalá-lo, podemos usar o comando: `pip install black`. 
- Em seguida, utilizamos o comando `black meu_codigo.py` para que ele analise e faça mudanças no código
```bash
pip install black
black meu_codigo.py
```

#### Organização de imports com isort

A PEP 8 também define regras para imports do código. O `isort` ajuda a manter essa seção organizada.

Isort é uma ferramenta Python para classificar importações alfabeticamente e separá-las automaticamente em seções. Ele proporciona uma maneira rápida e fácil de ordenar e categorizar suas importações.

>O isort também é um formatador, porém focado em imports.

Para instalá-lo, podemos usar o comando: `pip install isort`. 
- Em seguida, utilizamos o comando `isort meu_codigo.py` para que ele analise e faça mudanças no código
```bash
pip install isort
isort meu_codigo.py
```

>É possível instalar plugins no VSCode para manter o código organizado sem a necessidade de executar nenhum comando. Este é o nome deles no VSCode:
- Black Formatter
- isort

### Exemplo de código
Por exemplo, veja esse código como exemplo: de acordo com a PEP 8, ele possui alguns erros:
- Os imports estão com a ordem incorreta
- A variável `a` não possui um espaço na atribuição
- A lista `frutas` está declarada com aspas simples (') e está muito grande na horizontal
- A lista `carros` está com uma formatação incorreta (índices desorganizados)
```py
import sys
import os

a= "python"

frutas=['pera','maçã', 'laranja', 'uva', 'melão', 'morango', 'abacate' 'banana', 'carambola', 'pessego', 'tamara', 'melancia']

carros = ["ferrari", 
"brasilia", 
"gol", "up"
]
```

Agora, vamos executar o comando `flake8` para inspecionar esse código:
```bash
$ flake8 exemplo.py
exemplo.py:1:1: F401 'sys' imported but unused
exemplo.py:2:1: F401 'os' imported but unused
exemplo.py:4:2: E225 missing whitespace around operator
exemplo.py:6:7: E225 missing whitespace around operator
exemplo.py:6:15: E231 missing whitespace after ','
exemplo.py:6:80: E501 line too long (126 > 79 characters)
exemplo.py:8:21: W291 trailing whitespace
exemplo.py:9:1: E128 continuation line under-indented for visual indent
exemplo.py:9:12: W291 trailing whitespace
exemplo.py:10:1: E128 continuation line under-indented for visual indent
exemplo.py:11:1: E124 closing bracket does not match visual indentation
exemplo.py:11:2: W292 no newline at end of file
``` 

>OBS: Repare como o `flake8` inspecionou um erro no tamanho de uma linha (`E501 line too long (126 > 79 characters)`). Por padrão, `flake8` considera o tamanho de uma linha com 79 caracteres, mas existem desenvolvedores que utilizam padrões maiores (como 120, por exemplo). É possível aumentar o número máximo de linha no `flake8` com o parâmetro: `flake8 --max-line-length=120 exemplo.py`. Assim, ele irá considerar somente as linhas que excedem esse valor

Agora, vamos executar os comandos `black`, `isort` e verificar o resultado:
```bash
$ black exemplo.py
reformatted exemplo.py

All done! ✨ 🍰 ✨
1 file reformatted.

$ isort exemplo.py 
Fixing C:\Workspaces\Python\ws-bootcam-santander\bootcamp-santander-python\6 - Trabalhando com Pacotes Python\4 - Gerenciamento de pacotes, convenções e boas práticas\exemplo.py
```

**Código ajustado**
- Repare como os imports foram ajustados e o código foi formatado de maneira mais elegante e padronizada.
```py
import os
import sys

a = "python"

frutas = [
    "pera",
    "maçã",
    "laranja",
    "uva",
    "melão",
    "morango",
    "abacate" "banana",
    "carambola",
    "pessego",
    "tamara",
    "melancia",
]

carros = ["ferrari", "brasilia", "gol", "up"]
```

<br>

------------------------------------------------------------

<br>

## Desafio

Fazer o uso do `black`, `flake8` e `isort` para ajustar o sistema bancário (desenvolvido nos desafios anteriores)