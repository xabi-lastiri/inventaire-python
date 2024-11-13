from library import *


def ajouter_stock(inventaire, registre, utilisateur):

    while True:

        # Étape 1 : Sélectionner la référence
        while True:
            reference = input(f"\nSaisissez la référence à stocker : ({afficher_liste_references(inventaire)}) \nPour annuler, laissez vide.\n\n")
            if verifier_valeur_saisie_vide(reference):
                return
            elif not verifier_reference_existe(reference, inventaire):
                print("\nLa référence n'existe pas.")
            else:
                break

        # Étape 2 : Choisir la quantité à ajouter dans l'inventaire pour la référence donnée
        while True:
            quantite_a_entrer = input(f"\nSaisissez la quantité à entrer : \n\n")
            if not verifier_valeur_entiere_positive(quantite_a_entrer):
                print("\nValeur incorrecte.")
            else:
                break

        # Étape 3 : Confirmer l'opération
        while True:
            n = input(f"\nAjout de {quantite_a_entrer} unité(s) pour {reference}.\nConfirmez-vous ? (o/n) \n\n").lower()
            if n == "n":
                break
            elif n == "o":
                quantite_a_entrer = int(quantite_a_entrer)
                inventaire[reference] += quantite_a_entrer
                registre.append(f"{utilisateur} : AJOUT de {quantite_a_entrer} unité(s) de {reference}")
                print(f"\nVous venez d'ajouter {quantite_a_entrer} unité(s) de {reference}.\nIl y a maintenant {inventaire[reference]} unité(s) en stock.\n")
                break
            else:
                print("\nVeuillez saisir à nouveau votre réponse.")

        # Étape 4 : Réaliser une nouvelle opération ou revenir au menu
        while True:
            continuer = input("\nVoulez-vous ajouter autre chose ? (o/n)\n\n").lower()
            if continuer == "o":
                break
            if continuer == "n":
                return
            else:
                print("Veuillez saisir à nouveau votre réponse")

