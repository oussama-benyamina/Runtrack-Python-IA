# Initialisation des variables
montant_initial = float(input("Entrez le montant initial de l'investissement en euros : "))
taux_rendement_annuel = float(input("Entrez le taux de rendement annuel en pourcentage : "))

# Affichage du gain annuel en fonction du taux de rendement initial
gain_annuel = montant_initial * (taux_rendement_annuel / 100)
print(f"Le gain annuel avec un taux de rendement de {taux_rendement_annuel}% est de {gain_annuel} euros")

# Boucle pour simuler plusieurs années d'investissement
annees = int(input("Entrez le nombre d'années pour simuler l'investissement : "))
for annee in range(1, annees+1):
    # Augmentation du capital de l'investissement et du taux de rendement
    montant_initial += 5000
    taux_rendement_annuel += 2

    # Calcul du gain annuel après augmentation
    gain_annuel = montant_initial * (taux_rendement_annuel / 100)
    print(f"Le gain annuel après l'année {annee} est de {gain_annuel} euros")

    # Retrait de 10% du montant total et diminution du taux de rendement
    montant_initial -= 0.1 * montant_initial
    taux_rendement_annuel -= 1

# Calcul du montant final de l'investissement après plusieurs années
montant_final = montant_initial
nouveau_gain_annuel = montant_final * (taux_rendement_annuel / 100)

# Affichage du nouveau gain annuel après retrait et diminution du taux de rendement
print(f"Le nouveau gain annuel après retrait de 10% et diminution du taux de rendement est de {nouveau_gain_annuel} euros")
