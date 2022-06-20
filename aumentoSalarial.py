salario = float(input("Digite o salário R$"))

if salario <=280.0:
    aumento = salario * 0.2
    novoSalario= salario + aumento
    print("O Salario anterior era de R$", salario)
    print("O percentual de aumento é de 20%")
    print("O valor do aumento foi de R$", aumento)
    print("O novo salário é R$", novoSalario)
elif salario > 281.0 and salario < 700.0:
    aumento = salario * 0.15
    novoSalario = salario + aumento
    print("O Salario anterior era de R$", salario)
    print("O percentual de aumento é de 15%")
    print("O valor do aumento foi de R$", aumento)
    print("O novo salário é R$", novoSalario)
elif salario > 700.0 and salario < 1500.0:
    aumento = salario * 0.10
    novoSalario = salario + aumento
    print("O Salario anterior era de R$", salario)
    print("O percentual de aumento é de 10%")
    print("O valor do aumento foi de R$", aumento)
    print("O novo salário é R$", novoSalario)
else:
    aumento = salario * 0.05
    novoSalario = salario + aumento
    print("O Salario anterior era de R$", salario)
    print("O percentual de aumento é de 5%")
    print("O valor do aumento foi de R$", aumento)
    print("O novo salário é R$", novoSalario)

