def m5_afficher_stock(inventaire):
    while True: # pour arrêter le programme que lorsque l'utilisateur le décide
        print("\n")
        for reference, quantite in inventaire.items():
            print(f"{reference} : {quantite} unité(s) en stock.")
        sortir = input("\nPour revenir au menu, saisissez m : ").lower()
        if sortir == "m":
            break