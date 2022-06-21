print("Os valores são de um triângulo?  ")

a = float(input("\nDigite um número: "))
b = float(input("Digite outro número: "))
c = float(input("Digite outro número: "))

soma = a + b

if soma > c:
    if a == b and  b == c:
        print("É um triângulo Equilátero.")
    elif a == b and b != c:
        print("É um triângulo Isósceles.")
    elif a != b and b != c:
        print("É um triângulo Escaleno.")
    else:
        print("Não forma um triângulo.")
else:
    print("Não é um triângulo!")