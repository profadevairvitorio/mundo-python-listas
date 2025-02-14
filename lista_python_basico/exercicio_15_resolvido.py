# 15. Peça um texto e conte quantas vezes cada palavra aparece. Use Collections de String
from collections import Counter

texto = input("Digite um texto: ")

palavras = texto.split()

# Contando as palavras usando Counter
contagem = Counter(palavras)

print("Contagem das palavras:", contagem)