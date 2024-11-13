from library import *


def ajouter_reference(inventaire, registre, utilisateur):

    while True:

        # Étape 1 : Entrer le nom de la référence
        while True:
            reference = input("Saisissez la référence à ajouter dans l'inventaire.\nPour annuler, laissez vide.\n\n")
            if verifier_valeur_saisie_vide(reference):
                return
            elif verifier_reference_existe(reference,inventaire):
                print("\nLa référence existe déjà")
            else:
                break

        # Étape 2 : Choisir le stock initial pour la référence à entrer
        while True:
            stock_initial = input(f"\nSaisissez le stock initial : \n\n")
            if not verifier_valeur_entiere_positive(stock_initial):
                print("\nValeur incorrecte.")
            else:
                break

        # Étape 3 : Confirmer l'opération
        while True:
            n = input(f"\nAjouter {reference} avec {stock_initial} unité(s) en stock initial.\nConfirmez-vous ? (o/n) \n\n").lower()
            if n == "n":
                break
            elif n == "o":
                inventaire[reference] = int(stock_initial)
                registre.append(f"{utilisateur} : CRÉATION de {reference} avec {stock_initial} unité(s) en stock initial")
                print(f"\nVous venez d'ajouter {reference} avec {stock_initial} unité(s) en stock initial.\n")
                break
            else:
                print("\nVeuillez saisir à nouveau votre réponse.")

        # Étape 4 : Réaliser une nouvelle opération ou revenir au menu
        while True:
            continuer = input("\nVoulez-vous ajouter une autre référence ? (o/n)\n\n").lower()
            if continuer == "n":
                return
            if continuer == "o":
                break
            else:
                print("\nVeuillez saisir à nouveau votre réponse.")