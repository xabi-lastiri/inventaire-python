from library import *

def m1_vendre(inventaire, registre, utilisateur):
    while True: # pour arrêter le programme que lorsque l'utilisateur le décide
        while True:
            # demander à l'utilisateur de saisir la référence à vendre
            reference = input(f"\nSaisissez la référence à vendre ({f3_afficher_liste_references(inventaire)})\nPour annuler, laissez vide.\n\n")
            # vérifier si l'utilisateur souhaite annuler l'opération
            if f0_valeur_saisie_vide(reference):
                return
            # vérifier que la référence à vendre existe dans l'inventaire et que le stock correspondant n'est pas nul
            if f1_reference_existe(reference, inventaire):
                if inventaire[reference] == 0:
                    print(f"Il n'y a plus de {reference} en stock.")
                else:
                    break
            else:
                print(f"\n{reference} n'existe pas dans l'inventaire.")
        while True:
            try:
                # demander à l'utilisateur de saisir la quantité à vendre
                quantite_a_vendre = int(input(f"\nIl reste {inventaire[reference]} unité(s) en stock pour le produit {reference}.\nSaisissez la quantité à vendre : \n\n"))
                # vérifier que la quantité à vendre soit (1) cohérente et (2) possible compte tenu du stock disponible dans l'inventaire au moment de l'opération
                if f2_verifier_valeur_entiere_positive(quantite_a_vendre) and quantite_a_vendre <= inventaire[reference]:
                    break
                print("\nLe stock est insuffisant.")
            except ValueError:
                print("\nValeur incorrecte.")
        while True:
            # demander à l'utilisateur de confirmer l'opération ; si oui, retirer de l'inventaire la quantité pour la référence donnée
            n = input(f"\nVente de {quantite_a_vendre} unité(s) de {reference}.\nConfirmez-vous l'opération ? (o/n)\n\n").lower()
            if n == "n":
                break
            if n == "o":
                inventaire[reference] -= quantite_a_vendre
                # enregistrer l'opération dans le registre
                registre.append(f"{utilisateur} : VENTE de {quantite_a_vendre} unité(s) de {reference}")
                print(
                    f"\nVous venez de vendre {quantite_a_vendre} unité(s) de {reference}. Il reste maintenant {inventaire[reference]} unité(s) en stock")
                # proposer à l'utilisateur de réaliser une nouvelle opération ou de revenir au menu
                continuer = input("\nVoulez-vous vendre autre chose ? (o/n)\n\n").lower()
                if continuer == "n":
                    return
                if continuer == "o":
                    break
                else:
                    return
            else:
                print("\nVeuillez saisir à nouveau votre réponse.")