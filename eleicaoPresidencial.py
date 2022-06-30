
codigo = 1
candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
votoNulo = 0
votoBranco = 0
ganhador = 0
cont = 0 
nome = 0
while codigo != 0:

    print("\n\t-------ELEIÇÃO PRESIDENCIAL-------\n")
    print("[1]-CANDIDATO 1\n[2]-CANDIDATO 2\n[3]-CANDIDATO 3\n[4]-CANDIDATO 4")
    print("[5]-VOTO NULO\n[6]-VOTO BRANCO\n[0]-SAIR\n")
    codigo = int(input("ESCOLHA O CANDIDATO: "))
    if codigo == 0:
       print("\nVOTAÇÃO ENCERRADA!!!\n")
       break
    elif codigo == 1:
         candidato1 = candidato1 + 1
         print("\n\t\tCOMPUTADO!")
         cont = cont + 1
    elif codigo == 2:
         candidato2 = candidato2 + 1
         print("\n\t\tCOMPUTADO!")
         cont = cont + 1
    elif codigo == 3:
         candidato3 = candidato3 + 1
         print("\n\t\tCOMPUTADO!")
         cont = cont + 1
    elif codigo == 4:
         candidato4 = candidato4 + 1
         print("\n\t\tCOMPUTADO!")
         cont = cont + 1
    elif codigo == 5:
         votoNulo = votoNulo + 1
         print("\n\t\tCOMPUTADO!")
         cont = cont + 1
    elif codigo == 6:
         votoBranco = votoBranco + 1
         print("\n\t\tCOMPUTADO!")
         cont = cont + 1
    else:
         print("\nESSE CÓDIGO NÃO CORRESPONDE AOS CANDIDATOS!\n TENTE NOVAMENTE!")

if candidato1 > candidato2:
     ganhador = candidato1
     nome = 'CANDIDATO 1'
elif candidato2 > candidato1:
     ganhador = candidato2
     nome = 'CANDIDATO 2'
elif candidato3 > candidato4:
     ganhador = candidato3
     nome = 'CANDIDATO 3'
elif candidato4 > candidato3:
     ganhador = candidato4
     nome = 'CANDIDATO 4'

print("\nO RESULTADO DAS ELEIÇÕES FORAM AS SEGUINTES:")

print("\n O",nome, " GANHADOR OBTEVE ", ganhador," VOTOS.\n")
print("\n TOTAL DE VOTOS: ", cont)

print("\n VOTOS PARA O CANDIDATO 1: ", candidato1)
print("\n VOTOS PARA O CANDIDATO 2: ", candidato2)
print("\n VOTOS PARA O CANDIDATO 3: ", candidato3)
print("\n VOTOS PARA O CANDIDATO 4: ", candidato4)

print("\n VOTOS BRANCOS: ", votoBranco)
print("\n VOTOS NULOS: ", votoNulo)




