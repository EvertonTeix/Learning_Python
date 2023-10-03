#Em um mercado, as maçãs custam R$ 0,85 cada se forem compradas menos do que
#uma dúzia, e R$ 0,75 se forem compradas mais. Escreva um programa que leia o
#número de maçãs compradas, calcule e escreva o valor total da compra.

macas = int(input("Digite o número de maçãs que deseja comprar: "))

if (macas < 12):
    macas *= 0.85
    print("O total é: ", macas)

else:
    macas *= 0.75
    print("O total e: ", macas)