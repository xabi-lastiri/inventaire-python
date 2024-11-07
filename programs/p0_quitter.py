import sys


def p0_quitter():
    while True:
        n = input(f"\nConfirmez-vous vouloir quitter ? (o/n) \n\n")
        if n == "o":
            sys.exit()
        if n == "n":
            break
        else:
            print("\nValeur incorrecte. Veuillez re-saisir votre réponse.")