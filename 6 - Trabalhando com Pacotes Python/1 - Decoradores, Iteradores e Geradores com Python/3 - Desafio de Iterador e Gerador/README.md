# Iteradores e Geradores - Desafio

## Introdução
Com os novos conhecimentos adquiridos sobre decoradores, geradores e iteradores, você foi encarregado de implementar as seguintes funcionalidades no sistema bancário:
- Decorador de log
- Gerador de relatórios
- Iterador personalizado

### Decorador de log
Implemente um decorador que seja aplicado a todas as funções de transações (depósito, saque, criação de conta, etc). Esse decorador deve registrar (printar) a data e hora de cada transação, bem como o tipo de transação.

### Gerador de Relatório
Crie um gerador que permita iterar sobre as transações de uma conta e retorne, uma a uma, as transações que foram realizadas. Esse gerador deve também ter uma forma de filtrar as transações baseado em seu tipo (por exemplo, apenas saques ou apenas depósitos).

### Iterador personalizado
Implemente um iterador personalizado `Contalterador` que permita iterar sobre todas as contas do banco, retornando informações básicas de cada conta (número, saldo atual, etc).