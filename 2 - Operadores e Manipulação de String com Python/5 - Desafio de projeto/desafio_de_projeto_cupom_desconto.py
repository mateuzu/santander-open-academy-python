# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input().strip())
cupom = input().strip()
valor_desconto = 0

# TODO: Aplique o desconto se o cupom for válido:
if cupom in descontos:
    valor_desconto = descontos.get(cupom)
    preco -= (preco * valor_desconto)

print(f"{preco:.2f}")