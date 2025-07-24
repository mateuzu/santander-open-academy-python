# Desafio de projeto - Cupom desconto

## Descrição 

Uma loja online deseja aplicar descontos em seus produtos com base em cupons de desconto digitados pelos clientes.

### 📌 Regras de desconto:
- `"DESCONTO10"`: 10% de desconto.
- `"DESCONTO20"`: 20% de desconto.
- `"SEM_DESCONTO"`: Sem desconto.

## Entrada
- Preço original do produto.
- Código do cupom digitado.

## Saída
- Preço final após aplicar o desconto. Com duas casas decimais.

## Exemplos

A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

|Entrada|Saida|
|-------|-----|
|100 / DESCONTO10|90.00
|200 / DESCONTO20|160.00
|50 / SEM_DESCONTO|50.00

Atenção: É extremamente importante que as entradas e saídas sejam exatamente iguais às descritas na descrição do desafio de código.

--------------------------------------------------

<br>

# Desafio de projeto - Validador de Formato de E-mails

## Descrição
Uma empresa quer validar se os e-mails cadastrados pelos usuários estão no formato correto. Crie uma função que receba um e-mail e verifique se ele é válido, seguindo as regras:

### 📌 Regras de desconto:
1. Deve conter o caractere "@" e um domínio, como gmail.com ou outlook.com.
2. Não pode começar ou terminar com "@".
3. Não pode conter espaços.

## Entrada
- Uma string contendo o e-mail a ser validado.

## Saida
- `"E-mail válido"` se o e-mail estiver no formato correto.
- `"E-mail inválido"` caso contrário.

## Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

|Entrada|Saida|
|-------|-----|
usuario@gmail.com	E-mail válido
user@outlook.com	E-mail válido
usuario gmail.com	E-mail inválido