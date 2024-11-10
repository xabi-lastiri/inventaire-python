def m6_afficher_registre(registre):
    while True:
        # pour arrêter le programme que lorsque l'utilisateur le décide
        print("\n")
        for operation in registre:
            print(f"OPE{registre.index(operation)}. {operation}")
        sortir = input("\nPour revenir au menu, saisissez m : ").lower()
        if sortir == "m":
            break