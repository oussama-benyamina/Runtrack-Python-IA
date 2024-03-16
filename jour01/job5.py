

class Produit:
    def __init__(self, nom, prix_unitaire, quantite_stock):
        self.nom = nom
        self.prix_unitaire = prix_unitaire
        self.quantite_stock = quantite_stock

    def afficher_informations(self):
        print(f"Nom du produit : {self.nom}")
        print(f"Prix unitaire : {self.prix_unitaire} euros")
        print(f"Quantité en stock : {self.quantite_stock}")

    def mise_a_jour_prix(self, pourcentage_augmentation):
        self.prix_unitaire *= (1 + pourcentage_augmentation / 100)
        print(f"Prix unitaire mis à jour avec une augmentation de {pourcentage_augmentation}%")

    def ajouter_stock(self, quantite):
        self.quantite_stock += quantite
        print(f"{quantite} unité(s) ajoutée(s) au stock")

    def acheter_produit(self, quantite):
        if quantite <= self.quantite_stock:
            self.quantite_stock -= quantite
            print(f"{quantite} unité(s) de {self.nom} achetée(s)")
        else:
            print("Stock insuffisant, impossible de réaliser l'achat")

# Fonction pour saisir les informations du produit
def saisir_informations_produit():
    nom = input("Entrez le nom du produit : ")
    prix_unitaire = float(input("Entrez le prix unitaire du produit (en euros) : "))
    quantite_stock = int(input("Entrez la quantité en stock du produit : "))
    return nom, prix_unitaire, quantite_stock

# Saisie des informations du produit
nom_produit, prix_produit, stock_produit = saisir_informations_produit()

# Création du produit
produit1 = Produit(nom_produit, prix_produit, stock_produit)

# Affichage des informations du produit
print("\nInformations du produit :")
produit1.afficher_informations()

# Mise à jour du prix avec une augmentation de 10%
pourcentage_augmentation = 10
produit1.mise_a_jour_prix(pourcentage_augmentation)

# Affichage des informations du produit après mise à jour du prix
print("\nInformations du produit après mise à jour du prix :")
produit1.afficher_informations()

# Ajout de stock
quantite_ajoutee = int(input("\nEntrez la quantité à ajouter au stock : "))
produit1.ajouter_stock(quantite_ajoutee)

# Affichage des informations du produit après ajout au stock
print("\nInformations du produit après ajout au stock :")
produit1.afficher_informations()

# Achat de produits
quantite_achetee = int(input("\nEntrez la quantité de produit que vous souhaitez acheter : "))
produit1.acheter_produit(quantite_achetee)

# Affichage des informations du produit après achat
print("\nInformations du produit après achat :")
produit1.afficher_informations()
