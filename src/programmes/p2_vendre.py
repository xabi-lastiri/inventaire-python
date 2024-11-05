from src.programmes.fonctions import f0_valeur_saisie_vide, f1_reference_existe, f2_verifier_valeur_entiere_positive, f3_afficher_liste_references


def p2_vendre(inv):
    while True:
        reference = input(f"Saisissez la référence à vendre ({f3_afficher_liste_references(inv)})\n (pour annuler, laissez vide) \n")
        if f0_valeur_saisie_vide(reference):
            return
        if f1_reference_existe(reference, inv):
            break
        else:
            print("La référence n'existe pas.")
    while True:
        try:
            quantite_a_vendre = input(f"Il reste {inv[reference]} unité(s) en stock. Saisissez la quantité à vendre : \n  ")
            quantite_a_vendre = int(quantite_a_vendre)
            if f2_verifier_valeur_entiere_positive(quantite_a_vendre) and quantite_a_vendre <= inv[reference]:
                break
            print("Le stock est insuffisant.")
        except ValueError:
            print("Valeur incorrecte.")
    while True:
        n = input(f"Confirmez-vous l'opération ? (o/n) \n")
        if n == "o":
            break
        if n == "n":
            return
        else:
            print("Veuillez saisir à nouveau votre réponse.")
    inv[reference] -= quantite_a_vendre
    print(f"Vous venez de vendre {quantite_a_vendre} unité(s) de {reference}. Il reste maintenant {inv[reference]} unité(s) en stock")