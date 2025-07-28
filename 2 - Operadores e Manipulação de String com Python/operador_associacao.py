# O operador in verifica se um determinado valor está presente em uma sequencia (de string, numeros, objetos, etc)
# O not in verifica se um valor NÃO está presente em uma sequencia

curso = "Curso de Python" # Sequencia de caracteres
frutas = ["Laranja", "Uva", "Limão"] # Sequencia de string
saques = [1500, 100] # Sequencia de numeros

# Verifica se o valor Python está presente na stirng curso
print("Python" in curso)

# Verifica se a palavra maça esta presente na lista de frutas
print("Maçã" in frutas)

# Verifica se a palavra maça NÃO esta presente na lista de frutas
print("Maçã" not in frutas) # Como a palavra NÃO ESTÁ, o resultado é verdadeiro

# Verifica se 200  esta presente na lista de frutas
print(200 in saques)