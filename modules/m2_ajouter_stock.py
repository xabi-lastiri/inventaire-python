from library.fonctions import f0_valeur_saisie_vide, f1_reference_existe, f2_verifier_valeur_entiere_positive, f3_afficher_liste_references


def m2_ajouter_stock(inv):
    while True:
        # pour arrêter le programme que lorsque l'utilisateur le décide
        while True:
            # demander à l'utilisateur de saisir la référence à stocker
            # vérifier que la référence à stocker existe dans l'inventaire
            reference = input(f"\nSaisissez la référence à stocker : ({f3_afficher_liste_references(inv)}) \nPour annuler, laissez vide.\n\n")
            if f0_valeur_saisie_vide(reference):
                return
            if f1_reference_existe(reference, inv): #à debuger
                break
            else:
                print("\nLa référence n'existe pas.")
        while True:
            # demander à l'utilisateur de saisir la quantité à stocker
            # vérifier que la quantité à stocker est cohérente
            try:
                quantite_a_entrer = input(f"\nSaisissez la quantité à entrer : \n\n")
                quantite_a_entrer = int(quantite_a_entrer)
                if f2_verifier_valeur_entiere_positive(quantite_a_entrer):
                    break
            except ValueError:
                print("\nValeur incorrecte.")
        while True:
            # demander à l'utilisateur de confirmer l'opération ; si oui, ajouter dans l'inventaire la quantité pour la référence donnée
            n = input(f"\nAjout de {quantite_a_entrer} unité(s) pour {reference}.\nConfirmez-vous ? (o/n) \n\n").lower()
            if n == "o":
                inv[reference] += quantite_a_entrer
                print(
                    f"\nVous venez d'ajouter {quantite_a_entrer} unité(s) de {reference}.\nIl y a maintenant {inv[reference]} unité(s) en stock.\n")
                # proposer à l'utilisateur de réaliser une nouvelle opération ou de revenir au menu
                continuer = input("\nVoulez-vous ajouter autre chose ? (o/n)\n\n").lower()
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
