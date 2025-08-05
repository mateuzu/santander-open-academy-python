# Dicionário com usuários cadastrados e suas senhas
usuarios = {
    "joao": "1234",
    "ana": "abcd",
    "maria": "senha123",
    "marcelo": "iou789",

}

# Entrada do usuário
usuario = input().strip()
senha = input().strip()

# TODO: Verifique se o usuário existe e a senha está correta:
if usuario in usuarios.keys():
    password = usuarios.get(usuario)
    if senha != password:
        print("Usuário ou senha incorretos")
    else:
        print("Acesso permitido")