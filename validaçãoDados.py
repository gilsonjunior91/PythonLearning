
nome = []

print("\n\tVALIDAÇÃO DE DADOS \n")

while True:
    nome = input("\nDIGITE SEU NOME: ")
    if len(nome) < 3:
        print("\nO NOME PRECISA SER MAIOR QUE 3 CARACTERES!\n")
    else:
        print("\n SALVO!\n")
        break

while True:
    idade = int(input("\nDIGITE SUA IDADE: "))
    if idade < 0 or idade > 150:
        print("\nIDADE FORA DOS PADRÕES ACEITÁVEIS!\n")
    else:
        print("\nSALVO!\n")
        break

while True:
    salario = float(input("\nDIGITE SEU SALÁRIO: R$"))
    if salario < 0 and salario < 999999999:
        print("\nSALÁRIO INCOMPATÍVEL.\n")
    else:
        print("\nSALVO!\n")
        break

while True:
    sexo = input("\nDIGITE SEU SEXO: \n[M]- MASCULINO \n[F]- FEMENINO  \n[O]- OUTROS \n OPÇÃO ESCOLHIDA: ")
    if sexo == 'm' or sexo == 'M':
        print("\nSALVO!\n")
        break
    elif sexo == 'f' or sexo == 'F':
        print("\nSALVO!\n")
        break
    elif sexo == 'o' or sexo == 'O':
        print("\nSALVO!\n")
        break
    else:
        print("\nFORA DOS PADRÕES ACEITÁVEIS.\n")
        break

while True:
    estadoCivil = input("\nDIGITE O ESTADO CIVIL: \n [S]- SOLTEIRO(A) \n [C]- CASADO(A) \n [V]- VIÚVO(A) \n [D]- DIVORCIADO \n OPÇÃO ESCOLHIDA: ")

    if estadoCivil == 's' or estadoCivil == 'S':
        print("\nSALVO!\n")
        break
    elif estadoCivil == 'c' or estadoCivil == 'C':
        print("\nSALVO!\n")
        break
    elif estadoCivil == 'v' or estadoCivil == 'V':
        print("\nSALVO!\n")
        break
    elif estadoCivil == 'd' or estadoCivil == 'D':
        print("\nSALVO!\n")
        break
    else:
        print("\nFORA DOS PADRÕES ACEITÁVEIS.\n")
        