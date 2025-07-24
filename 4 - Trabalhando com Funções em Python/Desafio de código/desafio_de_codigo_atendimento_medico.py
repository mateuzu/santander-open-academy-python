# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes
pacientes = []
pacientes_ordenados = []
nomes = []

# Loop para entrada de dados
for _ in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status))

print(pacientes[0])

# TODO: Ordene por prioridade: urgente > idosos > demais:
def calcular_prioridade(paciente):
    nome, idade, status = paciente

    if status == "urgente":
        prioridade = 0
    elif idade >= 60:
        prioridade = 1
    else:
        prioridade = 2

    return (prioridade, -idade)

pacientes_ordenados = sorted(pacientes, key=lambda x: calcular_prioridade(x))

# TODO: Exiba a ordem de atendimento com título e vírgulas:
for paciente in pacientes_ordenados:
    nomes.append(paciente[0])

print("Ordem de Atendimento:", " ".join(nomes).replace(" ", ", "))