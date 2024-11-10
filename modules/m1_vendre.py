from library import *

def m1_vendre(inventaire, registre, utilisateur):
    while True:
        # pour arrêter le programme que lorsque l'utilisateur le décide
        while True:
            # demander à l'utilisateur de saisir la référence à vendre
            # vérifier que la référence à vendre existe dans l'inventaire
            reference = input(f"\nSaisissez la référence à vendre ({f3_afficher_liste_references(inventaire)})\nPour annuler, laissez vide.\n\n")
            if f0_valeur_saisie_vide(reference):
                return
            if not f1_reference_existe(reference, inventaire):
                print(f"\n{reference} n'existe pas dans l'inventaire.")
            if inventaire[reference] == 0:
                print("Le stock est nul.")
            else:
                break
        while True:
            # demander à l'utilisateur de saisir la quantité à vendre
            # vérifier que la quantité à vendre soit (1) cohérente et (2) possible compte tenu du stock diponible dans l'inventaire au moment de l'opération
            try:
                quantite_a_vendre = int(input(f"\nIl reste {inventaire[reference]} unité(s) en stock pour le produit {reference}.\nSaisissez la quantité à vendre : \n\n"))
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
                # enregistrement de l'opération dans le registre
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