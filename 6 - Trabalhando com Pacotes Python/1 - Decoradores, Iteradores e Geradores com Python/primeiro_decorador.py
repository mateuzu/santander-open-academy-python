def meu_decorador(funcao):
    def envelope():
        print("Faz algo antes de executar a função")
        funcao()
        print("Faz algo depois de executar a função")

    return envelope

def ola_mundo():
    print("Olá, mundo")

ola_mundo = meu_decorador(ola_mundo)
ola_mundo()

print()
#------------------------------AÇÚCAR SINTÁTICO------------------------------#
# permite trocar a atruição direta pelo sinal de @

# TROCA ISSO: 
# ola_mundo = meu_decorador(ola_mundo)

# POR ISSO: @meu_decorador
#           def ola_mundo() 

@meu_decorador # Usando o decorador para a função
def ola_mundo_2():
    print("Olá mundo 2")

ola_mundo_2()