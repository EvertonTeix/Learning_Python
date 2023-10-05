#Escreva um programa que leia as três notas de um aluno, calcule a média final e
#escreva a situação do aluno na disciplina de acordo com a média final: Reprovado (0 à
#3.9), Prova Final (4 à 6.9) e Aprovado (7 à 10).

nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))

media = (nota1 + nota2 + nota3)/3

if(media <= 3.9 and media >= 0):
    print("Reprivado ", media)
elif(media >= 4 and media <= 6.9):
    print("Prova Final", media)
elif(media >= 7 and media <=10):
    print("Aprovado", media)
else:
    print("Notas inválidas!")