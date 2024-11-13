from library import *


def supprimer_reference(inventaire, registre, utilisateur):

    while True:

        # Étape 1 : Entrer le nom de la référence
        while True:
            reference = input(f"Saisissez la référence à supprimer de l'inventaire : ({afficher_liste_references(inventaire)})\nPour annuler, laissez vide.\n\n")
            if valeur_saisie_vide(reference):
                return
            if not reference_existe(reference,inventaire):
                print("\nLa référence n'existe pas.")
            else:
                break

        # Étape 2 : Confirmer l'opération
        while True:
            n = input(f"\nSupprimer {reference}.\nConfirmez-vous ? (o/n) \n\n").lower()
            if n == "n":
                break
            elif n == "o":
                del inventaire[reference]
                registre.append(f"{utilisateur} : SUPPRESSION de {reference}")
                print(f"\nNous vous confirmons la suppression de la référence {reference}")
                break
            else:
                print("\nVeuillez saisir à nouveau votre réponse.")

        # Étape 3 : Réaliser une nouvelle opération ou revenir au menu
        while True:
            continuer = input("\nVoulez-vous supprimer une autre référence ? (o/n)\n\n").lower()
            if continuer == "n":
                return
            if continuer == "o":
                break
            else:
                print("\nVeuillez saisir à nouveau votre réponse.")
