def p5_afficher_stock(inv):
    while True:
        # pour arrêter le programme que lorsque l'utilisateur le décide
        print("\n")
        for reference, quantite in inv.items():
            print(f"{reference} : {quantite} unité(s) en stock.")
        sortir = input("\nPour revenir au menu, saisissez m : ").lower()
        if sortir == "m":
            break