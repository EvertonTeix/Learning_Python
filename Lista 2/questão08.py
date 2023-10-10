#Escreva um programa para ler 3 valores inteiros e imprima os mesmos em ordem
#crescente.

num1 = int(input("Digite o primeiro valor inteiro: "))
num2 = int(input("Digite o segundo valor inteiro: "))
num3 = int(input("Digite o terceiro valor inteiro: "))

if num1 <= num2 <= num3:
    print("Os valores em ordem crescente são:", num1, num2, num3)
elif num1 <= num3 <= num2:
    print("Os valores em ordem crescente são:", num1, num3, num2)
elif num2 <= num1 <= num3:
    print("Os valores em ordem crescente são:", num2, num1, num3)
elif num2 <= num3 <= num1:
    print("Os valores em ordem crescente são:", num2, num3, num1)
elif num3 <= num1 <= num2:
    print("Os valores em ordem crescente são:", num3, num1, num2)
else:
    print("Os valores em ordem crescente são:", num3, num2, num1)


