from library.fonctions import f0_valeur_saisie_vide, f1_reference_existe, f2_verifier_valeur_entiere_positive


def p3_ajouter_reference(inv):
    while True:
        while True:
            reference = input("Saisissez la référence à ajouter dans l'inventaire.\nPour annuler, laissez vide.\n\n")
            if f0_valeur_saisie_vide(reference):
                return
            if not(f1_reference_existe(reference,inv)):
                break
            else:
                print("\nLa référence existe déjà")
        while True:
            n = input(f"\nAjouter {reference}.\nConfirmez-vous ? (o/n) \n\n").lower()
            if n == "o":
                break
            if n == "n":
                return
            else:
                print("\nValeur incorrecte. Veuillez saisir à nouveau votre réponse.")
        while True:
            try:
                stock_initial = input(f"\nSaisissez le stock initial : \n\n")
                stock_initial = int(stock_initial)
                f0_valeur_saisie_vide(stock_initial)
                if f2_verifier_valeur_entiere_positive(stock_initial):
                    break
            except ValueError:
                print("\nValeur incorrecte.")
        while True:
            n = input(f"\nStock initial {stock_initial} pour {reference}. Confirmez-vous ? (o/n) \n\n").lower()
            if n == "o":
                break
            if n == "n":
                return
            else:
                print("\nVeuillez saisir à nouveau votre réponse.")
        inv[reference] = stock_initial
        print(f"\nVous venez d'ajouter {reference} avec {stock_initial} unité(s) en stock initial.\n")
        continuer = input("\nVoulez-vous ajouter une autre référence ? (o/n)\n\n").lower()
        if continuer == "n":
            break
        if continuer == "o":
            continue
        else:
            break