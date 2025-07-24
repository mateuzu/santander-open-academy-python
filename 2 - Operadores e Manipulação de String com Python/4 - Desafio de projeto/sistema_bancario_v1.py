menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numeros_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    match(opcao):
        case 'd':
            print("Depósito")
            valor = float(input("Informe o valor do depósito: "))

            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
            else:
                print("Operação falhou! O valor informado é inválido")
        
        case 's':
            print("Saque")
            valor = float(input("Informe o valor do saque: "))
            
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numeros_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente")
            elif excedeu_limite:
                print("Operação falhou! Você não tem limite suficiente")
            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido")
            elif valor > 0:
                saldo -= valor
                extrato = f"Saque: R$ {valor:.2f}\n"
                numeros_saques += 1
            else:
                print("Operação falhou! O valor informado é inválido")
        
        case 'e':
            print("Extrato")
            print("\n========= EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("=====================================")
        
        case 'q':
            print("Programa encerrado!")
            break
        
        case _:
            print("Opção inválida, tente novamente!")