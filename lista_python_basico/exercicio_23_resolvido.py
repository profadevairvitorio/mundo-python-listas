# 23. Seu professor de matemática desafiou a turma:
# "Escreva um programa que diga se um número tem raiz quadrada exata!”
import math

num = int(input("Digite um número: "))

# Verificando se a raiz quadrada é exata
if math.sqrt(num).is_integer():
    print(f"O número {num} tem raiz quadrada exata.")
else:
    print(f"O número {num} não tem raiz quadrada exata.")

