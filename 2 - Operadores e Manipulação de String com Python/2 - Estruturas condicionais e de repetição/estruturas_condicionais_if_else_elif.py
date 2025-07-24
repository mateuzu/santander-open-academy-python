MAIOR_IDADE = 18
IDADE_ESPECIAL = 16

idade = int(input("Informe sua idade: "))


print("\nIF")
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH\n")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH\n")


print("IF-ELSE")
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH\n")
else:
    print("Ainda não pode tirar a CNH\n")


print("IF-ELIF-ELSE")
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH\n")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aula teórica, mas não pode fazer aulas práticas")
else:
    print("Ainda não pode tirar a CNH\n")