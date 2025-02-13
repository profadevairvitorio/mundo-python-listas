# 10. Solicite o preço de um produto e o percentual de desconto, depois exiba o valor final.

preco = float(input("Digite o preço do produto: "))

desconto = float(input("Digite o percentual de desconto: "))

# Calculando o valor final com o desconto
valor_final = preco * (1 - desconto / 100)

print("Preço com desconto:", valor_final)