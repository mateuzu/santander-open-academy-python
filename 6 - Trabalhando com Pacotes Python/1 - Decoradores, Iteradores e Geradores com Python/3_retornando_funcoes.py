def calcular(operacao):
    
    def somar(a,b):
        return a + b
    
    def subtrair(a,b):
        return a - b
    
    def multiplicar(a,b):
        return a * b
    
    def dividir(a,b):
        return a / b
    
    match(operacao):
        case '+':
            return somar
        case "-":
            return subtrair
        case "*":
            return multiplicar
        case "/":
            return dividir
        case _:
            print("Operação inválida")
            return None
        
print(calcular("+")) # Exibe referência a funçãp

# Repassando o argumento das funções de dentro (somar, subtrair, multi, dividir)
print(calcular("+")(5, 5))
print(calcular("-")(5, 5))
print(calcular("*")(5, 5))
print(calcular("/")(5, 5))

# Outra forma de repassar o argumento, dessa vez através de uma variáveç
soma = calcular("+")
print(soma(5, 5))