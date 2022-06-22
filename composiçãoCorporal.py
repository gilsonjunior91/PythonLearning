#cadastro de bioimpedância

print("\t\tSEJA BEM VINDO AO SISTEMA DE IMPEDÂNCIA")

print("\n*******CADASTRO*******\n")

print("Para iniciar precisamos dos seguintes dados!\n")

nome = input("Digite o seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso: "))
sexo = input("Digite o sexo [M]-MASCULINO OU [F]-FEMININO: ")

imc = peso / altura ** 2

if imc < 20:
   print("\nESTÁ ABAIXO DO PESO! ")
elif imc == 20 or imc <= 25:
   print("\nO PESO ESTÁ NORMAL! ")
elif imc == 26 or imc <= 30:
   print("\nESTÁ SOBREPESO!")
elif imc == 31 or imc <= 40:
   print("\nESTÁ OBESO!")
else:
   print("\nESTÁ OBESO MÓRBIDO!")


print("\nSeu IMC(Índice de Massa Corpórea): ", imc)


massaGorda = float(input("\nDigite sua Massa Gorda em %: "))
massaMagra = float(input("\nDigite sua Massa Magra em %: "))

Mg = massaGorda / 100
Mm = massaMagra / 100
if Mg > 0.0 or Mg <=1.0 and Mm > 0.0 or Mm <= 1.0:
    indiceGorda = peso * (massaGorda/100)
    indiceMagra = peso - indiceGorda
    gorduraCorporal = massaGorda / peso * 100
else:
    print("Valores fora dos padrões aceitavéis.")

print("\nA MASSA MAGRA É ", indiceMagra)
print("\nA MASSA GORDA É ", indiceGorda)
#print("\nO PESO IDEAL DEVE SER ", pesoIdeal)
