nome = "Mateus"
idade = 22
profissao = "Progamador"
linguagem = "Python"

dados = {"nome": "Mateus", "idade": 28}
saldo = 45.2434

print("OLD STYLE")
print("Nome: %s Idade: %d" % (nome, idade))

print("\nFORMAT PADRÃO")
print("Nome: {} Idade: {}".format(nome, idade))

print("\nFORMAT COM INDICE")
# Repare como inverti as variaveis pois estou repassando os indices que cada uma vai ocpuar
# Alem disso, é possível repetir as variaveis sem a necessidade de referenciar novamente no .format()
print("Nome: {1} Idade: {0}, {1} {1}".format(idade, nome))

print("\nFORMAT COM NOME")
# Aqui também é possível repetir as variaveis
print("Nome: {nome} Idade: {idade}, {nome}, {nome}".format(nome = nome, idade = idade))

print("\nFORMAT COM DICIONARIO")
print("Nome: {nome} Idade: {idade}".format(**dados))

print("\nF-STRING")
print(f"Nome: {nome} Idade: {idade}")

print("\FORMATANDO CASAS DECIMAIS COM F-STRING")
print(f"Saldo: {saldo:.2f}")