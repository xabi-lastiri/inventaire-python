from library.fonctions import f0_valeur_saisie_vide, f1_reference_existe, f2_verifier_valeur_entiere_positive, f3_afficher_liste_references


def p2_ajouter_stock(inv):
    while True:
        while True:
            reference = input(f"\nSaisissez la référence à stocker : ({f3_afficher_liste_references(inv)}) \nPour annuler, laissez vide.\n\n")
            if f0_valeur_saisie_vide(reference):
                return
            if f1_reference_existe(reference, inv): #à debuger
                break
            else:
                print("\nLa référence n'existe pas.")
        while True:
            try:
                quantite_a_entrer = input(f"\nSaisissez la quantité à entrer : \n\n")
                quantite_a_entrer = int(quantite_a_entrer)
                if f2_verifier_valeur_entiere_positive(quantite_a_entrer):
                    break
            except ValueError:
                print("\nValeur incorrecte.")
        while True:
            n = input(f"\nAjout de {quantite_a_entrer} unité(s) pour {reference}.\nConfirmez-vous ? (o/n) \n\n")
            if n == "o":
                break
            if n == "n":
                return
            else:
                print("\nVeuillez saisir à nouveau votre réponse.")
        inv[reference] += quantite_a_entrer
        print(
            f"\nVous venez d'ajouter {quantite_a_entrer} unité(s) de {reference}.\nIl y a maintenant {inv[reference]} unité(s) en stock.\n")
        continuer = input("\nVoulez-vous ajouter autre chose ? (o/n)\n\n")
        if continuer == "n":
            break
        if continuer == "o":
            continue
        else:
            break