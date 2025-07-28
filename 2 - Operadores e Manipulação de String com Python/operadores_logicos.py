saldo = 1000
saque = 200
limite = 100
conta_especial = True

print("Operador and verdadeiro: ", True and True)
print("Operador and falso: ", True and True and True and True and False) # Não importa quantas expressões booleanas existem, todas precisam ser V para que o operador seja V 
print("Operador or verdadeiro: ", True or False or False or False) # Não importa quantas expressões booleanas existem, apenas 1 precisa ser verdadeira
print("Operador or falso: ", False or False)
print("Operador not verdadeiro: ", not False)
print("Operador not falso: ", not True)

# Troque isso
expressao = saldo >= saque and saque <= limite or conta_especial and saldo >= saque

# Por isso - melhor organização
expressao_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)