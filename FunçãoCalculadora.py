opcao = 0
soma = 0
numero = 0
num = 0
subtracao = 0
multiplicacao = 0
divisao = 0

def resultadoSoma (numero,num):
   return numero + num

def resultadoSub(numero, num):
    return numero - num

def resultadoMult(numero, num):
    return numero * num

def resultadoDiv(numero,num):
    return numero / num

numero = int(input("Digite um numero: "))
num = int(input("\nDigite outro numero: "))

while(opcao != '5'):
    
    print(" ESCOLHA UMA OPERAÇÃO ABAIXO \n")
    print(" [1]-SOMA\n [2]-SUBTRACAO\n [3]-MULTIPLICACAO\n [4]-DIVISÃO\n [5]-SAIR\n")
    opcao = input("Sua opção: ")
    if(opcao == '1'):
        soma = resultadoSoma(numero,num)
        print("A soma dos numeros foram ", soma)
        
    elif(opcao == '2'):
        subtracao = resultadoSub(numero,num)
        print("A subtração dos numeros foram ", subtracao)
        
    elif(opcao == '3'):
        multiplicacao = resultadoMult(numero,num)
        print("A subtração dos numeros foram ", multiplicacao)

    elif(opcao == '4'):
        divisao = resultadoDiv(numero,num)
        print("A subtração dos numeros foram ", divisao)

    elif(opcao == '5'):
        print("Até mais !\n")
