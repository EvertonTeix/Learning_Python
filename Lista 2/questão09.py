#Escreva um programa para ler 3 valores inteiros (considere que não serão lidos
#valores iguais) e escreva qual o maior.

num1 = int(input("Digite o primeiro valor inteiro: "))
num2 = int(input("Digite o segundo valor inteiro: "))
num3 = int(input("Digite o terceiro valor inteiro: "))

if(num1 > num2 and num1 > num3):
    print(num1)
elif(num2 > num1 and num2 > num3):
    print(num2)
else:
    print(num3)