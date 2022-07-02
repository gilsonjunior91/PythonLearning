from operator import index
from textwrap import indent


codigo = []
i = 0
escolha = 1
codigo1 = int(10)
codigo2 = int(20)
codigo3 = int(30)
codigo4 = int(40)
codigo5 = int(50)

prod = 0
opcao = 0
produto = ['caderno','caneta','lapis','borracha','regua']
produto1 = 'caderno'
produto2 = 'caneta'
produto3 = 'lapis'
produto4 = 'borracha'
produto5 = 'regua'

print("\n\t------ CONTROLE DE ESTOQUE ------\n")

while opcao != 'x' or opcao != 'X':
    print("\n ESCOLHA A OPERAÇÃO \n")
    print("[E]- ENTRADA NO ESTOQUE.")
    print("[S]- SAÍDA NO ESTOQUE.")
    print("[R]- RELATÓRIOS.")
    print("[X]- SAIR.")
    opcao = input("SUA ESCOLHA: ")
    if opcao == 'x' or opcao == 'X':
        print("\nPROGRAMA ENCERRADO!\n")
        break
    elif opcao == 'e' or opcao == 'E':
        print("\n\t------ ENTRADA DO ESTOQUE ------\n")
        while escolha != 2:
            if escolha == 1:
                codigo = (int(input("\nENTRE COM O CÓDIGO DO PRODUTO: ")))
                produto = (input("\nDIGITE A DESCRIÇÃO DO PRODUTO: "))
                print("\n\tINSERIDO COM SUCESSO.\n")
                print("\nDESEJA INSERIR MAIS PRODUTOS ?")
                escolha = int(input(" [1]- SIM\n [2]- NÃO\n SUA ESCOLHA: "))
            elif escolha == 2:
                break
            else:
                print("\nOPÇÃO INCORRETA.\n")
            
    elif opcao =='s' or opcao == 'S':
        print("\n\t------ SAÍDA DO ESTOQUE ------\n")
        prod = int(input("\nDIGITE O CÓDIGO: "))
        #if prod == codigo:
    elif opcao == 'r' or opcao == 'R':
        print("\n\t------ RELATÓRIOS ------\n")
        print(" [1]-ENTRADAS\n")
        print(" [2]-SAÍDAS\n")
        print(" [3]-VOLTAR\n")
        print("LISTA: ", len(codigo))
        print("LISTA 2: ", len(produto))

        print("LISTA index: ", index(codigo))
        print("LISTA 2: ", index(produto))

        escolha = int(input("DIGITE SUA A OPÇÃO DESEJADA: "))
        if escolha == 1:
            while i > (len(codigo)) and i > (len(produto)):
                print("CÓDIGO [ ",i,"]- ", codigo[i],"\n")
                print("PRODUTO [ ",i,"]- ", produto[i],"\n")
        elif escolha == 2:
            print("CÓDIGO [ ",i,"]- ", codigo,"\n")
            print("PRODUTO [ ",i,"]- ", produto,"\n")
        elif escolha == 3:
            break
        else:
            print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE!\n")
    else:
        print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE!\n")





##produto.upper()