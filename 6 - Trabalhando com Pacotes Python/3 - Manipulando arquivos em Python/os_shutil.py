import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# Criando um diretório
# os.mkdir(ROOT_PATH / "novo_diretorio")

arquivo = open(ROOT_PATH / 'novo_arquivo.txt', 'w')
arquivo.close()

os.rename(ROOT_PATH / "novo_arquivo.txt", ROOT_PATH / "alterado.txt")

os.remove(ROOT_PATH / "alterado.txt")

arquivo = open(ROOT_PATH / 'arquivo_mover.txt', 'w')
arquivo.close()

shutil.move(ROOT_PATH / 'arquivo_mover.txt', ROOT_PATH / 'novo_diretorio' / 'arquivo_mover.txt')