def verifier_valeur_saisie_vide(n):
    if str(n) == "":
        return True


def verifier_reference_existe(reference, inventaire):
    if reference in inventaire:
        return True
    else:
        print("La référence n'existe pas.")
        return False


def verifier_valeur_entiere_positive(n):
    try:
        n = int(n)
    except ValueError:
        print("Valeur incorrecte")
        return False
    if n < 0:
        print("Valeur incorrecte.")
        return False
    else:
        return True


def verifier_stock_suffisant(inventaire, reference, quantite):
    quantite = int(quantite)
    if quantite <= inventaire[reference]:
        return True
    else:
        print("Le stock est insuffisant")
        return False


def afficher_liste_references(inventaire):
    return ', '.join(inventaire.keys())


def confirmer():
    while True:
        n = input().lower()
        if n == "o":
            return True
        elif n == "n":
            return False
        else:
            print("Veuillez saisir à nouveau votre réponse.")