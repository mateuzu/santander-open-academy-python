texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

print("\nFOR")
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")


print("\nFOR-ELSE")
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else:
    print("Executaod no fim do laço")


print("\nFOR-RANGE")
for numero in range(0, 51, 5):
    print(numero, end=" ")


print("\nFOR COM CONTINUE")
for numero in range(0, 51, 5):
    if numero == 10:
        continue
    print(numero, end=" ")