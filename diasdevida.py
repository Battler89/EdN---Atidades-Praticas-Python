# Programa para calcular a idade em dias de vida
from datetime import date
def idade_em_dias(ano):
    ano_atual = date.today().year
    idade = ano_atual - ano
    return idade * 365
ano = int(input("Digite o ano de seu nascimento: "))
print(f"Você tem aproximadamente {idade_em_dias(ano)} dias de vida.")
