numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite outro numero: "))
numero3 = int(input("Digite mais um numero: "))

if numero1 > numero2 or numero2 > numero3:
    print(numero1, numero2, numero3)
elif numero2 > numero1 or numero1 > numero3:
    print(numero2, numero1, numero3)
elif numero2 > numero3 or numero3 > numero1:
    print(numero2, numero3, numero1)
else:
    print("Numeros Iguais.")