produto= float(input("Digite o primeiro preço: R$"))
produto1 = float(input("Digite o segundo preço: R$"))
produto2 = float(input("Digite o terceiro preço: R$"))

if produto > produto1 and produto1 > produto2:
    print("1-O maior valor foi R$", produto)
    print("1-O menor valor foi R$", produto2)
elif produto1 > produto and produto > produto2:
    print("2-O maior valor foi R$", produto1)
    print("2-O menor valor foi R$", produto2)
elif produto2 > produto and produto1 > produto:
    print("3-O maior valor foi R$", produto2)
    print("3-O menor valor foi R$", produto)
else:
    print(" Os valores são iguais.")
    print("-O maior valor foi R$", produto2)
    print("-O menor valor foi R$", produto)
    print("-O maior valor foi R$", produto1)

