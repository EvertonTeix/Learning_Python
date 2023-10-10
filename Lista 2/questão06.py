#Implemente um algoritmo que receba um número inteiro e verifique se este é divisível
#por 3 e por 5 ao mesmo tempo.

numero = int(input("Digite um número: "))

if(numero % 3 == 0 and numero % 5 == 0):
    print("Número divisível por 3 e por 5 ao mesmo tempo")
else:
    print("Número não divisível por 3 e por 5 ao mesmo tempo")