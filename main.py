from modules import *
from data import *

modules = ["Quitter",
           "Vendre",
           "Ajouter du stock",
           "Ajouter une référence",
           "Supprimer une référence",
           "Afficher le stock",
           "Afficher le registre des opérations",
           "Exporter la fiche de stock",
           "Exporter le registre des opérations"]

utilisateur = input("Saisissez votre nom : ")
print("")
while True:
    for module in modules:
        print(f"{modules.index(module)}. {module}")
    menu = input(f"\nSélectionner le programme : ")
    if menu == "0":
        quitter()
    if menu == "1":
        vendre(inventaire, registre, utilisateur)
    if menu == "2":
        ajouter_stock(inventaire, registre, utilisateur)
    if menu == "3":
        ajouter_reference(inventaire, registre, utilisateur)
    if menu == "4":
        supprimer_reference(inventaire, registre, utilisateur)
    if menu == "5":
        afficher_stock(inventaire)
    if menu == "6":
        afficher_registre(registre)
    if menu == "7":
        exporter_fiche_stock(inventaire)
    if menu == "8":
        exporter_registre(registre)