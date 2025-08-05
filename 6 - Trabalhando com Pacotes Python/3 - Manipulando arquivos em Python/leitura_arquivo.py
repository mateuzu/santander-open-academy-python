arquivo = open("C:\\Workspaces\\Python\\ws-bootcam-santander\\bootcamp-santander-python\\6 - Trabalhando com Pacotes Python\\3 - Manipulando arquivos em Python\\arquivo.txt", 'r')

print(arquivo.read()) # Lê o conteúdo de uma vez só
print(arquivo.readline()) # Lê linha por linha sem carregar o conteúdo na memória em uma lista
print(arquivo.readlines()) # Lê todo o conteúdo o arquivo carregado em uma lista

# READLINES() DICAS = readlines() retorna uma lista, onde cada indice é uma linha do arquivo. 
# É muito útil utilizá-lo combinado à laços de repetição, como nas estruturas abaixo:

# for line in arquivo.readlines():
#     print(line)

# while len(line := arquivo.readlines()):
#     print(line)

arquivo.close()