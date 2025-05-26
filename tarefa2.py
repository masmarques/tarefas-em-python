#tarefas2.py

def mostrar_dados(nome,idade,altura):
    """Exibe os dados formatados."""
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Altura {altura:.2f} m") #Formata a altura para 2 casa decimais

def eh_par(numero):
    """Retorna True se o número for par, False se for ímpar."""
    return numero % 2 == 0

def calcular_operacoes(n1, n2):
    """Retorna uma tupla com soma, subtração, multiplicação e divisão."""
    soma = n1 + n2
    subtracao = n1- n2
    multiplicacao = n1 * n2
    divisao = n1 / n2 if n2 != 0 else "Idefinido (divisão por zero)"
    return soma, subtracao, multiplicacao, divisao

def menu():
    """Exibe o menu de opções."""
    print("\nMenu:")
    print("1. Mostar dados")
    print("2. Verificar se um número é par")
    print("3. Calcular operações")
    print("4. Sair")

def main():
    while True:
        menu()
        opcao = input("Escolha uma Opção: ")

        if opcao == '1':
            nome = input("Digite seu nome: ")
            idade = int(input("Digite sua idade: "))
            altura = float(input("Digite sua altura (em metros):"))
            mostrar_dados(nome, idade, altura)

        elif opcao == '2':
            numero = int(input("Digite um número: "))
            if eh_par(numero):
                print(f"O número {numero} é par. ")
            else:
                print(f"O número {numero} é ímpar. ")

        elif opcao == '3':
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            soma, subtracao, multiplicacao, divisao = calcular_operacoes(n1, n2)
            print(f"Soma: {soma}")
            print(f"Subtração: {subtracao}")
            print(f"Multiplicação: {multiplicacao}")
            print(f"Divisão: {divisao}")

        elif opcao == '4':
            print("Saindo do programa...")
            break

        else:
            print( "Opção inválida. Tente novamente.")

if __name__=="__main__":
    main()


