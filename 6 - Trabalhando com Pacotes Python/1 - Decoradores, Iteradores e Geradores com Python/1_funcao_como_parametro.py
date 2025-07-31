def mensagem(nome):
    print("executando funcao menasgem()")
    return f'Oi {nome}'

def mensagem_longa(nome):
    print('exectuando funcao mensagem_longa()')
    return f"Olá, tudo bem com você {nome} ?"

def executar(funcao, nome):
    print('executando funcao executar')
    return funcao(nome)

print(executar(mensagem, "João")) # Uitlizando uma função como parâmetro
print(executar(mensagem_longa, "João"))