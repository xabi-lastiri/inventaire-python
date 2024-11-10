from library.fonctions import f0_valeur_saisie_vide, f1_reference_existe, f2_verifier_valeur_entiere_positive, f3_afficher_liste_references


def p1_vendre(inv):
    while True:
        # pour arrêter le programme que lorsque l'utilisateur le décide
        while True:
            # demander à l'utilisateur de saisir la référence à vendre
            # vérifier que la référence à vendre existe dans l'inventaire
            reference = input(f"\nSaisissez la référence à vendre ({f3_afficher_liste_references(inv)})\nPour annuler, laissez vide.\n\n")
            if f0_valeur_saisie_vide(reference):
                return
            if f1_reference_existe(reference, inv):
                break
            else:
                print(f"\n{reference} n'existe pas dans l'inventaire.")
        while True:
            # demander à l'utilisateur de saisir la quantité à vendre
            # vérifier que la quantité à vendre soit (1) cohérente et (2) possible compte tenu du stock diponible dans l'inventaire au moment de l'opération
            try:
                quantite_a_vendre = input(f"\nIl reste {inv[reference]} unité(s) en stock pour le produit {reference}.\nSaisissez la quantité à vendre : \n\n")
                quantite_a_vendre = int(quantite_a_vendre)
                if f2_verifier_valeur_entiere_positive(quantite_a_vendre) and quantite_a_vendre <= inv[reference]:
                    break
                print("\nLe stock est insuffisant.")
            except ValueError:
                print("\nValeur incorrecte.")
        while True:
            # demander à l'utilisateur de confirmer l'opération ; si oui, retirer de l'inventaire la quantité pour la référence donnée
            n = input(f"\nVente de {quantite_a_vendre} unité(s) de {reference}.\nConfirmez-vous l'opération ? (o/n)\n\n").lower()
            if n == "o":
                inv[reference] -= quantite_a_vendre
                print(
                    f"\nVous venez de vendre {quantite_a_vendre} unité(s) de {reference}. Il reste maintenant {inv[reference]} unité(s) en stock")
                # proposer à l'utilisateur de réaliser une nouvelle opération ou de revenir au menu
                continuer = input("\nVoulez-vous vendre autre chose ? (o/n)\n\n").lower()
                if continuer == "n":
                    return
                if continuer == "o":
                    break
                else:
                    return
            if n == "n":
                break
            else:
                print("\nVeuillez saisir à nouveau votre réponse.")