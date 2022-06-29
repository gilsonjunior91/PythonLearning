
alturas = 0
alturaBaixo = 1000
alturaAlta = 0
pesos = 0
cont = 0
codigo = 1
pesoGordo = 1000
pesoMagro = 0
codAlto = 0
codBaixo = 0
mediaAlturas = 0
mediaPesos = 0
print("\n\t------- SENSO ACADEMIA FELIZ ------- \n")
while codigo != 0:
    codigo = int(input("\n\nDIGITE O SEU CÓDIGO: "))
    if codigo == 0:
        print("\nPROGRAMA ENCERRADO.\n")
    else:
        altura = float(input("DIGITE SUA ALTURA: "))
        alturas = alturas + altura
        peso = float(input("DIGITE SEU PESO: "))
        pesos = pesos + peso
        cont = cont + 1
        if altura < alturaBaixo:
            alturaBaixo = altura
            codBaixo = codigo
        else:
            alturaAlta = altura
            codAlto = codigo
        
        if peso < pesoGordo:
           pesoGordo = peso
        else:
           pesoMagro = peso

mediaPesos = (pesos / cont)
mediaAlturas = (alturas / cont)

print("\n A MEDIA DOS PESOS É ", mediaPesos)
print("\n A MEDIA DAS ALTURAS É ", mediaAlturas)
print("\n CODIGO DO CLIENTE MAIS ALTO: ", codAlto)
print("\n MAIOR ALTURA: ", alturaAlta)
print("\n CODIGO DO CLIENTE MAIS BAIXO: ", codBaixo)
print("\n MENOR ALTURA: ",alturaBaixo)
print("\n MAIOR PESO: ", pesoGordo)
print("\n MENOR PESO: ", pesoMagro)