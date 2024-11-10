def m6_afficher_registre(registre):
    while True:
        for operation in registre:
            print(f"OPE{registre.index(operation)}. {operation}")
        sortir = input("\nPour revenir au menu, saisissez m : ").lower()
        if sortir == "m":
            break