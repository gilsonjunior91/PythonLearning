letra = input("Digite uma letra: ")

if (letra == 'f' or letra == 'F'):
    print("A letra digita representa FEMININO.")
elif letra == 'm' or letra == 'M':
    print("A letra digitada representa MASCULINO")
elif letra == 'o' or letra == 'O':
    print("A letra digitada representa a OUTROS")
else:
    print("Sexo inválido!")