turno = input("Escolha o seu turno: [M]-Matutino [V]-Vespertino [N]-Noturno => ")

if turno == 'm' or 'M':
    print("Bom dia!")
elif turno == 'v' or 'V':
    print("Boa tarde!")
elif turno == 'n' or 'N':
    print("Boa noite!")
else:
    print("Turno inválido!")