a = int(input("Digite um número: "))
if a == 0:
    print("A equação não pertence ao segundo grau!")
else:
    b = int(input("Digite outro número: "))
    c = int(input("Digite outro número: "))
    if c > 0:
        print("Número inválido.")
    else:
    # res = a * x**2 + b * x + c
        delta = b ** 2 - (4 * a * c)

        raizDelta = delta **  (1 / 2)

        x1 = (- b + raizDelta) / (2 * a)
        x2 = (- b - raizDelta) / (2 * a)

        if delta > 0:
            print("A primeira raiz é ", x1)
            print("A segunda raiz é ", x2)
        elif delta == 0:
            print("O delta possui apenas uma raiz real: ", delta)
        else:
            print("O delta não possui raizes reais.")