from library import *

def m8_exporter_registre(registre):
    with open('registre_operations.csv','w') as f:
        writer = csv.writer(f)
        writer.writerow(["Numéro", "Opération"])
        for operation in registre:
            numero = f"OPE{registre.index(operation)}"
            writer.writerow([numero, operation])
    print("\nExport réalisé avec succès.\n")