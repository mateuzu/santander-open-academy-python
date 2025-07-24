# Aprendendo a utilizar dicionários

Conhecer e entender o funcionamento da estrutura de dados dicionário em Python, bem como seus métodos úteis.

--------------------------------------------------------------------------------------------

## Criação e acesso aos dados

Um dicionário é um conjunto não-ordenado de pares chave:valor, onde as chaves são únicas em uma dada instância do dicionário. Dicionários são delimitados por chaves: {}, e contém uma lista de pares chave:valor separada por vírgulas.
- Chave: Sempre deve ser um objeto imutável (tupla, string, etc)
- Valor: Pode ser qualquer tipo de objeto (mutável ou imutável)

```py
pessoa {"nome": "Mateus", "idade":22} # Criando com {}

pessoa = dict(nome="Mateus", idade=22) # Criando com construtor dict()

pessoa["telefone"] = "1234-5678" # Adicionando uma chave à um dicionário existente

print(pessoa)
>>> {"nome":"Mateus", "idade":28, "telefone":" 1234-5678"}
```

#### Acesso aos dados
- Para acessar os dados de um dicionário, basta utilizar a chave do valor desejado, seguindo a sintaxe: `dicionario[chave]`
- **Alterar valo**: A sintaxe para alterar é semelhante, a diferença é que incluímos o operador de atribuição para inserir um novo valor: `dicionario[chave] = "novo valor"`
    - O dicionário não permite chaves duplicadas, então se você atribuir valor para uma chave que já existe, ele vai alterar o valor presente na chave
```py
dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

# Acessando valores
dados["nome"] # "Guilherme"
dados["idade"] # 28
dados["telefone"] # "3333-1234"

# Alterando valores
dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "9988-1781"

print(dados)
>>> {"nome": "Maria", "idade": 18, "telefone": "9988-1781"}
```

#### Dicionários aninhados
Dicionários podem armazenar qualquer tipo de objeto Python como valor, desde que a chave para esse valor seja um objeto imutável como (strings e números). Ou seja, um dicionário pode armazenar outro dicionário, criando assim um dicionário aninhado
- No exemplo abaixo, estamos criando um dicionário de contatos. A chave do dicionário é o e-mail (de um cliente, por exemplo) e o valor dessa chave é outro dicionário contendo os dados de nome e telefone. 
- Nesse caso, para acessar os dados precisamos passar a 1° chave (que seria o e-mail) e em seguida a chave da propriedade que queremos acessar: `dicionario[chave_1][chave_2]`,
    - Para acessar o telefone: `dicionario[email@gmail.com][telefone]` Isso vai retornar o telefone do cliente que tem o e-mail `email@gmail.com`
    - Para acessar o nome: `dicionario[email@gmail.com][nome]` Isso vai retornar o nome do cliente que tem o e-mail `email@gmail.com`
```py
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

contatos["giovanna@gmail.com"]["telefone"] # "3443-2121"
```

>Vale ressaltar que é possível aninhar vários dicionários. A lógica para acessar os dados é a mesma, utilizando a chave das propriedades que deseja acessar.
- Por exemplo, imagine que existe um outro dicionário com o nome de `endereco`. Agora, queremos acessar o valor da `rua` do cliente que tem o e-mail `melaine@gmail.com`: 
```py
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"} "endereco": {"rua": "Rua A", "numero": 20},
}

# Para ficar mais claro, vamos retornar por partes, retornando um dicionário de cada vez
rua_melanie = contatos[melaine@gmail.com] # {"nome": "Melaine", "telefone": "3333-7766"} "endereco": {"rua": "Rua A", "numero": 20} -> Aqui, retornamos o dicionário inteiro
rua_melanie = contatos[melaine@gmail.com]["endereco"] # {"rua": "Rua A", "numero": 20} -> Aqui, retornamos o subdicionário que possui propriedades do endereco
rua_melanie = contatos[melaine@gmail.com]["endereco"]["rua"] # "Rua A" -> Aqui, retornamos o valor que está armazenado na chave "rua"
``` 

#### Iterar dicionários

A forma mais comum para percorrer os dados de um dicionário é utilizando o comando for. Existem duas maneiras principais:
- iterando sobre cada chave e exibindo o valor que pertence a chave iterada:
```py
for chave in contatos:
    print(chave, contatos[chave])

# guilherme@gmail.com {'nome': 'Guilherme', 'telefone': '3333-2221'}
# giovanna@gmail.com {'nome': 'Giovanna', 'telefone': '3443-2121'}
# chappie@gmail.com {'nome': 'Chappie', 'telefone': '3344-9871'}
#melaine@gmail.com {'nome': 'Melaine', 'telefone': '3333-7766'}
```
- utilizando o método `.items()` que retorna uma lista de tuplas. Nessa lista de tuplas. o 1° argumento é a chave e o 2° é o valor, com isso podemos acessar as propriedades:
```py
for chave, valor in contatos.items():
    print(chave, valor)

# guilherme@gmail.com {'nome': 'Guilherme', 'telefone': '3333-2221'}
# giovanna@gmail.com {'nome': 'Giovanna', 'telefone': '3443-2121'}
# chappie@gmail.com {'nome': 'Chappie', 'telefone': '3344-9871'}
#melaine@gmail.com {'nome': 'Melaine', 'telefone': '3333-7766'}
```

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Métodos da classe dict

Alguns métodos úteis da classe dict

#### {}.clear
- Esse método limpa o dicionário
```py
contatos = {
"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
"chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}
contatos.clear()

contatos # {}
```

#### {}.copy
- Esse método cria um cópia dos valores presentes em um dicionário
```py
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

copia = contatos.copy()
copia["guilherme@gmail.com"] = { "nome": "Gui"} # Alterando os valores da copia

contatos["guilherme@gmail.com"] # {"nome": "Guilherme", "telefone": "3333-2221"}

copia["guilherme@gmail.com"] # {"nome": "Gui"}
```


#### {}.fromkeys
- Esse método cria chaves em um dicionário. É possível criar as chaves com ou sem valor padrão definido. Vale ressaltar que o parâmetro do método é uma lista de chaves (tem que ser objetos imutáteis)
```py
dict.fromkeys(["nome", "telefone"]) # Criando as chaves nome e telefone sem valor

dict.fromkeys(["nome", "telefone"], "vazio") # Criando as chaves nome e telefone com o valor "vazio"
``` 

#### {}.get
- Esse método é utilizado para acessar valores dentro do dicionário. Recebe como parâmetro o nome da chave do valor que será buscado. 
    - Além disso, é possível passar um 2° parâmetro que será retornado caso a chave repassada não exista: `dicionario.get("chave", {})`, nesse caso se "chave" não existir, será retornado um `{}` vazio.
- Diferente do acesso direto `dicionario[chave]`, o método `get` NÃO dá erro quando passamos uma chave que não existe.
```py
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

contatos ["chave"] # KeyError -> O acesso direto lança exceção quando a chave não existe
contatos.get("chave") # None -> O get não da erro

contatos.get("chave", {}) # {} -> Se a chave não existir, será retornado um dicionário vazio {}

contatos.get("guilherme@gmail.com", {}) # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
```

#### {}.items
- Esse método retorna uma lista de tuplas do dicionário. É útil para utilizar no laço for
```py
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

contatos.items() # dict_items([('guilherme@gmail.com', 'nome': 'Guilherme','telefone': '3333-2221'})])
```

#### {}.keys
- Esse método retorna todas as chaves existentes em um dicionário
```py
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

contatos.keys() # dict_keys(['guilherme@gmail.com'])
```

#### {}.pop
- Esse método vai remover um valor do dicionário com base na chave. Assim como o método `get`, se a chave não existir, é possível repassar um retorno padrão
- É útil para remover valores que você não tem certeza se existem
```py
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

contatos.pop("guilherme@gmail.com") # {'nome': 'Guilherme', 'telefone':'3333-2221'} -> O pop retorna o valor que foi removido
contatos.pop("guilherme@gmail.com", "nao encontrou") # nao encontrou
```

#### {}.popitem
- Esse método é muito parecido com o `.pop`, porém não recebe nenhuma chave como parâmetro. Por conta disso, ele remove na sequência deo inicio para o final. Se não existir nenhum elemento no dicionário, ele vai lançar um erro
```py
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

contatos.popitem() # ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone':'3333-2221'})
contatos.popitem() # KeyError
```

#### {}.setdefault
- Esse método é utilizado para definir uma chave/valor para um dicionpario caso a chave NÃO exista. Se a chave existir, esse método NÃO substitui o valor, ele simplesmente mantém o valor que já estava.
- É útil para adicionar valores caso a chave não exista, sem a necessidade de verificar todas as chaves 
```py
contato = {'nome': 'Guilherme', 'telefone': '3333-2221'}
contato.setdefault("nome", "Giovanna") # "Guilherme" -> Chave nome já existe, então o valor continua como está

contato # {'nome': 'Guilherme', 'telefone': '3333-2221'} -> Não trocou o nome, pois a chave ja existia

contato.setdefault("idade", 28) # 28 -> chave idade não existe, então será criada com o valor passado no argumento: 28

contato # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28} -> Adicionou a chave idade com o valor 28
``` 


#### {}.update
- Esse método atualiza um dicionário com outro dicionário. Quando fazemos um update com uma chave que já existe, ele atualiza o valor do dicionário original pelo dicionário passado como parâmetro. Se não existir, ele adiciona o novo dicionário ao original
```py
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

contatos.update({"guilherme@gmail.com": {"nome": "Gui"}}) # chave guilherme@gmail.com já existe, então ele vai atualizar a subchave com o nome ed Gui
contatos # {'guilherme@gmail.com': {'nome': 'Gui'}} -> atualizou o nome

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}}) # chave giovanna@gmail.com não existe, então ele vai adicionar esse dicionário ao original
contatos # {'guilherme@gmail.com': {'nome': 'Gui'), 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}} -> novo dicionário adicionado
```

#### {}.values
- Esse método retorna todos os valores (assim como o `keys` retorna todas as chaves, `values` retorna todos os valores)
```py
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

contatos.values() # dict_values([{'nome': 'Guilherme', 'telefone':'3333-2221'}, {'nome': 'Giovanna', 'telefone': '3443-2121'}, {'nome': 'Chappie','telefone': '3344-9871'}, {'nome': 'Melaine', 'telefone': '3333-7766'}])
```

#### in
- O `in` é usado para verificar uma chave existe ou não em um dicionário.
```py
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

"guilherme@gmail.com" in contatos # True
"megui@gmail.com" in contatos # False
"idade" in contatos ["guilherme@gmail.com"] # False
"telefone" in contatos ["giovanna@gmail.com"] # True
```

> A titulo de curiosidade: Se o operador `in` não existisse, seria necessário capturar todas as chaves de um dicionário e utilizar algum método auxiliar de list (`count` ou `indez`) para verificar a ocorrência da chave:
```py
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# Convertendo as chaves para lista
lista_chaves: list = contatos.keys()
count = lista_chaves.count("guilherme@gmail.com")

if count > 0:
    # Se a chave existir, faremos alguma lógica específica
```

#### {}.del
- Esse método exclui um objeto de um dicionário, podendo ser uma chave, dicionário aninhado ou o próprio dicionário
```py
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

del contatos ["guilherme@gmail.com"]["telefone"] # Excluindo a chave 'telefone' do dicionário 'guilherme@gmail.com'
del contatos ["chappie@gmail.com"] # Excluindo o dicionário 'chappie@gmail.com' inteiro
del contatos # Exclui o dicionário 'contatos' inteiro
```
