# CRIANDO LISTA
print("CRIANDO LISTA")
frutas = ["Laranja", "Maçã", "Uva", "Abacaxi", "Morango", "Manga"]
lista_vazia = []
letras = list("python") # Nesse caso, ele irá armazenar cada letra da palavra python dentro da lista ['p', 'y', 't', 'h', 'o', 'n']
numeros = list(range(10)) # Nesse caso, irá adicionar os números de 0 à 9
lista_diversos = ["Ferrari", "F8", 420000, 2020, 2900, "São Paulo", True]
carros = ["Gol", "Celta", "Palio", "Golf", "Corolla", "Vectra", "Jeep"]

print(letras)
print(numeros)

#-------------------------------------------------------------------------------------------#
# ACESSO DIRETO AOS ELEMENTOS DA LISTAS
# O acesso direto consiste em utilizar o indice/posição do elemento que desejado
print("\nACESSANDO ELEMENTO DA LISTA")
print(frutas[0])
print(frutas[1])
print(frutas[-1]) # Tambem funciona com indices negativos, sendo que -1 captura o ultimo elemento da lista

#-------------------------------------------------------------------------------------------#
# CRIANDO MATRIZ
print("\nMATRIZ OU LISTA ANINHADA")
matriz = [
    [1, "a", 2], # Linha 0
    ["b", 3, 4], # Linha 1
    [6, 5, "c"]  # Linha 2
#    0  1   2    Colunas    
]

print(matriz[0]) # Retorna a primeira LINHA inteira da matriz = [1, "a", 2]
print(matriz[0][0]) # Retorna o elemento que está na primeira LINHA e primeira COLUNA = 1
print(matriz[0][-1]) # Retorna o elemento que está na primeira LINHA e ultima COLUNA = 2
print(matriz[-1][-1]) # Retorna o elemento que está na ultima LINHA e ultima COLUNA = c

#-------------------------------------------------------------------------------------------#
# FATIAMENTO DE LISTAS
print("\nFATIAMENTO")
print(letras[2:]) # ["t", "h", "o", "n"]
print(letras[:2]) # ["p", "y"]
print(letras[1:3]) # ["y", "t"]
print(letras[0:3:2]) # ["p", "t"]
print(letras[::]) # ["p", "y", "t", "h", "o", "n"]
print(letras[::-1]) # ["n", "o", "h", "t", "y", "p"]

#-------------------------------------------------------------------------------------------#
# ITERAR SOBRE LISTAS
print("\nITERAR SOBRE LISTA")
# Para cada carro presente em CARROS
for carro in carros:
    print(carro, end=" ") # Exibe ele no console

for x in numeros:
    print(x, end=" ")

#-------------------------------------------------------------------------------------------#
# ENUMERATE AJUDA A DESCOBRIR O INDICE DE UM ELEMENTO ITERADO
print("\n\nENUMERATE")
for i, carro in enumerate(carros):
    print(f"Posilçao: {i} - Elemento: {carro}")


#-------------------------------------------------------------------------------------------#
# COMPRESSÃO DE LISTA: CRIA UMA NOVA LISTA COM BASE NOS VALORES DE UMA LISTA (FILTRO) OU GERA UMA NOVA LISTA APLICANDO MODIFICAÇÃO NOS ELEMENTOS

print("\nCOMPRESSÃO DE LISTAS")
print("COMPRESSÃO EXEMPLO 1 - CRIAR UMA LISTA DE 1° PARES COM BASE EM UMA LISTA DE NÚMEROS VARIADOS")
# EXEMPLO 1 (SEM COMPRESSAO): CRIAR UMA LISTA DE N° PARES COM BASE EM UMA LISTA DE NÚMEROS VARIADOS
lista_numeros = [1, 30, 21, 2, 9, 65, 34]
pares_sem_compressao = []

for numero in lista_numeros:
    if numero % 2 == 0:
        pares_sem_compressao.append(numero)

print("SEM COMPRESSÃO", pares_sem_compressao)

# EXEMPLO 2 (COM COMPRESSAO): CRIAR UMA LISTA DE N° PARES COM BASE EM UMA LISTA DE NÚMEROS VARIADOS
# OBS: A COMPRESSÃO PODE SER FEITA EM UMA LINHA, EU "QUEBREI" PARA EXPLICAR CADA ETAPA
pares_com_compressao = [numero # [numero] -> Retorno da operação que será adicionado a lista pares_com_compressao
                        for numero in lista_numeros # for numero in lista_numeros -> Laço para percorrer todos os elementos de lista_numeros
                        if numero % 2 == 0] # if numero % 2 == 0 -> Condição booleana para filtrar os valores
print("COM COMPRESSÃO",pares_com_compressao)


print("\nCOMPRESSÃO EXEMPLO 2 - CRIAR UMA LISTA MODIFICADA ONDE CADA ELEMENTO É ELEVADO AO QUADRADO")
# EXEMPLO 2 (SEM COMPRESSAO): CRIAR UMA LISTA MODIFICADA ONDE CADA ELEMENTO É ELEVADO AO QUADRADO
quadrado_sem_compressao = []

for numero in lista_numeros:
    quadrado_sem_compressao.append(numero ** 2)

print("SEM COMPRESSÃO", quadrado_sem_compressao)


# EXEMPLO 1 (COM COMPRESSAO): CRIAR UMA LISTA MODIFICADA ONDE CADA ELEMENTO É ELEVADO AO QUADRADO
quadrado_com_compressao = [numero ** 2 # numero ** 2 -> retorno da operação será o elemento elevado ao quadrado  
                            for numero in lista_numeros] # for numero in lista_numeros -> laço para percorrer todos os elementos da lista_numeros e aplicar a operação
print("COM COMPRESSÃO", quadrado_com_compressao)