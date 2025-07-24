# Entrada do usuário
email = input()
comeco = email[0]
final = email[-1]

# TODO: Verifique as regras do e-mail:
if(comeco == "@" or final == "@"):
    print("E-mail inválido")
elif ("@" in email and ("gmail.com" or "outlook.com" in email)) and (" " not in email):
    print("E-mail válido")
else:
    print("E-mail inválido")