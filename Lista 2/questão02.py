#Faça um programa que o usuário informe o salário recebido e o total gasto. Deverá ser
#exibido na tela “Gastos dentro do orçamento” caso o valor gasto não ultrapasse o
#valor do salário e “Orçamento estourado” se o valor gasto ultrapassar o valor do
#salário

salario = float(input("Informe o salário recebido: "))
gastos = float(input("Informe o total gasto: "))

if(gastos <= salario):
    print("Gastos dentro do orçamento")
else:
    print("Orçamento estourado")