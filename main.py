from modules.m0_quitter import m0_quitter
from modules.m3_ajouter_reference import m3_ajouter_reference
from modules.m1_vendre import m1_vendre
from modules.m2_ajouter_stock import m2_ajouter_stock
from modules.m5_afficher_stock import m5_afficher_stock
from modules.m6_exporter_fiche_stock import m6_exporter_fiche_stock
from modules.m4_supprimer_reference import m4_supprimer_reference


while True:
    from data.inventaire import inventaire
    menu = input(f"\nSélectionner le programme :\n\n 0. Quitter \n 1. Vendre \n 2. Ajouter du stock \n 3. Ajouter une référence \n 4. Supprimer une référence \n 5. Afficher le stock \n 6. Exporter la fiche de stock  \n\n ")
    if menu == "0":
        m0_quitter()
    if menu == "1":
        m1_vendre(inventaire)
    if menu == "2":
        m2_ajouter_stock(inventaire)
    if menu == "3":
        m3_ajouter_reference(inventaire)
    if menu == "4":
        m4_supprimer_reference(inventaire)
    if menu == "5":
        m5_afficher_stock(inventaire)
    if menu == "6":
        m6_exporter_fiche_stock(inventaire)