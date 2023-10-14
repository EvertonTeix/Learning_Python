#Implemente um algoritmo que receba o valor do produto e a forma de pagamento.
#1= à vista;
#2= à prazo.
#Se o produto for pago à vista aplique um desconto de 10% antes de mostrar o valor
#final, senão informe o valor da prestação, sabendo que a divisão é feita de 5 vezes.

valorProduto = float(input("Informe o valor do produto: "))
formaPagamento = int(input("___MENU___\n1 - À vista\n2 - À prazo\nInforme a forma de pagamento: "))

if(formaPagamento == 1):
    valorProduto -= (valorProduto * 0.1)
    print(valorProduto)
elif(formaPagamento == 2):
    valorProduto = valorProduto/5
    print("O valor da prestacao é ", valorProduto)
else:
    print("Numero invalido")