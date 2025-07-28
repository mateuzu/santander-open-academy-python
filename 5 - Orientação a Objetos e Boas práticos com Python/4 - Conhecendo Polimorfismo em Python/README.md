# Conhecendo polimorfismo em Python

Objetivo: Aprender a criar classes polimórficas com Python

## O que é polimorfismo?

A palavra polimorfismo significa ter muitas formas. Na programação, polimorfismo significa o mesmo nome de função (mas assinaturas diferentes) sendo usado para tipos diferentes.

Um exemplo de polimorfismo já visto nos nossos exemplos é a função `len()`:
- Ele é um bom exemplo de polimorfismo pois conseguimos utilizar diversos tipos diferentes como parâmetro e, para cada tipo, ele se comporta de uma maneira diferente
  - `len("python")`: Vai contar a quantidade de letras existentes na palavra python
  - `len([10, 20, 30])`: Vai contar a quantidade de elementos da lista
```py
len("python") # 5
len([10, 20, 30]) # 3
```

------------------------------------------------

## Polimorfismo com herança

Na herança, a classe filha herda os métodos da classe pai. No entanto, é possível modificar um método em uma classe filha herdada da classe pai. 

Isso é particularmente útil nos casos em que o método herdado da classe pai não se encaixa perfeitamente na classe filha. Com isso, a classe filha pode sobrescrever o método com uma implementação de acordo com as suas necessidades.

#### Exemplo
No exemplo abaixo, vemos uma sobrescrita de método.
- A classe `Passaro` possui a assinatura de um método `voar`. Nesse classe, esse método não possui nenhuma lógica implementada, é um método vazio onde a implementação dependerá de quem herdar.
- `Pardal`: Essa classe herda `Passaro`. Em seguida, o método `voar` é declarado novamente, mas dessa vez com uma implementação concreta, exibindo a mensagem "Pardal voa".
- `Avestruz`: Essa classe também herda `Passaro`. O método `voar` também foi declarado e implementado, mas com uma mensagem diferente: "Avestruz NÃO voa"
- `def plano_de_voo(passaro)`: Em seguida, criamos uma função que recebe um `passaro` como parâmetro (ou seja, pode ser um `Pardal` ou `Avestruz`). A função desse método é simplesmente delegar a execução do método `voar` para o objeto repassado como parâmetro. Em seguida, repassamos um `Pardal` e um `Avestruz` para verificarmos a diferença no resultado.
```py
class Passaro:
    def voar(self): pass

class Pardal(Passaro):
    def voar(self): 
        print("Pardal voa")

class Avestruz(Passaro):
    def voar(self): 
        print("Avestruz não voa")

def plano_de_voo(passaro):
    passaro.voar()

plano_de_voo(Pardal()) # Pardal voa
plano_de_voo(Avestruz()) # Avestruz não voa
```