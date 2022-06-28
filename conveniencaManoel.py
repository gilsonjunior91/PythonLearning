
#MERCADO E CONVENIÊNCIA MANOEL JOAQUIM
opcao = 1
soma = 0
produto = 1

while True:
    opcao = int(input("\n[1]-INSERIR VALOR \n [0]-SAIR \n SUA OPÇÃO: "))
    if opcao == 1:
        while produto != 0:
            produto = float(input("\nDIGITE O VALOR DO PRODUTO: R$"))
            soma = soma + produto

        print("\n O TOTAL FOI DE R$", soma, ".\n")
        valor = float(input("\n DIGITE O VALOR EM DINHEIRO PARA PAGAR: R$"))
        troco = soma - valor
        print("\n O TROCO FOI DE R$", troco,".\n")

    elif opcao == 0:
        break
    else:
        print("\n OPÇÃO INVÁLIDA.")
