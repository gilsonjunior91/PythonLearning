
print("\n\tCONTA VIRTUAL \n")

usuario = 1
senha = 1

while usuario == senha:
    usuario = input("Nome de usuário: ")
    senha = input("Senha: ")
    if usuario == senha:
        print("\nINFORMAÇÕES INVÁLIDAS, TENTE NOVAMENTE!\n")
    else:
        print("\nINFORMAÇÕES SALVAS!\n")

