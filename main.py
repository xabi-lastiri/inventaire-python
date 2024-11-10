from modules import *
from data import *

# demander à l'utilisateur de s'autentifier pour permettre le traçage des opérations
utilisateur = input("Saisissez votre nom : ")
while True:
    menu = input(f"\nSélectionner le programme :\n\n 0. Quitter \n 1. Vendre \n 2. Ajouter du stock \n 3. Ajouter une référence \n 4. Supprimer une référence \n 5. Afficher le stock \n 6. Afficher le registre des opérations \n 7. Exporter la fiche de stock \n 8. Exporter le registre des opérations  \n\n")
    if menu == "0":
        m0_quitter()
    if menu == "1":
        m1_vendre(inventaire, registre, utilisateur)
    if menu == "2":
        m2_ajouter_stock(inventaire, registre, utilisateur)
    if menu == "3":
        m3_ajouter_reference(inventaire, registre, utilisateur)
    if menu == "4":
        m4_supprimer_reference(inventaire, registre, utilisateur)
    if menu == "5":
        m5_afficher_stock(inventaire)
    if menu == "6":
        m6_afficher_registre(registre)
    if menu == "7":
        m7_exporter_fiche_stock(inventaire)
    if menu == "8":
        m8_exporter_registre(registre)