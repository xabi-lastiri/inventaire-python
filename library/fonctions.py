def valeur_saisie_vide(n):
    if str(n) == "":
        return True

def reference_existe(n, x): # ici, n correspond au champ saisi et x à l'inventaire
    if n in x:
        return True
    else:
        return False

def verifier_valeur_entiere_positive(n):
    try:
        n = int(n)
    except ValueError:
        return False
    if n < 0:
        return False
    else:
        return True

def afficher_liste_references(n):
    return ', '.join(n.keys())