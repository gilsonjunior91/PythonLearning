cinema = ('Sony Picture','Walt Disney','Universal Picture','Warner')
if 'Disney' in cinema:
   print(cinema.index('Disney'))
else:
   print("Disney não está na tupla.")

print(cinema.index('Warner')) # mostra a posição que se encontra a string

# Ocasiona em erro porque está incompleto print(cinema.index("Disney"))