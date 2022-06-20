numero = int(input("Digite um numero: "))
numero2 = int(input("Digite outro numero: "))

if numero > numero2:
    print("O numero ", numero, "é o maior digitado.")
elif numero2 == numero:
    print("Os numeros digitados são iguais.")
else:
    print("O numero ", numero, "é menor digitado!")