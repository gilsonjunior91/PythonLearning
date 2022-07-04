codigo = 0
escolha = 1
cad = 0
cad1 = 0
cad2 = 0
can = 0
can1 = 0
can2 = 0
lap = 0
lap1 = 0
lap2 = 0
bor = 0
bor1 = 0
bor2 = 0
reg = 0
reg1 = 0
reg2 = 0
qtde = 0
prod = 0
opcao =0
contEntrada = 0 
contSaida = 0

print("\n\t------ CONTROLE DE ESTOQUE ------\n")
while opcao != 'x' or opcao != 'X':                                        #ÍNICIO DO MENU PRINCIPAL.
    print("\n ESCOLHA A OPERAÇÃO \n")
    print("[E]- ENTRADA NO ESTOQUE.")
    print("[S]- SAÍDA NO ESTOQUE.")
    print("[R]- RELATÓRIOS.")
    print("[X]- SAIR.")
    opcao = input("SUA ESCOLHA: ")
    if opcao == 'e' or opcao == 'E':                                #OPÇÃO [ENTRADAS] DO MENU PRINCIPAL.
        print("\n\t------ ENTRADA DO ESTOQUE ------\n")
        print("\tCÓDIGO || PRODUTO\n")
        print("\t  [10] ||[CADERNO]")
        print("\t  [20] ||[CANETA]")
        print("\t  [30] ||[LÁPIS]")
        print("\t  [40] ||[BORRACHA]")
        print("\t  [50] ||[RÉGUA]")
        print("\t_______________________\n")
        contEntrada = contEntrada + 1
        codigo = (int(input("\nENTRE COM O CÓDIGO DO PRODUTO: ")))
        if codigo == 10:                                            #ÍNICIO DA CONDICIONAL DA [ENTRADA]
            print("\n[10]|[CADERNO]")
            cad1 = int(input("DIGITE A QUANTIDADE DESEJADA: "))
            cad = cad + cad1
            cad2 = cad2 + 1
            print("\nREGISTRO EFETUADO COM SUCESSO.\n")
        elif codigo == 20:
            print("\n[20]|[CANETA]")
            can1 = int(input("DIGITE A QUANTIDADE DESEJADA: "))
            can = can + can1
            can2 = can2 + 1
            print("\nREGISTRO EFETUADO COM SUCESSO.\n")
        elif codigo == 30:
            print("\n[30]|[LÁPIS]")
            lap1 = int(input("DIGITE A QUANTIDADE DESEJADA: "))
            lap = lap + lap1
            lap2 = lap2 + 1
            print("\nREGISTRO EFETUADO COM SUCESSO.\n")
        elif codigo == 40:
            print("\n[40]|[BORRACHA]")
            bor1 = int(input("DIGITE A QUANTIDADE DESEJADA: "))
            bor = bor + bor1
            bor2 = bor2 + 1
            print("\nREGISTRO EFETUADO COM SUCESSO.\n")
        elif codigo == 50:
            print("\n[50]|[RÉGUA]")
            reg1 = int(input("DIGITE A QUANTIDADE DESEJADA: "))
            reg = reg + reg1
            reg2 = reg2 + 1
            print("\nREGISTRO EFETUADO COM SUCESSO.\n")
        else:
            print("CÓDIGO INVÁLIDO.")
    elif opcao =='s' or opcao == 'S':                           #OPÇÃO [SAÍDA] DO MENU PRINCIPAL.
        print("\n\t------ SAÍDA DO ESTOQUE ------\n")
        print("\tCÓDIGO || PRODUTO\n")
        print("\t  [10] ||[CADERNO]")
        print("\t  [20] ||[CANETA]")
        print("\t  [30] ||[LÁPIS]")
        print("\t  [40] ||[BORRACHA]")
        print("\t  [50] ||[RÉGUA]")
        print("\t_______________________\n")
        contSaida = contSaida + 1
        prod = int(input("\nDIGITE O CÓDIGO: "))
        if prod == 10:                                        #ÍNICIO DA CONDICIONAL [SAÍDA].
            print("\n[10]|[CADERNO]")
            qtde = int(input("DIGITE A QUANTIDADE QUE DESEJA RETIRAR: "))
            if cad > 0:
                cad = cad - qtde
                print("\nREGISTRO EFETUADO COM SUCESSO.\n")
            else:
                print("\n NÃO HÁ ESTOQUE DESSE PRODUTO.")
        elif prod == 20:
            print("\n[20]|[CANETA]")
            qtde = int(input("DIGITE A QUANTIDADE DESEJADA: "))
            if can > 0:
                can = can - qtde
                print("\nREGISTRO EFETUADO COM SUCESSO.\n")
            else:
                print("\n NÃO HÁ ESTOQUE DESSE PRODUTO.")
        elif prod == 30:
            print("\n[30]|[LÁPIS]")
            qtde = int(input("DIGITE A QUANTIDADE DESEJADA: "))
            if lap > 0:
                lap = lap - qtde
                print("\nREGISTRO EFETUADO COM SUCESSO.\n")
            else:
                print("\n NÃO HÁ ESTOQUE DESSE PRODUTO.")
        elif prod == 40:
            print("\n[40]|[BORRACHA]")
            qtde = int(input("DIGITE A QUANTIDADE DESEJADA: "))
            if bor > 0:
                bor = bor - qtde
                print("\nREGISTRO EFETUADO COM SUCESSO.\n")
            else:
                print("\n NÃO HÁ ESTOQUE DESSE PRODUTO.\n")
        elif prod == 50:
            print("\n[50]|[RÉGUA]")
            qtde = int(input("DIGITE A QUANTIDADE DESEJADA: "))
            if reg > 0:
                reg = reg - qtde
                print("\nREGISTRO EFETUADO COM SUCESSO.\n")
            else:
                print("\n NÃO HÁ ESTOQUE DESSE PRODUTO.\n")
        else:
            print("CÓDIGO INVÁLIDO.")            
    elif opcao == 'r' or opcao == 'R':                          #OPÇÃO [ENTRADAS] DO SUBMENU RELATÓRIOS.
        print("\n\t------ RELATÓRIOS ------\n")
        print(" [1]-ENTRADAS")
        print(" [2]-SAÍDAS")
        print(" [3]-VOLTAR")
        escolha = int(input("DIGITE SUA A OPÇÃO DESEJADA: "))
        if escolha == 1:                                        #ÍNICIO DA CONDICIONAL [ENTRADAS] [RELATÓRIOS]
            if contEntrada > 0:
                if cad and can and lap and bor and reg > 0:
                    print("\tCÓDIGO || PRODUTO")
                    print("\t  [10] ||[CADERNO] = ", cad)
                    print("\t  [20] ||[CANETA] = ", can)
                    print("\t  [30] ||[LÁPIS] = ", lap)
                    print("\t  [40] ||[BORRACHA] = ", bor)
                    print("\t  [50] ||[RÉGUA] = ", reg)
                elif cad > cad2:
                    print("\tCÓDIGO || PRODUTO")
                    print("\t  [10] ||[CADERNO] = ", cad)
                elif can > cad2:
                    print("\tCÓDIGO || PRODUTO")
                    print("\t  [20] ||[CANETA] = ", can)
                elif lap > lap2:
                    print("\tCÓDIGO || PRODUTO")
                    print("\t  [30] ||[LÁPIS] = ", lap)
                elif bor > bor2:
                    print("\tCÓDIGO || PRODUTO")
                    print("\t  [40] ||[BORRACHA] = ", bor)
                elif reg > reg2:
                    print("\tCÓDIGO || PRODUTO")
                    print("\t  [50] ||[RÉGUA] =", reg)
            #    if cad > 0 and can > 0:
            #        print("\tCÓDIGO || PRODUTO")
            #        print("\t  [10] ||[CADERNO] = ", cad)
            #        print("\t  [20] ||[CANETA] = ", can)
            #    if cad and lap > 0:
            #        print("\tCÓDIGO || PRODUTO\n")
            #        print("\t  [10] ||[CADERNO] = ", cad)
            #        print("\t  [30] ||[LÁPIS] = ", lap)
            #    if cad and bor > 0:
            #        print("\tCÓDIGO || PRODUTO")
            #        print("\t  [10] ||[CADERNO] = ", cad)
            #        print("\t  [40] ||[BORRACHA] = ", bor)
            #    if cad and reg > 0:
            #        print("\tCÓDIGO || PRODUTO")
            #        print("\t  [10] ||[CADERNO] = ", cad)
            #        print("\t  [50] ||[RÉGUA] =", reg)
            #    if can and lap > 0:
            #        print("\tCÓDIGO || PRODUTO")
            #        print("\t  [20] ||[CANETA] = ", cad)
            #        print("\t  [30] ||[LÁPIS] =", reg)
            #    if can and bor > 0:
            #        print("\tCÓDIGO || PRODUTO")
            #        print("\t  [20] ||[CANETA] = ", cad)
            #        print("\t  [40] ||[BORRACHA] = ", bor)
            #    if can and reg > 0:
            #        print("\tCÓDIGO || PRODUTO")
            #        print("\t  [20] ||[CANETA] = ", cad)
            #        print("\t  [50] ||[RÉGUA] =", reg)
            #    if lap and bor > 0:
            #        print("\tCÓDIGO || PRODUTO")
            #        print("\t  [30] ||[LÁPIS] =", reg)
            #        print("\t  [40] ||[BORRACHA] = ", bor)
            #    if lap and reg > 0:
            #        print("\tCÓDIGO || PRODUTO")
            #        print("\t  [30] ||[LÁPIS] =", reg)
            #        print("\t  [50] ||[RÉGUA] =", reg)
            #    if bor and reg > 0:
            #        print("\tCÓDIGO || PRODUTO")
            #        print("\t  [40] ||[BORRACHA] =", reg)
            #        print("\t  [50] ||[RÉGUA] =", reg)
            #    if lap and bor > 0:
            #        print("\t  [30] ||[LÁPIS] = ", lap)
            #        print("\t  [40] ||[BORRACHA] = ", bor)
                else:
                    if cad and can and lap > cad2 and can2 and lap2:
                        print("\tCÓDIGO || PRODUTO")
                        print("\t  [10] ||[CADERNO] = ", cad)
                        print("\t  [20] ||[CANETA] = ", can)
                        print("\t  [30] ||[LÁPIS] = ", lap)
                    elif can and lap and bor > can2 and lap2 and bor2:
                        print("\tCÓDIGO || PRODUTO")
                        print("\t  [20] ||[CANETA] = ", can)
                        print("\t  [30] ||[LÁPIS] = ", lap)
                        print("\t  [40] ||[BORRACHA] = ", bor)
                    elif lap and bor and reg > lap2 and bor2 and reg2:
                        print("\tCÓDIGO || PRODUTO")
                        print("\t  [30] ||[LÁPIS] = ", lap)
                        print("\t  [40] ||[BORRACHA] = ", bor)
                        print("\t  [50] ||[RÉGUA] = ", reg)
                    elif cad and can and lap and bor > cad2 and can2 and lap2 and bor2:
                        print("\tCÓDIGO || PRODUTO")
                        print("\t  [10] ||[CADERNO] = ", cad)
                        print("\t  [20] ||[CANETA] = ", can)
                        print("\t  [30] ||[LÁPIS] = ", lap)
                        print("\t  [40] ||[BORRACHA] = ", bor)
                    elif can and lap and bor and reg > can2 and lap2 and bor2 and reg2:
                        print("\tCÓDIGO || PRODUTO")
                        print("\t  [20] ||[CANETA] = ", can)
                        print("\t  [30] ||[LÁPIS] = ", lap)
                        print("\t  [40] ||[BORRACHA] = ", bor)
                        print("\t  [50] ||[RÉGUA] = ", reg)
            else:
                print("\nNÃO HOUVE ENTRADA!\n")
        elif escolha == 2:                                        #OPÇÃO [SAÍDA] DO SUBMENU RELATÓRIOS.
            if contSaida < contEntrada :
                print("\tCÓDIGO || PRODUTO\n")
                print("\t  [10] ||[CADERNO] = ", cad)
                print("\t  [20] ||[CANETA] = ", can)
                print("\t  [30] ||[LÁPIS] = ", lap)
                print("\t  [40] ||[BORRACHA] = ", bor)
                print("\t  [50] ||[RÉGUA] = ", reg)
            else:
                print("\nNÃO HOUVE SAÍDAS.")
        elif escolha == 3:                                         #OPÇÃO [VOLTAR] DO SUBMENU RELATÓRIOS.
            breakpoint
        else:            
            print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE!\n")
    elif opcao == 'x' or opcao == 'X':                                        #OPÇÃO [SAIR] DO MENU PRINCIPAL.
        print("\nPROGRAMA ENCERRADO!\n")
        break
    else:
        print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE!\n")