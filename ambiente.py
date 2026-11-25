
import os

with open(".env", "r") as arquivo:
    for linha in arquivo:
        nome, valor = linha.strip().split("=", 1)
        os.environ[nome] = valor

chave = os.getenv("API_KEY")

if chave:
    print("Variável de ambiente lida com sucesso!")
else:
    print("Variável de ambiente não encontrada.")
