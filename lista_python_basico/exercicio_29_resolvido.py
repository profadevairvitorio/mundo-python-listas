# 29. Você recebeu um pagamento em dólares e quer converter para reais.
# Peça um valor em dólares e exiba o equivalente em reais, considerando que 1 dólar = 5,00 reais.
dolares = float(input("Digite o valor em dólares: "))

# Convertendo dólares para reais

reais = dolares * 5

print(f"O valor em reais é: R${reais:.2f}")
