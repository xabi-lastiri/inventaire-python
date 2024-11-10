from modules.p0_quitter import p0_quitter
from modules.p3_ajouter_reference import p3_ajouter_reference
from modules.p1_vendre import p1_vendre
from modules.p2_ajouter_stock import p2_ajouter_stock
from modules.p5_afficher_stock import p5_afficher_stock
from modules.p6_exporter_fiche_stock import p6_exporter_fiche_stock
from modules.p4_supprimer_reference import p4_supprimer_reference


while True:
    from data.inventaire import inventaire
    menu = input(f"\nSélectionner le programme :\n\n 0. Quitter \n 1. Vendre \n 2. Ajouter du stock \n 3. Ajouter une référence \n 4. Supprimer une référence \n 5. Afficher le stock \n 6. Exporter la fiche de stock  \n\n ")
    if menu == "0":
        p0_quitter()
    if menu == "1":
        p1_vendre(inventaire)
    if menu == "2":
        p2_ajouter_stock(inventaire)
    if menu == "3":
        p3_ajouter_reference(inventaire)
    if menu == "4":
        p4_supprimer_reference(inventaire)
    if menu == "5":
        p5_afficher_stock(inventaire)
    if menu == "6":
        p6_exporter_fiche_stock(inventaire)