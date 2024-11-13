def verifier_valeur_saisie_vide(n):
    if str(n) == "":
        return True

def verifier_reference_existe(n, x):
    if n in x:
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

def verifier_stock_suffisant(n, x, y):
    y = int(y)
    if y <= n[x]:
        return True
    else:
        print("Le stock est insuffisant")
        return False

def afficher_liste_references(n):
    return ', '.join(n.keys())

def confirmer():
    while True:
        n = input().lower()
        if n == "o":
            return True
        elif n == "n":
            return False
        else:
            print("Veuillez saisir à nouveau votre réponse.")