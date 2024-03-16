# Fonction pour vérifier si un nombre est premier
def est_premier(nombre):
    if nombre <= 1:
        return False
    elif nombre <= 3:
        return True
    elif nombre % 2 == 0 or nombre % 3 == 0:
        return False
    i = 5
    while i * i <= nombre:
        if nombre % i == 0 or nombre % (i + 2) == 0:
            return False
        i += 6
    return True

# Affichage des nombres premiers jusqu'à 1000
print("Nombres premiers jusqu'à 1000 :")
for i in range(2, 1001):
    if est_premier(i):
        print(i, end=' ')
