# 17. Peça um texto e exiba quantas vezes cada caractere aparece.
from collections import Counter

texto = input("Digite um texto: ")

# Contando a frequência dos caracteres
contagem = Counter(texto)

print("Contagem dos caracteres:", contagem)