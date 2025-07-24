nome = "mAteuS"

# Maiuscula, minuscula e titulo

print("ORIGINAL", nome)
print("MAISCULO", nome.upper())
print("MINUSCULO", nome.lower())
print("TITULO", nome.title())

print()
# Removendo espaços em branco
texto = "        Olá mundo!  "
print("ORIGINAL", texto + ".")
print("SEM ESPAÇOS EM BRANCO", texto.strip() + ".")
print("REMOVE ESPAÇO DA ESQUERDA", texto.lstrip() + ".")
print("REMOVE ESPAÇO DA DIREITA", texto.rstrip() + ".")


print()
# Centralização e junção
menu = "Titulo"
print("****" + menu + "****")
print(menu.center(14, "*")) # Centraliza de uma maneira mais elegante
print("Juntando", ".".join(menu))