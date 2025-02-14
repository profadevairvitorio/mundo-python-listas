# 12. Solicite um intervalo e gere um número aleatório dentro dele. Use a Biblioteca Random
import random

inicio = int(input("Digite o valor de início do intervalo: "))

fim = int(input("Digite o valor final do intervalo: "))

# Gerando um número aleatório dentro do intervalo
print("Número aleatório:", random.randint(inicio, fim))
