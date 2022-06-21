print("\nQUANTIDADE DE CENTENAS, DEZENAS E UNIDADES\n")

numero = int(input("Digite um número: "))

if numero < 1000:
   unidade = numero % 10
   numero = (numero - unidade) / 10

   dezena = numero % 10
   numero = (numero - dezena) / 10

   centena = numero

   dezena = int(dezena)
   centena = int(centena)

   print(centena, "centena(s),", dezena, "dezena(s) e", unidade, "unidade(s)")
else:
   print("FORA DO INTERVALO PROPOSTO.")