# 4. Solicitar ao usuário a temperatura em Celsius
# A função input() recebe o valor como uma string, então usamos float() para converter em número decimal.
celsius = float(input("Digite a temperatura em Celsius: "))

# Calcular a temperatura em Fahrenheit
# A fórmula para converter Celsius para Fahrenheit é: (Celsius * 9/5) + 32
fahrenheit = (celsius * 9/5) + 32

# Exibir o resultado da conversão
# Usamos print() para exibir a temperatura convertida em Fahrenheit.
print("A temperatura em Fahrenheit é:", fahrenheit)
