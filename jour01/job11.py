# Chaîne de caractères
chaine = "abcdefghijklmnopqrstuvwxyz" * 10

# Nombre de lignes pour la pyramide
nb_lignes = min(len(chaine), 28)  # 28 étant la hauteur maximale de la pyramide

# Affichage de la pyramide
for i in range(1, nb_lignes + 1):
    # Nombre de caractères à extraire pour cette ligne
    nb_caracteres = 2 * i - 1
    
    # Extraction des caractères pour cette ligne
    caracteres = chaine[:nb_caracteres]
    
    # Affichage de la ligne de la pyramide
    print(caracteres.center(50))  # Centrage pour une meilleure visualisation
