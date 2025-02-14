# 25. Seu carro tem um limite de velocidade de 100 km/h.
# Peça ao usuário a velocidade atual e informe se ele está acima do limite.
velocidade = int(input("Digite a velocidade atual do carro: "))

# Verificando se a velocidade está acima do limite
if velocidade > 100:
    print("Você está acima do limite de velocidade!")
else:
    print("Você está dentro do limite de velocidade.")