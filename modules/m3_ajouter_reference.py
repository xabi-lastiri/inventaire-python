from library import *

def m3_ajouter_reference(inventaire, registre, utilisateur):
    while True:
        # pour arrêter le programme que lorsque l'utilisateur le décide
        while True:
            # demander à l'utilisateur de saisir la référence à ajouter dans l'inventaire
            # vérifier que la référence à ajouter n'existe PAS dans l'inventaire
            reference = input("Saisissez la référence à ajouter dans l'inventaire.\nPour annuler, laissez vide.\n\n")
            if f0_valeur_saisie_vide(reference):
                return
            if not(f1_reference_existe(reference,inventaire)):
                break
            else:
                print("\nLa référence existe déjà")
        while True:
            # demander à l'utilisateur de saisir le stock initial pour la référence à entrer dans l'inventaire
            # vérifier que la quantité saisie est cohérente
            try:
                stock_initial = int(input(f"\nSaisissez le stock initial : \n\n"))
                if type(stock_initial) == int and stock_initial >= 0:
                    break
            except ValueError:
                print("\nValeur incorrecte.")
        while True:
            # demander à l'utilisateur de confirmer l'opération ; si oui, ajouter la référence et son stock initial dans l'inventaire
            n = input(f"\nAjouter {reference} avec {stock_initial} unité(s) en stock initial.\nConfirmez-vous ? (o/n) \n\n").lower()
            if n == "o":
                inventaire[reference] = stock_initial
                # enregistrement de l'opération dans le registre
                registre.append(f"{utilisateur} - Création : {reference} avec {stock_initial} unité(s) en stock initial")
                print(f"\nVous venez d'ajouter {reference} avec {stock_initial} unité(s) en stock initial.\n")
                # proposer à l'utilisateur de réaliser une nouvelle opération ou de revenir au menu
                continuer = input("\nVoulez-vous ajouter une autre référence ? (o/n)\n\n").lower()
                if continuer == "n":
                    return
                if continuer == "o":
                    break
                else:
                    return
            if n == "n":
                break
            else:
                print("\nVeuillez saisir à nouveau votre réponse.")