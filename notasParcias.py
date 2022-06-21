nota1 = float(input("Digite uma nota: "))
nota2 = float(input("Digite outra nota: "))
nota3 = float(input("Digite outra nota: "))

med = ((nota1 + nota2 + nota3) / 3)

if med == 10.0:
    print("\nFOI APROVADO COM DISTINÇÃO COM A MÉDIA ", med)
elif med >= 7.0 or med == 9.5:
     print("\nFOI APROVADO COM A MÉDIA ", med)
elif med < 7.0:
     print("\nFOI REPROVADO COM A MÉDIA ", med)
else:
    print("ESSA NOTA NÃO É VÁLIDA!")