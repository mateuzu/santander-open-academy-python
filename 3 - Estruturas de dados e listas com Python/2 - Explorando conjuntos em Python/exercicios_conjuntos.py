# Remover duplicatas usando conjunto
lista = [1, 2, 2, 3, 4, 4, 5, 6, 7, 8, 8, 9, 9, 9, 10]
conjunto = set()

for numero in lista:
    if numero not in conjunto:
        conjunto.add(numero)

print(conjunto)

# 2. União de conjuntos
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}
uniao = set()

for x in conjunto_a:
    for y in conjunto_b:
        if (x not in uniao) or (y not in uniao):
            uniao.add(x)
            uniao.add(y)
print(uniao)

# 3. Intersecção dos conjuntos
interseccao = set()

for x in conjunto_a:
    if x in conjunto_b:
        interseccao.add(x)
print(interseccao)

# 4. Diferença entre os conjuntos
diferenca = set()

for x in conjunto_a:
    if x not in conjunto_b:
        diferenca.add(x)
print(diferenca)

# 5. Diferença simétrica entre os conjuntos
diferenca_simetrica = set()

for x in conjunto_a:
    for y in conjunto_b:
        if x not in conjunto_b and y not in conjunto_a:
            diferenca_simetrica.add(x)
            diferenca_simetrica.add(y)
print(diferenca_simetrica)

# 6. Verificar se é subconjunto
if conjunto_a in conjunto_b:
    print("A é um subconjunto de B")
else:
    print("A NÃO é um subconjunto de B")

# 7. Conjunto de caracteres únicos
frase = "Vou retornar os caracteres unicos dessa frase"
caracteres_unicos = set()

for letra in frase:
    if letra not in caracteres_unicos:
        caracteres_unicos.add(letra)

print(caracteres_unicos)

# 8. Remover elementos em comum entre dois conjuntos: remova os elementos que estão em B do conjunto A.
conjunto_a_2 = {1, 2, 3, 4}
conjunto_b_2 = {3, 4, 5, 6}
numeros_repetidos = []

for numero in conjunto_a_2:
    if numero in conjunto_b_2:
        numeros_repetidos.append(numero)

for numero in numeros_repetidos:
    conjunto_a_2.discard(numero)
    
print(conjunto_a_2)