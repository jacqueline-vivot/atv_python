#impressão de número
numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))
if numero_1 > numero_2:
        print("O maior número é:", numero_1)
else:
        print("O maior número é:", numero_2)

#média do aluno
media_do_aluno = float(input("Digite o valor da média do aluno:"))
if media_do_aluno == 10:
        print("Aprovado com distinção!")
elif media_do_aluno >=7 <10:
        print("Aprovado!") 
else:
        print("Reprovado!")