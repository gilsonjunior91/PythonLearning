horaTrabalho = int(input("Digite a quantidade de horas trabalhadas: "))
valorHora = float(input("Digite o valor da sua hora: R$"))

salarioBruto = horaTrabalho * valorHora

if salarioBruto <=900.0:
    fgts = salarioBruto * 0.11
    descontos = salarioBruto * 0.03
    salarioLiquido = salarioBruto - descontos
    print("O salário bruto (",horaTrabalho, "*",valorHora, ") é R$", salarioBruto)
    print("(-) I.R = ISENTO")
    print("(-) FGTS (11%): R$", fgts)
    print("Total de descontos: R$", descontos)
    print("Salário Liquido: R$", salarioLiquido)
elif salarioBruto > 901.0 and salarioBruto <=1500.0:
    fgts = salarioBruto * 0.11
    iR = salarioBruto * 0.05
    descontos = ((salarioBruto * 0.03) + iR)
    salarioLiquido = salarioBruto - descontos
    print("O salário bruto (", horaTrabalho, "*", valorHora, ") é R$", salarioBruto)
    print("(-) I.R = 5%")
    print("(-) FGTS (11%): R$", fgts)
    print("Total de descontos: R$", descontos)
    print("Salário Liquido: R$", salarioLiquido)
elif salarioBruto > 1501.0 and salarioBruto <2500.0:
    fgts = salarioBruto * 0.11
    iR = salarioBruto * 0.10
    descontos = ((salarioBruto * 0.03) + iR)
    salarioLiquido = salarioBruto - descontos
    print("O salário bruto (", horaTrabalho, "*", valorHora, ") é R$", salarioBruto)
    print("(-) I.R = 10%")
    print("(-) FGTS (11%): R$", fgts)
    print("Total de descontos: R$", descontos)
    print("Salário Liquido: R$", salarioLiquido)
elif salarioBruto > 2501.0:
    fgts = salarioBruto * 0.11
    iR = salarioBruto * 0.20
    descontos = ((salarioBruto * 0.03) + iR)
    salarioLiquido = salarioBruto - descontos
    print("O salário bruto (", horaTrabalho, "*", valorHora, ") é R$", salarioBruto)
    print("(-) I.R = 20%")
    print("(-) FGTS (11%): R$", fgts)
    print("Total de descontos: R$", descontos)
    print("Salário Liquido: R$", salarioLiquido)