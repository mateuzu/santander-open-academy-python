lista = []

#------------------------------------------------------------------------------------------------------------
# #APPEND - ADICIONA UM OBJETO A LISTA - PODE ADICIONAR QUALQUER TIPO DE OBJETO, INCLUSIVE OUTRAS LISTAS
print("APPEND - ADICIONANDO VALORES A LISTA")
lista.append("Mateus")
lista.append("Ferreira")
lista.append(22)
lista.append([30, 20, 10]) # inserindo outras listas

print(lista)

#------------------------------------------------------------------------------------------------------------
#CLEAR - LIMPA A LISTA
print("\nCLEAR - LIMPANDO A LISTA")
lista.clear()
print(lista)

#------------------------------------------------------------------------------------------------------------
#COPY - CRIA UMA CÓPIA IDÊNTICA A LISTA ORIGINAL
print("\nCOPY - COPIANDO UMA LISTA")
lista = [1, "Python", [40, 30, 20]]
lista_copia = lista.copy()

# Mesmo copiando exatamente, eles ocupam espaços diferentes na memória. o id(list) retorna o identificador do objeto
print("ORIGINAL", lista, "ID:" , id(lista)) 
print("COPIA", lista_copia, "ID:" , id(lista_copia))

#------------------------------------------------------------------------------------------------------------
#COUNT - RETORNA A QUANTIDADE DE VEZES QUE UM DETERMINADO VALOR APARECE
print("\nCOUNT - CONTAGEM DE APARIÇÃO DE UM ELEMENTO")
cores = ["vermelho", "azul", "verde", "azul", "roxo", "roxo", "azul", "amarelo"]
print(cores.count("vermelho"))
print(cores.count("azul"))
print(cores.count("roxo"))


#------------------------------------------------------------------------------------------------------------
#EXTEND - INCORPORA UMA SEQUENCIA DE VALORES A UMA LISTA - ESSE MÉTODO PERMITE ADICIONAR VALORES DUPLICADOS A LISTA
print("\nEXTEND - ADICIONA UMA SEQUENCIA DE VALORES A UMA LISTA")
linguagens = ["python", "js", "c"]
linguagens.extend(["java", "csharp"])
print(linguagens)
# OBS: Com o append também é possível adicionar uma sequencia de valores, porém ele adiciona uma lista à lista. O extend adiciona somente os valores da sequencia
# linguagens.append(["java", "csharp"]) - Se eu fizer isso, o resultado será uma lista dentro de outra -> ["python", "js", "c", [["java", "csharp"]]]



#------------------------------------------------------------------------------------------------------------
#INDEX - RETORNA A POSIÇÃO DA PRIMEIRA APARIÇÃO DO VALOR REPASSADO COMO PARÂMETRO
# SE EXISTIR VALORES DUPLICADOS, ELE RETORNA A POSIÇÃO SOMENTE DA PRIMEIRA OCORRECIA
print("\nINDEX - RETORNA A POSIÇÃO DA PRIMEIRA OCORRENCIA DE UM VALOR")
print(linguagens.index("java"))


#------------------------------------------------------------------------------------------------------------
#POP() - SEM NENHUM PARAMENTRO, RETIRA O ULTIMO ELEMENTO DA LISTA.
#POP(i) - COM UM INDICE, REMOVE O ELEMENTO QUE ESTÁ NO INDICE ESPECIFICADO
print("\nPOP - REMOVE O ULTIMO ELEMENTO DA LISTA OU O ELEMENTO DO INDICE ESPECIFICADO")
linguagens.pop() # remove o ultimo elemento da lista
linguagens.pop(0) # remove o primeiro elemento da lista
print(linguagens) 


#------------------------------------------------------------------------------------------------------------
#REMOVE() - REMOVE UM ELEMENTO COM BASE NO VALOR
print("\nREMOVE - REMOVE UM ELEMENTO COM BASE NO VALOR")
linguagens.append("Go")
linguagens.remove("Go")
print(linguagens)


#------------------------------------------------------------------------------------------------------------
#INVERSE() - INVERTE OS ELEMENTOS DA LISTA
print("\nREVERSE - INVERTE OS ELEMENTOS DA LISTA")
numeros = [8, 1, 2, 5, 14, 7, 20, 3]
print("ORIGINAL", numeros)
numeros.reverse()
print("REVERSE", numeros)


#------------------------------------------------------------------------------------------------------------
#SORT() - ORDENA A LISTA ALFABETICAMENTE EM ORDEM CRESCENTE
#SDRT(REVERSE=TRUE) - ORDENA A LISTA ALFABETICAMENTE EM ORDEM DECRESCENTE
#OBS: É possível usar o parametro key (numeros.sort(key=lambda) para ordenar a lista com base em uma função anonima, mas vamos explicar isso posteriormente
print("\nSORT - ORDENANDO ELEMENTOS DA LISTA")
numeros.sort()
print("CRESCENTE", numeros)
numeros.sort(reverse=True)
print("DECRESCENTE", numeros)

linguagens.sort(key=lambda x: len(x)) # Lambda para ordenar os elementos com base na quantidade de caracterers de forma CRESCENTE, para DECRESCENTE basta reverse=True
print("LAMBDA", linguagens)



#------------------------------------------------------------------------------------------------------------
#SORTED() - PARECIDO COM O SORT, PORÉM ESSA É UMA FUNÇÃO BUILT-IN DO PYTHON E PODE SER USADA COM DIVERSOS OBJETOS, INCLUINDO LISTAS
print("\nSORTED - ORDENANDO ELEMENTOS DA LISTA")
numeros_desordenados = [1, 4, 2, 6, 20, 11, 3, 5]
sorted(numeros_desordenados)
print(numeros_desordenados)



#------------------------------------------------------------------------------------------------------------
#LEN() - RETORNA O TAMANHO DA LISTA OU DOS ELEMENTOS
print("\nLEN - RETORNA O TAMANHO DA LISTA/ELEMENTOS")
print("TAMANHO DA LISTA:" , len(linguagens))
print("TAMANHO DE UM ELEMENTO", len("TESTE"))


