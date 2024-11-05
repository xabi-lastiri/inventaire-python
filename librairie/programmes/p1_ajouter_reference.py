from librairie.fonctions import f0_valeur_saisie_vide, f1_reference_existe, f2_verifier_valeur_entiere_positive


def p1_ajouter_reference(inv):
    while True:
        reference = input("Saisissez la référence à ajouter dans l'inventaire (pour annuler, laissez vide) \n")
        if f0_valeur_saisie_vide(reference):
            return
        if not(f1_reference_existe(reference,inv)):
            break
        else:
            print("La référence existe déjà")
    while True:
        n = input(f"Confirmez-vous ? (o/n) \n")
        if n == "o":
            break
        if n == "n":
            return
        else:
            print("Veuillez saisir à nouveau votre réponse.")
    while True:
        try:
            stock_initial = input(f"Saisissez le stock initial : ")
            stock_initial = int(stock_initial)
            f0_valeur_saisie_vide(stock_initial)
            if f2_verifier_valeur_entiere_positive(stock_initial):
                break
        except ValueError:
            print("Valeur incorrecte.")
    while True:
        n = input(f"Confirmez-vous ? (o/n) \n")
        if n == "o":
            break
        if n == "n":
            return
        else:
            print("Veuillez saisir à nouveau votre réponse.")
    inv[reference] = stock_initial
    print(f"Vous venez d'ajouter {reference} avec {stock_initial} unité(s) en stock initial.")