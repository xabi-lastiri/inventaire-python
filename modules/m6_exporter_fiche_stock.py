from library import csv


def m6_exporter_fiche_stock(inv):
    with open('fiche_stock.csv','w') as f:
        writer = csv.writer(f)
        writer.writerow(["Référence", "Stock"])
        for reference, quantite in inv.items():
            writer.writerow([reference, inv[reference]])
    print("\nExport réalisé avec succès.\n")