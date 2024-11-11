from library import *

def m2_ajouter_stock(inventaire, registre, utilisateur):
    while True: # pour arrêter le programme que lorsque l'utilisateur le décide
        while True:
            # demander à l'utilisateur de saisir la référence à stocker
            reference = input(f"\nSaisissez la référence à stocker : ({f3_afficher_liste_references(inventaire)}) \nPour annuler, laissez vide.\n\n")
            # vérifier si l'utilisateur souhaite annuler l'opération
            if f0_valeur_saisie_vide(reference):
                return
            # vérifier que la référence à stocker existe dans l'inventaire
            if f1_reference_existe(reference, inventaire):
                break
            else:
                print("\nLa référence n'existe pas.")
        while True:
            try:
                # demander à l'utilisateur de saisir la quantité à stocker
                quantite_a_entrer = int(input(f"\nSaisissez la quantité à entrer : \n\n"))
                # vérifier que la quantité à stocker est cohérente
                if f2_verifier_valeur_entiere_positive(quantite_a_entrer):
                    break
            except ValueError:
                print("\nValeur incorrecte.")
        while True:
            # demander à l'utilisateur de confirmer l'opération ; si oui, ajouter dans l'inventaire la quantité pour la référence donnée
            n = input(f"\nAjout de {quantite_a_entrer} unité(s) pour {reference}.\nConfirmez-vous ? (o/n) \n\n").lower()
            if n == "n":
                break
            if n == "o":
                inventaire[reference] += quantite_a_entrer
                # enregistrer l'opération dans le registre
                registre.append(f"{utilisateur} : AJOUT de {quantite_a_entrer} unité(s) de {reference}")
                print(f"\nVous venez d'ajouter {quantite_a_entrer} unité(s) de {reference}.\nIl y a maintenant {inventaire[reference]} unité(s) en stock.\n")
                # proposer à l'utilisateur de réaliser une nouvelle opération ou de revenir au menu
                continuer = input("\nVoulez-vous ajouter autre chose ? (o/n)\n\n").lower()
                if continuer == "n":
                    return
                if continuer == "o":
                    break
                else:
                    return
            else:
                print("\nVeuillez saisir à nouveau votre réponse.")
