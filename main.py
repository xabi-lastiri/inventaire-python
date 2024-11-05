from src.programmes.p0_quitter import p0_quitter
from src.programmes.p1_ajouter_reference import p1_ajouter_reference
from src.programmes.p2_vendre import p2_vendre
from src.programmes.p3_ajouter_stock import p3_ajouter_stock
from src.programmes.p4_afficher_stock import p4_afficher_stock
from src.programmes.p5_exporter_fiche_stock import p5_exporter_fiche_stock
from src.programmes.p6_supprimer_reference import p6_supprimer_reference


inv = {
    "pomme": 50,
    "banane": 100,
    "orange": 50
}


while True:
    menu = input(f"Sélectionner le programme : \n 0. Quitter \n 1. Ajouter une référence \n 2. Vendre \n 3. Ajouter du stock \n 4. Afficher le stock \n 5. Exporter la fiche de stock \n 6. Supprimer une référence \n ")
    if menu == "0":
        p0_quitter()
    if menu == "1":
        p1_ajouter_reference(inv)
    if menu == "2":
        p2_vendre(inv)
    if menu == "3":
        p3_ajouter_stock(inv)
    if menu == "4":
        p4_afficher_stock(inv)
    if menu == "5":
        p5_exporter_fiche_stock(inv)
    if menu == "6":
        p6_supprimer_reference(inv)