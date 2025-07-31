def meu_decorador(funcao):
    def envelope(*args, **kwwargs):
        print("Faz algo antes de executar a função")
        funcao(*args, **kwwargs)
        print("Faz algo depois de executar a função")
        return funcao(*args, **kwwargs) # Precisa retornar o resultado da função orignal no decorador

    return envelope

@meu_decorador
def ola_mundo(nome):
    print(f"Olá, {nome}")
    return nome.upper()

resultado = ola_mundo("João")
print("Resultado:", resultado) # Agora, conseguimos retornar o resultado

print()

#--------------------------------------OUTRO EXEMPLO - ATRUBUINDO O RESULTADO A UMA VARIAVEL--------------------------------------$

def duplicar(funcao):
    def envelope(*args, **kwargs):
        resultado = funcao(*args, **kwargs)
        return resultado # usando a variavel resultado para armazenar o retorno da função, depois retornamos ela 
    
    return envelope

@duplicar
def aprender(tecnologia):
    print(f"estou aprendendo {tecnologia}")
    return tecnologia.upper()

tecnologia = aprender("Python")
print("Resultado: ", tecnologia)

print()
#--------------------------------------OUTRO EXEMPLO - SEM RETORNO --------------------------------------$

def duplicar(funcao):
    def envelope(*args, **kwargs): # se nao incluir retorno no decorador
        funcao(*args, **kwargs)
    
    return envelope

@duplicar
def aprender(tecnologia):
    print(f"estou aprendendo {tecnologia}")
    return tecnologia.upper()

tecnologia = aprender("Python")
print("Resultado", tecnologia) # None -> o resultado será None