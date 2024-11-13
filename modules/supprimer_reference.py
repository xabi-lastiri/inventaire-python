from library.fonctions import *


def supprimer_reference(inventaire, registre, utilisateur):

    while True:

        # Étape 1 : Entrer le nom de la référence
        while True:
            reference = input(f"Saisissez la référence à supprimer de l'inventaire : ({afficher_liste_references(inventaire)})\nPour annuler, laissez vide.\n\n")
            if verifier_valeur_saisie_vide(reference):
                return
            if verifier_reference_existe(reference, inventaire):
                break

        # Étape 2 : Confirmer l'opération
        while True:
            print(f"\nSupprimer {reference}.\nConfirmez-vous ? (o/n) \n")
            if confirmer():
                del inventaire[reference]
                registre.append(f"{utilisateur} : SUPPRESSION de {reference}")
                print(f"\nNous vous confirmons la suppression de la référence {reference}")
                break
            else:
                break

        # Étape 3 : Réaliser une nouvelle opération ou revenir au menu
        if not confirmer():
            break