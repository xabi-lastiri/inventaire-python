def afficher_registre(registre):

    while True:
        print("\n")
        for operation in registre:
            print(f"OPE{registre.index(operation)} - {operation}")
        sortir = input("\nPour revenir au menu, saisissez m : ").lower()
        if sortir == "m":
            break