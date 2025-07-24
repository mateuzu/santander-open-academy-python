# Desafio de código - Sistema de atendiment médico

## Descrição

Uma clínica médica quer automatizar seu sistema de atendimento. Crie uma função que organize os pacientes em ordem de prioridade com base na idade e na urgência do caso.

### Critérios de prioridade:
- Pacientes acima de 60 anos têm prioridade.
- Pacientes que apresentam a palavra "urgente" na ficha têm prioridade máxima.
- Os demais pacientes são atendidos por ordem de chegada.

## Entrada
- Um número inteiro n, representando a quantidade de pacientes.
- n linhas seguintes, cada uma contendo os dados de um paciente no formato: nome, idade, status
- nome: string representando o nome do paciente.
- idade: número inteiro representando a idade do paciente.
- status: string que pode ser "urgente" ou "normal".

## Saida
- A saída deve exibir a lista dos pacientes ordenada de acordo com as regras de prioridade, no formato: Ordem de Atendimento: nome1, nome2, nome3, ...

## Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

|Entrada | Saída| 
|-------|-------|
3 / Carlos, 40, normal / Ana, 70, normal / Bruno, 30, urgente | Ordem de Atendimento: Bruno, Ana, Carlos
| 4 / Paula, 30, normal / Ricardo, 60, normal / Tiago, 60, urgente / Amanda, 50, urgente | Ordem de Atendimento: Tiago, Amanda, Ricardo, Paula
|5 / João, 65, normal / Maria, 80, urgente / Lucas, 50, normal / Fernanda, 25, normal / Pedro, 90, urgente | Ordem de Atendimento: Pedro, Maria, João, Lucas, Fernanda

<br>

------------------------------------------------------------------------

<br>

# Desafio de código - Sistema de reservas de hotel

## Descrição
Uma pousada deseja automatizar seu sistema de reservas. Crie uma função que receba uma lista de quartos disponíveis e uma lista de reservas solicitadas. A função deve verificar quais reservas podem ser aceitas e quais devem ser recusadas por falta de disponibilidade.

## Entrada
- Uma lista contendo os números dos quartos disponíveis.
- Uma lista contendo os números dos quartos solicitados pelos clientes.

## Saida
- Uma mensagem informando quais reservas foram confirmadas e quais foram recusadas.

## Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

| Entrada | Saida |
|---------|-------|
|101 102 103 104 102 105 101 103 | Reservas confirmadas: 102 101 103 / Reservas recusadas: 105|
|201 202 203 204 205 205 202 208 201 203 | Reservas confirmadas: 205 202 201 203 / Reservas recusadas: 208
| 10 20 30 40 50 25 30 10 40 50 60 | Reservas confirmadas: 30 10 40 50 / Reservas recusadas: 25 60|