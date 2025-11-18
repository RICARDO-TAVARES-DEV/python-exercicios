f = open('arquivo_de_trabalho', 'r', encoding="utf-8")
with open('arquivo_de_trabalho', encoding="utf-8") as f:
    read_data = f.read()

# Podemos verificar se o arquivo foi fechado automaticamente.
f.closed
