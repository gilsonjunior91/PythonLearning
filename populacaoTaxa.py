
paisA = float(80.000)
paisB = float(200.000)

anos = 0
while paisA < paisB:
    paisA = paisA + (paisA * 0.03)
    paisB = paisB + (paisB * 0.015)
    anos = anos + 1

print("\nVai precisar de ", anos, " anos para a população A alcançar a população B \n")