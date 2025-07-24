# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input().strip())

# TODO: Crie um loop para armazenar participantes e seus temas:
for _ in range(n):
    linha = input().strip()
    valores = linha.split(",")
    participante = valores[0].strip()
    tema = valores[1].strip()
    
    if tema not in eventos:
        eventos.setdefault(tema, [participante])
    else:
        eventos[tema] += [participante]

# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")