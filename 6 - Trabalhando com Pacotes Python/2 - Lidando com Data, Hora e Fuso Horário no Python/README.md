# Lidando com Data, Hora e Fuso Horário no Python

Objetivo: Aprender a trabalhar com datas, horas e fusos horários em Python, dominando o módulo 'datetime' para manipulações precisas.

Contéudo
- Introdução ao módulo datetime
- Manipulação de datas e horas
- Conversão e formatação de datas e horas
- Trabalhando com timezones

## Introdução ao módulo datetime

O módulo `datetime` em Python é usado para lidar com datas e horas. Ele possui várias classes úteis como date, time e timedelta.

Para usá-lo basta realizar a importação com a linha `import datetime` ou `from datetime import` (esse segundo é utilizado de maneira ligeiramente diferente, confira no exemplo)

>Sempre confira a documentação da linguagem. Clique [aqui](https://docs.python.org/3/library/datetime.html) para verficar a documentação do módulo `datetime`

#### Objeto date()
- O objeto date representa uma data (ano, mês e dia) em um calendário idealizado, o atual calendário Gregoriano estendido indefinidamente em ambas as direções.
- `date(ano, mes, dia)` permite criar um objeto `date` com a data que foi utilizda como parâmetro (nesse caso: 19/07/2023). 
- O construtor do `date` possui diversas validações para os parâmetros, por exemplo:
  - **MINYEAR** <= year <= **MAXYEAR**
  - 1 <= month <= 12
  - 1 <= day <= número de dias no mês e ano fornecidos
```py
import datetime

d = datetime.date(2023, 7, 19)
print(d) # 2023-07-19

# Utilizando from datetime import
from datetime import date
data = date(2023, 7, 19)
print(data)# 2023-07-19
```

Outro método interessante é o método interessante do objeto `date` é o `date.today()`, que retorna a data atual local:
- Repare que o formato retornado da data é ano-mes-dia, mas podemos modificar isso com formatação
```py
print(date.today()) # 2025-08-01
```

#### Objeto datetime
**Documentação**: Um objeto datetime é um único objeto contendo todas as informações de um objeto date e um objeto time.
Assim como um objeto date, datetime presume o atual calendário Gregoriano estendido em ambas as direções; assim como um objeto time, datetime presume que existem exatamente 3600*24 segundos em cada dia.

Diferente do `date`, o `datetime` espera como argumento informações como: hora, minuto e segundo. 
- Ele é muito utilizado no mundo corporativo por possuir informações de horas, minutos e segundos. Por exemplo, ao salvar um pedido de um e-commerce, o ideal é utilizar a data/hora em que ele foi realizado e não somente a data

Assim como o `date`, ele possui diversas validações no construtor:
- Os argumentos year, month e day são obrigatórios. `tzinfo` pode ser None, ou uma instância de subclasse de tzinfo. Os argumentos remanescentes devem ser inteiros nos seguintes intervalos:
    - MINYEAR <= year <= MAXYEAR,
    - 1 <= month <= 12,
    - 1 <= day <= número de dias no mês e ano fornecidos,
    - 0 <= hour < 24,
    - 0 <= minute < 60,
    - 0 <= second < 60,
    - 0 <= microsecond < 1000000,
    - fold in [0, 1].
```py
data_hora = datetime(2023, 7, 19, 10, 30, 0)
print(data_hora) # 2023-07-19 10:30:00

# Se eu nao passar hora-minuto-segundo, ele retorna essas informações zeradas
data_hora = datetime(2023, 7, 19)
print(data_hora) # 2023-07-19 00:00:00
``` 

> O `datetime` também tém o método `.today()`
```py
print(datetime.todau()) # 2025-08-01 16:03:20
```

#### Objeto time

**Documentação**: Um objeto time representa a hora (local) do dia, independente de qualquer dia em particular, e sujeito a ajustes através de um objeto `tzinfo`.

O `time` é utilizado para informações de tempo (hora, minuto, segundo). Mas não suporta datas (dia, mes, ano) 

O `time` também possui validações. Elas são parecidas com a do `datetime`, com a diferença que ele não possui validação para datas, somente para as horas-minutos-segundos.

```py
hora = time(10, 20, 0)
print(hora) # 10:20:00
```

----------------------------------------------------------------------------

## Manipulando datas com `timedelta`

Podemos criar e manipular objetos `date`, `time` e `datetime` de várias maneiras. Por exemplo, podemos adicionar e subtrair datas, verificar a diferença entre datas e muito mais.

Utilizamos o objeto `timedelta` para realizar essas manipulações. O `timedelta` representa uma duração, a diferença entre duas instâncias datetime ou date.
```py
class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
```

É possível realizar diversas operações com as datas:
- Soma
- Diferença
- Multiplicação
- Divisão
- Entre outras.

>As operações mais realizadas são a de `soma` e `diferença`, onde adicionamos ou subtraímos um `timedelta`  à uma data `datetime` ou `date` (o `time` não suporta esse tipo de manipulação). Com isso, podemos criar um `timedelta` com as informações que queremos adicionar/remover/multiplicar à outra data (como dias, semanas, meses. horas, minutos, segundos, milissegundos, etc)

#### **Exemplo - soma**
No exemplo abaixo estamos manipulando um objeto `datetime` com o `timedelta`
- `datetime()`: Criamos uma data/hora com `datetime`.
- `timedelta(weeks=1)`: Vimos que o construtor de `timedelta` suporta diversas unidades de tempo (dia, mes, ano, semanas, horas, etc), então podemos utilizar qualquer uma delas para adicionar/subtrair (ou realizar qualquer operação) à data. Nesse caso, adicionamos uma semana à data original.
```py
import datetime

# Criando data e hora
d = datetime.datetime(2023, 7, 19, 13, 45)
print(d) # 2023-07-19 13:45:00

# Adicionando uma semana
d = d + datetime.timedelta(weeks=1)
print(d) # 2023-07-26 13:45:00
```

>O `timedelta` é capaz de "virar" a data de um dia para o outro se você adicionar horas/minutos para isso. 

#### **Exemplo - subtração**
Nesse caso, vamos remover 3 dias de um `datetime`
```py
import datetime

# Criando data e hora
d = datetime.datetime(2023, 7, 19, 13, 45)
print(d) # 2023-07-19 13:45:00

# Adicionando uma semana
d = d - datetime.timedelta(days=3)
print(d) # 2023-07-16 13:45:00
```

### Exemplo - lava rápido
```py
```

--------------------------------------------------------------------

## Formatando e convertendo datas com strftime e strptime

Python também permite converter e formatar datas e horas.
Para isso, usamos os métodos `strftime` (string format time) e `strptime` (string parse time).
- `strftime` (formatar como string)
- `strptime` (converter de string).

Formatar uma data significa exibi-la em um padrão diferente, utilizando uma máscara. Por padrão, o formato das datas no Python é o americano (yyyy-MM-dd HH:mm:ss), sendo que:
- `yyyy`: Representa o ano com 4 dígitos - ex: 2025
- `MM`: Representa o mês com 2 dígitos - ex: 08
- `dd`: Representa o dia com 2 dígitos - ex: 01
- `HH`: Representa a hora com 2 dígitos - ex: 16
- `mm`: Representa os minutos com 2 dígitos - ex: 36
- `ss`: Representa os segundos com 2 dígitos - ex: 36

Aqui no brasil, utilizamos o padrão `dd/MM/yyyy HH:mm:ss`, algo assim: `01/12/2025 20:30:00`

#### Exemplo - formatando com strftime
O `strftime` ("**str**ing **f**ormat **time**") permite transformar um objeto `date` ou `datetime` em uma string com o formato desejado, usando códigos de formatação.

- O `strftime` permite "cortar" o seu objeto `date/datetime`. Por exemplo, se você omitir minutos ou segundos na máscara, eles não aparecerão na string formatada.
```py
import datetime

d = datetime.now()

print(d.strftime("%d/%m/%Y %H")) # 01/08/2025 16 -> retorno sem minutos e segundos
```

Já a conversão consiste em transformar uma data em um formato diferente (string, por exemplo) para um objeto de data (`date` ou `datetime`)
#### Exemplo - convertendo strptime
O `strptime` é utilizado para converter strings em objetos `date` ou `datetime`. Ele transforma uma string de data/hora em um objeto `datetime`, desde que você informe o formato da string.
- O 1° argumento é a string que será convertida `date_string`, o 2° é mascara/formato que a string utiliza (nesse caso, utiliza dd/MM/yyyy HH:mm) `%d/%m/%Y %H:%M`
```py
date_string = "20/07/2023 15:30"
data_convertida = datetime.strptime(date_string, "%d/%m/%Y %H:%M")
print(data_convertida) # 2023-07-20 15:30:00
```

#### Tabela de códigos de formatação

| Código | Significado                                 | Exemplo                    |
| ------ | ------------------------------------------- | -------------------------- |
| `%d`   | Dia do mês (2 dígitos)                      | `03`                       |
| `%m`   | Mês (2 dígitos)                             | `08`                       |
| `%Y`   | Ano com 4 dígitos                           | `2025`                     |
| `%y`   | Ano com 2 dígitos                           | `25`                       |
| `%H`   | Hora (formato 24h, 2 dígitos)               | `16`                       |
| `%I`   | Hora (formato 12h, 2 dígitos)               | `04`                       |
| `%p`   | AM/PM                                       | `PM`                       |
| `%M`   | Minutos (2 dígitos)                         | `36`                       |
| `%S`   | Segundos (2 dígitos)                        | `05`                       |
| `%f`   | Microssegundos (6 dígitos)                  | `524236`                   |
| `%A`   | Nome completo do dia da semana              | `Sunday`                   |
| `%a`   | Nome abreviado do dia da semana             | `Sun`                      |
| `%B`   | Nome completo do mês                        | `August`                   |
| `%b`   | Nome abreviado do mês                       | `Aug`                      |
| `%w`   | Dia da semana (0=domingo, 6=sábado)         | `0`                        |
| `%j`   | Dia do ano (001–366)                        | `216`                      |
| `%W`   | Semana do ano (segunda começa semana)       | `31`                       |
| `%c`   | Representação completa local da data e hora | `Sun Aug  3 16:45:30 2025` |
| `%x`   | Representação local da data                 | `08/03/25` (pt-BR)         |
| `%X`   | Representação local da hora                 | `16:45:30`                 |


--------------------------------------------------------------------------------

## Trabalhando com timezone

Quando trabalhamos com data e hora, lidar com fusos horários é uma necessidade comum. Python facilita isso através do módulo `pytz`.

Assim como o `datetime`, o `pytz` é um módulo que precisa ser importado com `import pytz`. Além disso, precisamos instalá-lo com o comando `pip install pytz` no terminal

Para utilizar o `pytz`, devemos utilizar o método `timezone(fuso_horario)`, passando como parâmetro o fuso horário que deseja utilizar.
- O parâmetro que utilizamos é justamente o nome do fuso horário, ou seja, uma string. EX: `America/Sao_Paulo`
```py
# pip install pytz
import datetime
import pytz 

d = datetime.now(pytz.timezone("America/Sao_Paulo"))
print(d) # 2025-08-31 16:56:00-03:00
```

>Você pode se perguntar, como eu vou saber o nome dos fusos-horários?
- Os nomes dos `timezones` seguem um padrão definido no banco de dados tz. Você pode clicar [aqui](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) para acessar a lista completa dos fusos horários, bem como quanto tempo eles correspondem.
- Nessa lista, vemos quanto tempo um fuso horário equivale. No caso de São Paulo, o valor é -3. Isso significa que o horário em SP será 3 horas a menos do horário de Londres (que é o marco zero)

> Sempre salve as datas no formato UTC em seu banco de dados. Será mais fácil realizar a manipulação futuramente

### Timezone com datetime
O Python permite fazer isso com o módulo `datetime` padrão, embora seja um pouco mais complexo do que usando bibliotecas como '`pytz`'.

Utilizando o módulo `datetime`, poderíamos utilizar timezones seguindo o exemplo abaixo:
```py
from datetime import datetime, timezone, timedelta

# Com datetime
data_time_2 = datetime.now()
date_sao_paulo_2 = data_time_2(timezone(timedelta(hours=-3)))
print(date_sao_paulo_2)
date_time_oslo_2 = data_time_2(timezone(timedelta(hours=2)))
```

<br>

## Data-hora - Desafio

Com os novos conhecimentos adquiridos sobre data e hora, você foi encarregado de implementar as seguintes funcionalidades no sistema:
- Estabelecer um limite de 10 transações diárias para uma conta
- Se o usuário tentar fazer uma transação após atingir o limite, deve ser informado que ele excedeu o número de transações permitidas para aquele dia.
- Mostre no extrato, a data e hora de todas as transações.