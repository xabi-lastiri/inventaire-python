from library.fonctions import *


def vendre(inventaire, registre, utilisateur):

    while True:

        # Étape 1 : Sélectionner la référence
        while True:
            reference = input(f"\nSaisissez la référence à vendre "
                              f"({afficher_liste_references(inventaire)}) "
                              f"\nPour annuler, laissez vide.\n\n")
            if verifier_valeur_saisie_vide(reference):
                return
            if verifier_reference_existe(reference, inventaire):
                break

        # Étape 2 : Choisir la quantité à retirer de l'inventaire pour la référence donnée
        while True:
            quantite_a_vendre = input(f"\nIl reste {inventaire[reference]} unité(s) en stock pour le produit {reference}."
                                      f"\nSaisissez la quantité à vendre : \n\n")
            if (verifier_valeur_entiere_positive(quantite_a_vendre)
            and verifier_stock_suffisant(inventaire, reference, quantite_a_vendre)):
                break

        # Étape 3 : Confirmer l'opération
        while True:
            print(f"\nVente de {quantite_a_vendre} unité(s) de {reference}.\nConfirmez-vous l'opération ? (o/n)\n")
            if not confirmer():
                break
            else:
                quantite_a_vendre = int(quantite_a_vendre)
                inventaire[reference] -= quantite_a_vendre
                registre.append(f"{utilisateur} : VENTE de {quantite_a_vendre} unité(s) de {reference}")
                print(f"\nVous venez de vendre {quantite_a_vendre} unité(s) de {reference}. "
                      f"Il reste maintenant {inventaire[reference]} unité(s) en stock")
                break

        # Étape 4 : Réaliser une nouvelle opération ou revenir au menu
        print("Voulez-vous réaliser une nouvelle opération ? (o/n) :\n")
        if not confirmer():
            break