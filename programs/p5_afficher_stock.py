def p5_afficher_stock(inv):
    for reference, quantite in inv.items():
        print(f"{reference} : {quantite} unité(s) en stock.\n")