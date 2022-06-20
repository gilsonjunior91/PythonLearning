n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
n3 = int(input("Digite mais um numero: "))

if n1 > n2 and n2 > n3:
    print("1-O maior número foi ",n1 )
elif n2 > n1 and n1 > n3:
    print("2-O maior número foi: ", n2)
elif n3 > n2 and n2 > n1:
    print("3-O maior número foi: ", n3)
else:
    print(" Os numeros são iguais.")