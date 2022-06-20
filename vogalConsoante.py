letra = input("Digite uma letra: ")

if letra.isalpha():
    if (letra == 'a' or letra == 'A'):
        print("A letra digitada é uma Vogal.")
    elif (letra == 'e' or letra == 'E'):
        print("A letra digitada é uma Vogal.")
    elif (letra == 'i' or letra == 'I'):
        print("A letra digitada é uma Vogal.")
    elif (letra == 'o' or letra == 'O'):
        print("A letra digitada é uma Vogal.")
    elif (letra == 'u' or letra == 'U'):
        print("A letra digitada é uma Vogal.")
    else:
        print(" A letra digitada é uma Consoante.")
else:
    print("Não é letra!")