from library import *


def vendre(inventaire, registre, utilisateur):

    while True:

        # Étape 1 : Sélectionner la référence
        while True:
            reference = input(f"\nSaisissez la référence à vendre ({afficher_liste_references(inventaire)}) \nPour annuler, laissez vide.\n\n")
            if valeur_saisie_vide(reference):
                return
            if not reference_existe(reference, inventaire):
                print(f"\n{reference} n'existe pas dans l'inventaire.")
            elif inventaire[reference] == 0:
                print(f"Il n'y a plus de {reference}(s) en stock.")
            else:
                break

        # Étape 2 : Choisir la quantité à retirer de l'inventaire pour la référence donnée
        while True:
            quantite_a_vendre = input(f"\nIl reste {inventaire[reference]} unité(s) en stock pour le produit {reference}.\nSaisissez la quantité à vendre : \n\n")
            if not verifier_valeur_entiere_positive(quantite_a_vendre):
                print("\nValeur incorrecte.")
            elif int(quantite_a_vendre) > inventaire[reference]:
                print("\nLe stock est insuffisant.")
            else:
                break

        # Étape 3 : Confirmer l'opération
        while True:
            n = input(f"\nVente de {quantite_a_vendre} unité(s) de {reference}.\nConfirmez-vous l'opération ? (o/n)\n\n").lower()
            if n == "n":
                break
            elif n == "o":
                quantite_a_vendre = int(quantite_a_vendre)
                inventaire[reference] -= quantite_a_vendre
                registre.append(f"{utilisateur} : VENTE de {quantite_a_vendre} unité(s) de {reference}")
                print(f"\nVous venez de vendre {quantite_a_vendre} unité(s) de {reference}. Il reste maintenant {inventaire[reference]} unité(s) en stock")
                break
            else:
                print("\nVeuillez saisir à nouveau votre réponse.")

        # Étape 4 : Réaliser une nouvelle opération ou revenir au menu
        while True:
            continuer = input("\nVoulez-vous vendre autre chose ? (o/n)\n\n").lower()
            if continuer == "o":
                break
            elif continuer == "n":
                return
            else:
                print("Veuillez saisir à nouveau votre réponse.")