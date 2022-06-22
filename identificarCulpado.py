print("\n\tQUESTIONÁRIO DE IDENTIFICAÇÃO!")

resultado = 0


telefone = input("TELEFONOU PARA A VÍTIMA? ")
local = input("\nESTEVE NO LOCAL DO CRIME? ")
moradia = input("\n MORA PERTO DA VÍTIMA? ")
deve = input("\nDEVIA PARA A VÍTIMA? ")
trabalha = input("\nJÁ TRABALHOU COM A VÍTIMA? ")

if telefone == 'SIM' or telefone == 'sim':
    resultado = resultado + 1
    if local == 'SIM' or local == 'sim':
        resultado = resultado + 1
        if moradia == 'SIM' or moradia == 'sim':
            resultado = resultado + 1
            if deve == 'SIM' or deve == 'sim':
                resultado = resultado + 1
                if trabalha == 'SIM' or trabalha == 'sim':
                    resultado = resultado + 1
                else:
                    print("\nINOCENTE!")
else:
    print("\nINOCENTE!")
if resultado == 2:
    print("\nSUSPEITA")
elif resultado == 3 or resultado == 4:
    print("\nCÚMPLICE!")
elif resultado == 5:
    print("\nASSASSINO!")
else:
    print("\nINOCENTE!")
