def m5_afficher_stock(inventaire):

    while True:
        print("\n")
        for reference, quantite in inventaire.items():
            print(f"{reference} : {quantite} unité(s) en stock.")
        sortir = input("\nPour revenir au menu, saisissez m : ").lower()
        if sortir == "m":
            break