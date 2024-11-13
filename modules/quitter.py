from library.fonctions import *


def quitter():
    print(f"\nConfirmez-vous vouloir quitter ? (o/n) \n")
    if confirmer():
        exit()
    else:
        return