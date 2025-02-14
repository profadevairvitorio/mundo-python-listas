# 16. Gere uma senha aleatória de 8 caracteres.
import random
import string

# Gerando uma senha aleatória com 8 caracteres
senha = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

print("Senha aleatória:", senha)