# Fonction pour vérifier si une chaîne peut être convertie en un entier
def est_entier(chaine):
    try:
        entier = int(chaine)
        return True
    except ValueError:
        return False

# Saisie de N jusqu'à ce que l'utilisateur entre un entier valide
while True:
    n_str = input("Entrez un entier supérieur à zéro (N) : ")
    if est_entier(n_str):
        N = int(n_str)
        if N > 0:
            break
    print("Veuillez entrer un entier valide supérieur à zéro.")

# Affichage des tables de multiplication de 1 à N
for i in range(1, N + 1):
    print(f"\nTable de multiplication de {i} :")
    for j in range(1, 11):
        resultat = i * j
        print(f"{i} x {j} = {resultat}")
