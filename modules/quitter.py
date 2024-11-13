def quitter():
    while True:
        confirmer = input(f"\nConfirmez-vous vouloir quitter ? (o/n) \n\n").lower()
        if confirmer == "o":
            exit()
        if confirmer == "n":
            break
        else:
            print("\nValeur incorrecte. Veuillez re-saisir votre réponse.")