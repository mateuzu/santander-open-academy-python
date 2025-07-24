produto_1 = 20
produto_2 = 10

print("Soma: ", produto_1 + produto_2)
print("Subtração: ", produto_1 - produto_2)
print("Divisão: ", produto_1 / produto_2)
print("Divisão inteira: ", produto_1 // produto_2)
print("Multiplicação: ", produto_1 * produto_2)
print("Potenciação: ", produto_1 ** produto_2)
print("Módulo: ", produto_1 % produto_2)

# Precedencia
print("Resolve 1° a multiplicação: ", 10 - 5 * 2)
print("Resolve 1° a operação no (): ", (10 - 5) * 2)
print("Resolve 1° a potência: ", 10 ** 2 * 2)
print("Resolve 1° a operação no (): ", 10 ** (2*2))
print("Resolve na ordem da esquerda para direita: ", 10 / 2 * 4)