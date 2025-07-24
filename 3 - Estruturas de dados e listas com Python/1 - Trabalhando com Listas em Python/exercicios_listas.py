# 1. Removendo duplicatas de uma lista
lista = [1, 2, 2, 3, 4, 4, 5, 6, 7, 8, 8, 9, 9, 9, 10]
lista_sem_duplicatas = []

for numero in lista:
    if numero not in lista_sem_duplicatas:
        lista_sem_duplicatas.append(numero)

print("Lista sem duplicatas:",lista_sem_duplicatas)

# 2. Inversão manual da lista
lista_invertida = []
indice = len(lista_sem_duplicatas) - 1

for numero in lista_sem_duplicatas:
    lista_invertida.append(lista_sem_duplicatas[indice])
    indice -= 1

print("Lista invertida:",lista_invertida)


# 3. Soma de elementos pares
soma = 0
for numero in lista_sem_duplicatas:
    if numero % 2 == 0:
        soma += numero

print("Soma:", soma)

# 4. Filtar nomes com mais de 5 letras
nomes = ["Mateus", "Caio", "Maria", "Joana", "Helena", "Henrique", "José", "Beatriz"]
nomes_com_mais_de_5_letras = [nome for nome in nomes if len(nome) > 5]
print("Nomes com mais de 5 letras:", nomes_com_mais_de_5_letras)


# 5. Intercalar duas listas
a = [1, 2, 3]
b = ['a', 'b', 'c']
c = []

for letra in b:
    for numero in a:
        if letra not in c and numero not in c:
            c.append(letra)
            c.append(numero)

print(c)
