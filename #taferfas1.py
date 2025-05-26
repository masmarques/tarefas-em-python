#taferfas1.py

nome = "João"
idade = 25
altura= 1.75

print(f"Nome: {nome}")
print(f"idade: {idade}")
print(f"Altura: {altura:.2f} m")

numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print(f" O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar")


num1 = float(input(" Digite o primeiro número:"))
num2 = float(input("Digite o segundo número:"))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2 if num2!= 0 else "Indefinido (divisão por zero)"

print (f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")