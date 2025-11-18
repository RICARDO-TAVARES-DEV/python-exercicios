#------------------MANIPULAÇÃO DE STRINGS----------------------------
# EXERCICIO 1 PEDIR AO USUARIO UMA PALAVRA E ESTA APARECER INVERTIDA
palavra = input("Digite uma palavra: ")
#  transforma a string em lista de caracteres
# #Peguei a minha palavra e transformei em uma lista pra depois inverter com o reverse
lista = list(palavra) 
print("Lista de caracteres:", lista)
# inverte a lista aqui eu utilizei o reverse pra inverter a minha lista 
lista.reverse()
print("Lista invertida:", lista)
# junta de volta em uma string e aqui eu ja estou usando o join pra voltar a ser uma string
novapalavra = "".join(lista)
print("Palavra invertida:", novapalavra)
#-----------------------------------------------------------------------------------------------------

#EXERCICIO 2:CONTAGEM DE VOGAIS EM UMA PALAVRA DIGITADA PELO USUARIO
palavra = input("Digite uma palavra: ")
vogais = ["a", "e", "i", "o", "u"]
contador = 0 #o contador vai servir pra contar quantas vogais estão contidas na palavra
for letra in palavra: # O laço de repetição for vai verificar cada letra na palavra
    if letra in vogais:# caso encontre vogal some um e no final descobrimos quantas vogais temos
        contador += 1

print(f"A palavra '{palavra}' tem {contador} vogais.")

#EXERCICIO 3 : PALINDROMO
palavra1 = input("Digite sua primeira palavra: ")
palavra2 = input("Digite a sua segunda palavra: ")

# Converter a primeira palavra em uma lista.
lista1 = list(palavra1)

# Converter a segunda palavra em outra lista e inverter
lista2 = list(palavra2)
lista2.reverse()

# Verificar se as duas são iguais
if lista1 == lista2:
    print("Isso é um palíndromo")
else:
    print("Isso não é um palíndromo")
    
#Exercicio 4: Substituição de palavras
frase=input("Digite sua frase com pelo menos três palavras:")
listadepalavras=frase.split()
if len(listadepalavras) >=3:
    listadepalavras[3]="Amora"
    novafrase =" ".join(listadepalavras)
    print("Nova frase :" ,novafrase)
else:
    print("A frase precisa de pelo menos 3 palavras")
    
#Exercicio 5: Nome com sobrenome = nome completo
nome=input("Digite seu nome : ")
sobrenome=input("Digite seu sobrenome: ")
nomecompleto=(nome+" "+sobrenome)
print(nomecompleto)

Exercicio 6:Verificar se são anagramas
palavra1 = input('Digite sua primeira palavra: ')
palavra2 = input('Digite a outra palavra: ')

Converter em listas de letras ordenadas
novalista1 = sorted(palavra1)
novalista2 = sorted(palavra2)

print(novalista1)
print(novalista2)

Comparando as listas ordenadas iremos verificar se são anagramas ou não.
if novalista1 == novalista2:
    print("São anagramas")
else:
    print("Não são anagramas")

       


