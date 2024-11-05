import sys

def p0_quitter():
    while True:
        n = input(f"Confirmez-vous ? (o/n) \n")
        if n == "o":
            sys.exit()
        if n == "n":
            break
        else:
            print("Veuillez saisir à nouveau votre réponse.")