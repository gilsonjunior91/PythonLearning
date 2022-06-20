nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media == 10.0:
    print("Foi aprovado com distinção.")
elif media >= 7.0 and media <=9.5:
    print("Você foi aprovado com a média ", media)
else:
    print("Voce foi reprovado com a média", media)