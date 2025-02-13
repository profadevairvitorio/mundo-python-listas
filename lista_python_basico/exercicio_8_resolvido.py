# 8. Peça dois números inteiros e mostre o resultado da divisão inteira e o resto.

# Solicitar o primeiro número inteiro
num1 = int(input("Digite o primeiro número inteiro: "))

# Solicitar o segundo número inteiro
num2 = int(input("Digite o segundo número inteiro: "))

# Calcular a divisão inteira
divisao_inteira = num1 // num2

# Calcular o resto da divisão
resto = num1 % num2

# Exibir os resultados
print(f"A divisão inteira de {num1} por {num2} é: {divisao_inteira}")
print(f"O resto da divisão é: {resto}")
