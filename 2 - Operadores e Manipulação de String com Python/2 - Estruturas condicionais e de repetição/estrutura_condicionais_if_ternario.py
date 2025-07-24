saldo = 2000
saque = 2500

# Sucesso = 1 parte: retorno caso a expressão retorne verdadeiro
# if saldo >= saque = 2 parte: expressão lógica
# else "Falha" = 3 parte: retorno caso a expressão não seja atendida
status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar saque!")