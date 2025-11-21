# # ******************LÓGICA DE PROGRAMAÇÃO *********************
# # EXERCICIO 1: VERIFICAR SE UM NUMERO É ÍMPAR OU PAR

# num=int(input("Digite um número: "))
# if num%2==0:
#         print(f"O número digitado {num} é par.")
# else:
#         print(f"O número digitado {num} é ímpar.")

# ---------------------------------------------------------------------------------------------------
# # EXERCICIO 2 : CALCULADORA SIMPLES DE DOIS DIGITOS praticamente temos a função calculadora com os seguintes elementos os dois valores a serem utilizados e as teclas de operações, que nesse caso são soma(+), subtração(-),multiplicação(*) e divisão(/)

# operacoes = ("+", "-", "*", "/")

# def calculadora(a, b, operacao):
#     if operacao == "+":  # soma
#         resultado = a + b
#         print(f"A soma destes números é igual a: {resultado}")
#         return resultado

#     elif operacao == "-":  # subtração
#         if a >= b:
#             resultado = a - b
#             print(f"A subtração destes números é igual a: {resultado}")
#             return resultado
#         else:
#             print("Erro: subtração não é permitida (a < b).")
#             return None

#     elif operacao == "*":  # multiplicação
#         resultado = a * b
#         print(f"A multiplicação destes números é igual a: {resultado}")
#         return resultado

#     elif operacao == "/":  # divisão
#         if b != 0:
#             resultado = a / b
#             print(f"A divisão destes números é igual a: {resultado}")
#             return resultado
#         else:
#             print("Erro: divisão por zero não é permitida.")
#             return None

#     else:
#         print("Operação inválida.")
#         return None


# #exemplo de uso
# calculadora(80, 90, "-")
# #----------------------------------------------------------------------------------------------------

# # EXERCICIO 3 FATORIAL DE UM NÚMERO
# import #math pois e uma biblioteca que facilita
# numero = int(input("Digite seu número: "))
# print(f"O fatorial de {numero} é {math.factorial(numero)}") #aqui eu so chamei a biblioteca atribuindo o valor fatorial
# #-------------------------------------------------------------------------------------------------------------------

# # Exercício 4: Média de uma lista de números
# #O Usuário digita os números separados por espaço dando tab
# entrada = input("Digite os números separados por espaço: ")
# #Convertemos para lista de inteiros,pois a principio a lista so e strings
# numeros = [int(x) for x in entrada.split()]#o split ele divide em lista os numeros da entrada separados por tab
# # Calcula soma e média
# soma = sum(numeros) #o sum ele soma os valores soma e so o nome
# media = soma / len(numeros) #com o len a gente tem a quantidade de elementos da lista,
# print(f"A média dos números é: {media}")
# --------------------------------------------------------------------------------------------------

# #EXERCICIO 5 CALCULAR A POTENCIA PEDINDO AO USUARIO DOIS NUMEROS ONDE
# #UM E A BASE E OUTRO EXPOENTE
# num1=int(input("Digite o primeiro número: "))
# num2=int(input("Digite o segundo número:"))
# potencia=(num1**num2)
# print(potencia)




















