# Introspecção é a capacidade de um objeto saber sobre seus próprios atributos em tempo de execução
# Como o python saber o nome da função executada 

import functools

def meu_decorador(funcao):
    @functools.wraps(funcao) # arante que a função envelope finja ser a função original (ola_mundo)
    def envelope(*args, **kwwargs):
        print("Faz algo antes de executar a função")
        funcao(*args, **kwwargs)
        print("Faz algo depois de executar a função")
        return funcao(*args, **kwwargs)

    return envelope

@meu_decorador
def ola_mundo(nome):
    print(f"Olá, {nome}")
    return nome.upper()

resultado = ola_mundo("João")
print("Resultado:", resultado)

print(print.__name__)
print(ola_mundo.__name__)