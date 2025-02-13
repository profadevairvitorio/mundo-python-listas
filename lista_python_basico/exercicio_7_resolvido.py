# Solicitar o valor total da compra
valor_compra = float(input("Digite o valor da compra: "))

# Solicitar o valor pago pelo cliente
valor_pago = float(input("Digite o valor pago: "))

# Calcular o troco
troco = valor_pago - valor_compra

# Troco
print(f"O troco é: R${troco:.2f}")
