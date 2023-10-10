#Escreva um programa que leia o código de um alimento e mostre sua classificação de
#acordo com a tabela abaixo: (questão no pdf)

codigo = int(input("___MENU___\n1 - Alimento não-perecível\n2 - Alimento perecível\n3 - Vestuário\n4 - Limpeza\n\nDigite um codigo (de 1 a 4) "))

if(codigo == 1):
    print("Alimento não-perecível")
elif(codigo == 2):
    print("Alimento perecível")
elif(codigo == 3):
    print("Vestuário")
else:
    print("Limpeza")

