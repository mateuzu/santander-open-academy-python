def meu_decorador(funcao):
    def envelope(*args, **kwwargs): # É possível usar somente o argumento que a função orignal espera (nome), mas com args e kwargs fica mais dinamico
        print("Faz algo antes de executar a função")
        funcao(*args, **kwwargs)
        print("Faz algo depois de executar a função")

    return envelope

@meu_decorador
def ola_mundo(nome):
    print(f"Olá, {nome}")

ola_mundo("João")


#--------------------------------------EXEMPLO - DECORADOR COM ARGS E KWARGS--------------------------------------#
def duplicar(funcao):
    def envelope(*args, **kwargs):
        funcao(*args, **kwargs)
        funcao(*args, **kwargs)
    
    return envelope

@duplicar
def aprender(tecnologia):
    print(f"estou aprendendo {tecnologia}")

aprender("Python")