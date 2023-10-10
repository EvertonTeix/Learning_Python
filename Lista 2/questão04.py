#Peça ao usuário para inserir uma temperatura em graus Celsius e permita que ele
#escolha se deseja convertê-la para Fahrenheit ou Kelvin. Realize a conversão e exiba
#o resultado

temperatura = int(input("Digite uma temperatua em graus Celsius: "))

menu = int(input("____MENU____\n1 - Celsius para Fahrenheit\n2 - Celsius para Kelvin\n"))

if(menu == 1):
     fahrenheit = (temperatura * 9/5) + 32
     print(fahrenheit)
else:
     kelvin = temperatura + 273.15
     print(kelvin)

