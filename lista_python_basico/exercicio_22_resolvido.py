# 22. Seu amigo propôs um jogo: quem tirar o maior número em um dado de 6 lados ganha.
# Simule o lançamento de dois dados e determine o vencedor.
import random

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)

# Exibindo os resultados dos dados
print("Dado 1:", dado1)

print("Dado 2:", dado2)

if dado1 > dado2:
    print("Vencedor: Dado 1")
elif dado2 > dado1:
    print("Vencedor: Dado 2")
else:
    print("Empate!")