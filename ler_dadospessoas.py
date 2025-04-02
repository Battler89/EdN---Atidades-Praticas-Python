# Programa para criar um arquivo json, abrir o arquivo e exibir os dados do arquivo
import json
arquivo = "dadospessoas.json"
dados = [
    ["Nome", "Idade", "Cidade"], 
    ["Thiago", 21, "Pindamonhagaba"],
    ["Leandro", 12, "Amazonas"],
    ["João", 20, "Santa Catarina"]
]
with open(arquivo, "w", encoding="utf=8") as arquivo:
    json.dump(dados, arquivo, indent=4)
    print(f"Dados gravados em '{arquivo} com sucesso")
try:
    with open(arquivo, "r", encoding="utf=8") as arquivo:
        dados_lidos = json.load(arquivo)
        for pessoa in dados_lidos:
            print(f"Nome: {pessoa['Nome']}, Idade: {pessoa['Idade']}, Cidade: {pessoa['Cidade']}")
        print("Dados lidos no arquivo JSON: ")
        print(json.dumps(dados_lidos, indent=4, ensure_ascii=False))
except FileNotFoundError:
    print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")
except json.JSONDecodeError:
    print("Erro: arquivo JSON incorreto.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
