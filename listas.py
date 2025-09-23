#Exercício 6 - Listas
"""
Crie um programa que:

> Peça 5 números ao usuário e os armazene em uma lista.
> Mostre a lista completa.
> Mostre o maior e o menor número digitado.
"""

num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))
num4 = int(input("Digite um número: "))
num5 = int(input("Digite um número: "))
lista = [num1, num2, num3, num4, num5]

print(f"Lista: {lista}")

print("O maior número da lista é: ", max(lista))
print("O menor número da lista é: ", min(lista))