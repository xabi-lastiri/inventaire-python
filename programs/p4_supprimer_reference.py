from library.fonctions import f0_valeur_saisie_vide, f1_reference_existe, f3_afficher_liste_references


def p4_supprimer_reference(inv):
    while True:
        while True:
            reference = input(f"Saisissez la référence à supprimer de l'inventaire : ({f3_afficher_liste_references(inv)})\nPour annuler, laissez vide.\n\n")
            if f0_valeur_saisie_vide(reference):
                return
            if f1_reference_existe(reference,inv):
                break
            else:
                print("\nLa référence n'existe pas.")
        while True:
            n = input(f"\nSupprimer {reference}.\nConfirmez-vous ? (o/n) \n\n")
            if n == "o":
                break
            if n == "n":
                return
            else:
                print("\nVeuillez saisir à nouveau votre réponse.")
        del inv[reference]
        print(f"\nNous vous confirmons la suppression de la référence {reference}")
        continuer = input("\nVoulez-vous supprimer une autre référence ? (o/n)\n\n")
        if continuer == "n":
            break
        if continuer == "o":
            continue
        else:
            break