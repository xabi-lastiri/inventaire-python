from src.programmes.fonctions import f0_valeur_saisie_vide, f1_reference_existe, f2_verifier_valeur_entiere_positive, f3_afficher_liste_references


def p3_ajouter_stock(inv):
    while True:
        reference = input(f"Saisissez la référence à stocker ({f3_afficher_liste_references(inv)}) \n (pour annuler, laissez vide) \n")
        if f0_valeur_saisie_vide(reference):
            return
        if f1_reference_existe(reference, inv): #à debuger
            break
        else:
            print("La référence n'existe pas.")
    while True:
        try:
            quantite_a_entrer = input(f"Saisissez la quantité à entrer : ")
            quantite_a_entrer = int(quantite_a_entrer)
            if f2_verifier_valeur_entiere_positive(quantite_a_entrer):
                break
        except ValueError:
            print("Valeur incorrecte.")
    while True:
        n = input(f"Confirmez-vous ? (o/n) \n")
        if n == "o":
            break
        if n == "n":
            return
        else:
            print("Veuillez saisir à nouveau votre réponse.")
    inv[reference] += quantite_a_entrer
    print(
        f"Vous venez d'ajouter {quantite_a_entrer} unité(s) de {reference}. Il y a maintenant {inv[reference]} unité(s) en stock")