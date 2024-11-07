def p5_afficher_stock(inv):
    while True:
        for reference, quantite in inv.items():
            print(f"{reference} : {quantite} unité(s) en stock.")
        sortir = input("\nPour revenir au menu, saisissez m : ")
        if sortir == "m":
            break