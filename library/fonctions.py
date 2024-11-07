def f0_valeur_saisie_vide(n):
    if str(n) == "":
        return True

def f1_reference_existe(n, x): # ici, n correspond au champ saisi et x à l'inventaire
    if n in x:
        return True
    else:
        return False

def f2_verifier_valeur_entiere_positive(n):
    if type(n) == int and n > 0:
        return True
    else:
        return False

def f3_afficher_liste_references(n):
    return ', '.join(n.keys())