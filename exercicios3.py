#a=append(incrementar)
#r=read(leitura)
#w=write(escrita)
#r+=leitura + escrita
# palavra=open("teste2.txt","x")
# print(palavra)
# print(palavra.readable())
# print(palavra.read())
# print(palavra.readline())
# print(palavra.readline())
# print(palavra.readline())
# print(palavra.readline())

# lista = palavra.readlines()
# print(lista)

# print(lista[4])

# palavra.write("\nPython")
# palavra.write("\nJava Script")
# palavra.write("\nPython")

# palavra.close()

# import os
# if os.path.exists("teste1.txt"):
#      os.remove("teste1.txt")
# else:
#         print("Arquivo não existe")

# # import os
# # os.rmdir("./nova pasta")

#****************Manipulação de arquivos ***************************
#Exercicio 1 Leitura de uma arquivo de texto e exibir na tela
# texto=open("teste.txt","a")
# print("texto.txt")
# texto.close()
#-----------------------------------------------------------------
#Exercicio 2 Peça ao usuario pra inserir um texto e salvar em um arquivo
# arquivo = input(">> Digite o nome do arquivo para ler: ")
# with open(arquivo, "r") as x:
#     leitor = x.read()
#     print("## Conteúdo do arquivo:\n" + leitor)
#---------------------------------------------------------------------------------       
#Exercicio 3 Contagem de linhas conte o numero de linhas em um aarquivo de texto
# arquivo = input(">> Digite o nome do arquivo para contar linhas: ")

# with open(arquivo, "r") as teste:
#     linhas = teste.readlines()
#     linha_conta = len(linhas)
#     print("## Número de linhas no arquivo: " + str(linha_conta))         
#----------------------------------------------------------------------------------------

#Exercicio 4 Cópia de um arquivo crie a cópia de um arquivo existente
# arquivo1 = input(">> Digite o nome do arquivo de origem: ")
# arquivo2 = input(">> Digite o nome do arquivo de destino: ")

# with open(arquivo1, "r") as f1:
#     content = f1.read()
#     with open(arquivo2, "w") as f2:
#         f2.write(content)

#------------------------------------------------------------------------------------------

#Exercicio 5 Adicionar conteudo em um arquivo. Peça ao usuario adicionar um texto no final de um arquivo existente

# arquivo = input(">> Digite o nome do arquivo para adicionar conteúdo: ")
# with open(arquivo, "a") as f1:
#     content = input(">> Digite o conteúdo para adicionar ao arquivo: ")
#     f1.write(content + "\n")
#     print("## Conteúdo adicionado ao arquivo com sucesso.")









