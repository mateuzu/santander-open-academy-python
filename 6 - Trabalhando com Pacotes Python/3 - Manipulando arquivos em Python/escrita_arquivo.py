arquivo = open("./novo_arquivo.txt", 'w')

arquivo.write("Olá, mundo!") # Escrevendo uma linha

arquivo.writelines(["Assim", "fica", "sem", "espaço", "entre", "as", "palavras"])

arquivo.writelines(["Agora ", "tem ", "um ", "espaço ", "entre ", "as ", "palavras"])

arquivo.writelines(["\n", "isso ", "vai ", "estar ", "em " , "outra ", "linha"])

arquivo.close()