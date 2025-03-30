def palindromo(texto):
    texto_invertido = ''.join(char.lower() 
                          for char in texto 
                          if char.isalnum())
    return texto_invertido == texto_invertido[::-1]
frase = input("Digite sua palavra ou frase aqui: ")
resultado = palindromo(frase)
if resultado != True:
    resposta = "Não"
else:
    resposta = "Sim"
print(f"'{frase}' é considerado um palíndromo? {resposta}")
