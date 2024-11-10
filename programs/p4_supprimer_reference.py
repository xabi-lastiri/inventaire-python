from library.fonctions import f0_valeur_saisie_vide, f1_reference_existe, f3_afficher_liste_references


def p4_supprimer_reference(inv):
    while True:
        # pour arrêter le programme que lorsque l'utilisateur le décide
        while True:
            # demander à l'utilisateur de saisir la référence à supprimer
            # vérifier que la référence à supprimer existe dans l'inventaire
            reference = input(f"Saisissez la référence à supprimer de l'inventaire : ({f3_afficher_liste_references(inv)})\nPour annuler, laissez vide.\n\n")
            if f0_valeur_saisie_vide(reference):
                return
            if f1_reference_existe(reference,inv):
                break
            else:
                print("\nLa référence n'existe pas.")
        while True:
            # demander à l'utilisateur de confirmer l'opération ; si oui, supprimer de l'inventaire la référence et son stock associé
            n = input(f"\nSupprimer {reference}.\nConfirmez-vous ? (o/n) \n\n").lower()
            if n == "o":
                break
            if n == "n":
                return
            else:
                print("\nVeuillez saisir à nouveau votre réponse.")
        del inv[reference]
        print(f"\nNous vous confirmons la suppression de la référence {reference}")
        # proposer à l'utilisateur de réaliser une nouvelle opération ou de revenir au menu
        continuer = input("\nVoulez-vous supprimer une autre référence ? (o/n)\n\n").lower()
        if continuer == "n":
            break
        if continuer == "o":
            continue
        else:
            break