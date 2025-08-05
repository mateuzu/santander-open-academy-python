from pathlib import Path

# exceção de arquivo não encontrado
try:
    arquivo = open('arquivo_inexistente', 'r')
except FileNotFoundError as e:
    print("Arquivo não encontrado!")
    print(e)
    
ROOT_PATH = Path(__file__).parent

# exceção de diretório
try:
    arquivo = open(ROOT_PATH / "diretorio_inexistente")
except IsADirectoryError as exc:
    print(f"Não foi possível abrir o arquivo: {exc}")