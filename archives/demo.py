import csv

inventaire = {
    "pomme": 50,
    "banane": 100,
    "orange": 75
}

def verifier_entier_positif(n):
    if type(n) == int and n > 0:
        return True
    else:
        return False

def verifier_stock_suffisant(n,x):
    if int(n) <= inventaire[x]:
        return True
    else:
        return False

def afficher_stock():
    print(f"Voici l'état actuel des stocks :")
    for fruit, quantite in inventaire.items():
        print(f" \n {fruit}: {quantite} unité(s) \n ----------- \n ")

def afficher_references():
    return ', '.join(inventaire.keys())

def vendre():
    while True:
        fruit_a_acheter = input("Quel fruit souhaitez-vous vendre ? " + "(" + str(afficher_references()) + ") \n Saisir la valeur ou annuler \n ")
        if fruit_a_acheter == "annuler":
            menu()
        while fruit_a_acheter not in inventaire:
            print(f"Vous ne ne vendez pas de {fruit_a_acheter}. Veuillez re-saisir une valeur.")
        print(f"Il vous reste {inventaire[fruit_a_acheter]} {fruit_a_acheter}(s) en stock. ")
        while True:
            qte_a_acheter = input("Combient d'unités souhaitez-vous vendre ? (saisir la valeur, ou annuler) ")
            if qte_a_acheter == "annuler":
                menu()
            try:
                qte_a_acheter = int(qte_a_acheter)
                if not verifier_entier_positif(qte_a_acheter):
                    print("La valeur que vous avez saisie est incorrecte")
                elif not verifier_stock_suffisant(qte_a_acheter, fruit_a_acheter):
                    print("Le stock est insuffisant.")
                else:
                    break
            except ValueError:
                print("Veuillez entrer un nombre entier valide")

        inventaire[fruit_a_acheter] -= int(qte_a_acheter)
        print(f"Vous venez de vendre {qte_a_acheter} {fruit_a_acheter}(s). Il vous reste {inventaire[fruit_a_acheter]} {fruit_a_acheter}(s) en stock.")
        continuer = input("Voulez-vous vendre autre chose ?")
        if continuer == "non":
            break

def ajouter_reference():
    while True:
        produit_a_ajouter = input("Quel produit souhaitez-vous ajouter dans l'inventaire ? (saisir la valeur ou annuler) ")
        if produit_a_ajouter == "annuler":
            menu()
        confirmer = input(f"Vous confirmez vouloir ajouter {produit_a_ajouter} ? (oui/non) ")
        if confirmer == "oui":
            while True:
                try:
                    stock_initial = input("Quel est le stock initial ? (saisir la valeur ou annuler) ")
                    if stock_initial == "annuler":
                        break
                    else:
                        valider = input(f"Vous confirmer que le stock initial de {produit_a_ajouter} est {stock_initial}? (oui/non) ")
                        if valider == "oui":
                            inventaire[produit_a_ajouter] = int(stock_initial)
                            afficher_stock()
                            break
                        else:
                            break
                except ValueError:
                    print("Re-saisissez le stock initial ")
            continuer = input("Voulez-vous ajouter une autre référence ? ")
            if continuer == "non":
                break

def supprimer_reference():
    while True:
        reference_a_supprimer = input("Quel produit souhaitez-vous supprimer de l'inventaire ? " + "(" + str(afficher_references()) + ")" + "\n Saisir la valeur ou annuler \n ")
        if reference_a_supprimer == "annuler":
            menu()
        confirmer = input(f"Vous confirmez vouloir supprimer {reference_a_supprimer} ? (oui/non) ")
        if confirmer == "oui":
            del inventaire[reference_a_supprimer]
            afficher_stock()
            break
        else:
            break

def exporter_inventaire():
    with open('stock_fruit.csv','w') as f:
        writer = csv.writer(f)
        writer.writerow(["Stocks"])
        for fruit in inventaire:
            writer.writerow([fruit, inventaire[fruit]])

def ajouter_stock():
    while True:
        fruit_a_augmenter = input("Quel fruit souhaitez-vous stocker ? " + "(" + str(afficher_references()) + ") \n Saisir la valeur ou annuler \n ")
        if fruit_a_augmenter == "annuler":
            menu()
        while fruit_a_augmenter not in inventaire:
            print(f"Vous ne ne vendez pas de {fruit_a_augmenter}. Veuillez re-saisir une valeur.")
        while True:
            qte_a_saisir = input("Combient d'unités souhaitez-vous ajouter ? (saisir la valeur, ou annuler) ")
            if qte_a_saisir == "annuler":
                menu()
            try:
                qte_a_saisir = int(qte_a_saisir)
                if not verifier_entier_positif(qte_a_saisir):
                    print("La valeur que vous avez saisie est incorrecte")
            except ValueError:
                print("Veuillez entrer un nombre entier valide")

            inventaire[fruit_a_augmenter] += int(qte_a_saisir)
            print(f"Vous venez d'ajouter {qte_a_saisir} {fruit_a_augmenter}(s). Vous avez {inventaire[fruit_a_augmenter]} {fruit_a_augmenter}(s) en stock.")
            continuer = input("Voulez-vous ajouter autre chose ?")
            if continuer == "non":
                menu()
            else:
                break

def menu():
    while True:
        action = input("Menu principal. Programmes : \n a. consulter les stocks \n b. vendre \n c. ajouter une référence dans l'inventaire \n d. ajouter du stock \n e. supprimer une référence \n f. exporter l'inventaire en csv \n g. quitter \n \n ")
        if action == "a":
            afficher_stock()
        if action == "b":
            vendre()
        if action == "c":
            ajouter_reference()
        if action == "d":
            ajouter_stock()
        if action == "e":
            supprimer_reference()
        if action == "f":
            exporter_inventaire()
        if action == "g":
            quitter = input("Voulez-vous vraiment quitter ? (oui/non) ")
            if quitter == "oui":
                break
menu()