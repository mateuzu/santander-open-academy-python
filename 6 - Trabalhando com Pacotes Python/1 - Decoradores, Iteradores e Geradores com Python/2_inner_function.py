def principal():
    print("executando a funcao principal")

    def funcao_interna():
        print("executando a funcao_interna")

    def funcao_interna_2():
        print("executando a funcao_interna_2")

    funcao_interna()
    funcao_interna_2()

principal()