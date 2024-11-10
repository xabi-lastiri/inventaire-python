from library import *

def m7_exporter_fiche_stock(inventaire):
    with open('fiche_stock.csv','w') as f:
        writer = csv.writer(f)
        writer.writerow(["Référence", "Stock"])
        for reference, quantite in inventaire.items():
            writer.writerow([reference, inventaire[reference]])
    print("\nExport réalisé avec succès.\n")