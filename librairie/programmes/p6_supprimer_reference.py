from librairie.fonctions import f0_valeur_saisie_vide, f1_reference_existe


def p6_supprimer_reference(inv):
    while True:
        reference = input("Saisissez la référence à supprimer de l'inventaire (pour annuler, laissez vide) \n")
        if f0_valeur_saisie_vide(reference):
            return
        if f1_reference_existe(reference,inv):
            break
        else:
            print("La référence n'existe pas")
    while True:
        n = input(f"Confirmez-vous ? (o/n) \n")
        if n == "o":
            break
        if n == "n":
            return
        else:
            print("Veuillez saisir à nouveau votre réponse.")
    del inv[reference]
    print(f"Nous vous confirmons la suppression de la référence {reference}")