from modules import *
from data import *

modules = ["Quitter", "Vendre", "Ajouter du stock", "Ajouter une référence", "Supprimer une référence", "Afficher le stock", "Afficher le registre des opérations", "Exporter la fiche de stock", "Exporter le registre des opérations"]

# demander à l'utilisateur de s'autentifier pour permettre le traçage des opérations
utilisateur = input("Saisissez votre nom : ")
print("")
while True:
    for module in modules:
        print(f"{modules.index(module)}. {module}")
    menu = input(f"\nSélectionner le programme : ")
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