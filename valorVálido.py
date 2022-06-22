nota = -1

while nota < 0 or nota > 10.0:
    nota = float(input("DIGITE UMA NOTA: "))
    if nota < 0 or nota > 10.0:
        print("\nVALOR INVÁLIDO!")
    else:
        print("\nVALOR VÁLIDO!")
