# 28. Um número primo só é divisível por 1 e por ele mesmo. Peça um número e diga se ele é primo ou não. Use sympy
import sympy

num = int(input("Digite um número: "))

# Verificando se o número é primo usando sympy
if sympy.isprime(num):
    print(f"O número {num} é primo.")
else:
    print(f"O número {num} não é primo.")
