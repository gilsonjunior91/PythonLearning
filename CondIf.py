idade = int(input("Digite a idade: "))
if idade == 16:
   print("Pode votar!")
else:
    if idade >= 16:
        print("Pode dirigir!")
    else:
        if idade < 16:
            print("Apenas estude!")