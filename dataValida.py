print("Digite a data no formato: dd/mm/aaaa")

dia = [10]
#data = ['dd','/','mm','/','aaaa']
dia = (input("Digite: "))

if dia[0] == data[0] and dia[2] == data[1]:
    if dia[3] == data[2] and dia[4] == data[3]:
        print("É uma data válida.", dia)
    else:
        print("Não é uma data válida.")
else:
    print("Data Inválida.")