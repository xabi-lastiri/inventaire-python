from library import *

def m4_supprimer_reference(inventaire, registre, utilisateur):
    while True: # pour arrêter le programme que lorsque l'utilisateur le décide
        while True:
            # demander à l'utilisateur de saisir la référence à supprimer
            reference = input(f"Saisissez la référence à supprimer de l'inventaire : ({f3_afficher_liste_references(inventaire)})\nPour annuler, laissez vide.\n\n")
            # vérifier si l'utilisateur souhaite annuler l'opération
            if f0_valeur_saisie_vide(reference):
                return
            # vérifier que la référence à supprimer existe dans l'inventaire
            if f1_reference_existe(reference,inventaire):
                break
            else:
                print("\nLa référence n'existe pas.")
        while True:
            # demander à l'utilisateur de confirmer l'opération ; si oui, supprimer de l'inventaire la référence et son stock associé
            n = input(f"\nSupprimer {reference}.\nConfirmez-vous ? (o/n) \n\n").lower()
            if n == "n":
                break
            if n == "o":
                del inventaire[reference]
                # enregistrer l'opération dans le registre
                registre.append(f"{utilisateur} : SUPPRESSION de {reference}")
                print(f"\nNous vous confirmons la suppression de la référence {reference}")
                # proposer à l'utilisateur de réaliser une nouvelle opération ou de revenir au menu
                continuer = input("\nVoulez-vous supprimer une autre référence ? (o/n)\n\n").lower()
                if continuer == "n":
                    return
                if continuer == "o":
                    break
                else:
                    return
            else:
                print("\nVeuillez saisir à nouveau votre réponse.")
