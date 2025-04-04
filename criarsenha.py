# Programa para criar senha de acordo com um tamanho de caracteres 
import random
import string
def criar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha
try:
    tamanho = int(input("Digite o tamanho da senha desejada: "))
    if tamanho < 4:
        print("O tamanho da senha deve ter mais que 4 caracteres.")
    else:
        senha_gerada = gerar_senha(tamanho)
        print(f"Senha gerada: {senha_gerada}")
except ValueError:
    print("Por favor, insira um número válido.")
