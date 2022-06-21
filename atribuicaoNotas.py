nota1 = float(input("Digite uma nota: "))
nota2 = float(input("Digite outra nota: "))

med = ((nota1 + nota2) / 2)

if med > 9.0 or med == 10.0:
    print("\nNota 1 ", nota1, "\nNota 2 ", nota2)
    print("\nA media do aluno foi ", med)
    print("\nSeu conceito foi A - APROVADO")
elif med >= 7.5 or med == 9.0:
     print("\nNota 1 ", nota1, "\nNota 2 ", nota2)
     print("\nA media do aluno foi ", med)
     print("\nSeu conceito foi B - APROVADO")
elif med >= 6.0 or med == 7.5:
     print("\nNota 1 ", nota1, "\nNota 2 ", nota2)
     print("\nA media do aluno foi ", med)
     print("\nSeu conceito foi C - APROVADO")
elif med >= 4.0 or med == 6.0:
     print("\nNota 1 ", nota1, "\nNota 2 ", nota2)
     print("\nA media do aluno foi ", med)
     print("\nSeu conceito foi D - REPROVADO")
elif med < 4.0 or med <= 0.0:
     print("\nNota 1 ", nota1, "\nNota 2 ", nota2)
     print("\nA media do aluno foi ", med)
     print("\nSeu conceito foi E - REPROVADO")
else:
    print("Essa nota não é valida!")