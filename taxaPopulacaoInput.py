
anos = 0

while True:
    paisA = float(input("\nDIGITE A QUANTIDADE DA POPULAÇÃO A: "))
    taxaA = float(input("\nDIGITE A TAXA DA POPULAÇÃO A: "))
    paisB = float(input("\nDIGITE A QUANTIDADE DA POPULAÇÃO B: "))
    taxaB = float(input("\nDIGITE A TAXA DA POPULAÇÃO B: "))
    if paisA < paisB:
        paisA = paisA + (paisA * taxaA / 100)
        paisB = paisB + (paisB * taxaB / 100)
        print("\nOK\n")
        anos = anos + 1
    else:
        print("\nNÃO FOI POSSÍVEL OBTER OS DADOS!\n")
        break

print("\nVai precisar de ", anos, " ano(s) para a população A alcançar a população B \n")