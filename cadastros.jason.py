import json
import os

def carregar_cadastros():
    """Carrega os cadastros de um arquivo JSON, se existir."""
    if os.path.exists("cadastros.json"):
        with open("cadastros.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_cadastros(cadastros):
    """Salva os cadastros em um arquivo JSON."""
    with open("cadastros.json", "w", encoding="utf-8") as f:
        json.dump(cadastros, f, ensure_ascii=False, indent=2)

def cadastrar_pessoa():
    """Cadastra uma pessoa e retorna um dicionário com os dados."""
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura (em metros): "))
    return {"nome": nome, "idade": idade, "altura": altura}

def calcular_media_idade(cadastros):
    """Calcular e retorna a média da idades."""
    total_idades = sum(pessoa['idade'] for pessoa in cadastros)
    return total_idades / len(cadastros) if cadastros else 0

def calcular_media_alturas(cadastros):
    """Calcula e retorna média das alturas."""
    total_alturas = sum(pessoa['altura'] for pessoa in cadastros)
    return total_alturas / len(cadastros) if cadastros else 0

def pessoa_mais_velha(cadastros):
    """Retorna a pessoa mais velha."""
    return max(cadastros, key=lambda x: x['idade'], default=None)

def pessoa_mais_baixa(cadastros):
    """Retorna a pessoa mais baixa."""
    return min(cadastros, key=lambda x: x['altura'], default=None)

def mostrar_relatorio(cadastros):
    """mostra o relatório final com as informações dos cadastros."""
    print(f"\nTotal de pessoa cadastradas: {len(cadastros)}")
    print(f"Média das idade: {calcular_media_idade(cadastros):.2f}")
    print(f"média das alturas: {calcular_media_alturas(cadastros):.2f} m")

    pessoa_velha = pessoa_mais_velha(cadastros)
    if pessoa_velha:
        print(f"A pessoa mais velha: {pessoa_velha['nome']} ({pessoa_velha['idade']} anos)")

    pessoa_baixa = pessoa_mais_baixa(cadastros)
    if pessoa_baixa:
        print(f"A pessoa amis baixa: {pessoa_baixa['nome']} ({pessoa_baixa['altura']:.2f} m)")

def main():
    cadastros = carregar_cadastros()

    while True:
        cadastros.append(cadastrar_pessoa())
        salvar_cadastros(cadastros)  #Salva os cadastos após cada adoção
        continuar = input("deseja cadastra outra pessoa? (s/n): ").strip().lower()
        if continuar != 's':
            break

    mostrar_relatorio(cadastros)

if __name__ =="__main__":
    main()