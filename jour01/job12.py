# Fonction pour déterminer le type de triangle
def type_triangle(a, b, c):
    # Vérification si les longueurs peuvent former un triangle
    if a + b > c and a + c > b and b + c > a:
        # Vérification si le triangle est équilatéral
        if a == b == c:
            return "équilatéral"
        # Vérification si le triangle est rectangle
        elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            # Vérification si le triangle est également isocèle
            if a == b or a == c or b == c:
                return "rectangle et isocèle"
            else:
                return "rectangle"
        # Vérification si le triangle est isocèle
        elif a == b or a == c or b == c:
            return "isocèle"
        # Si le triangle n'est ni équilatéral, ni rectangle, ni isocèle, alors il est quelconque
        else:
            return "quelconque"
    else:
        return "impossible de former un triangle"

# Saisie des longueurs des côtés du triangle
a = float(input("Entrez la longueur du côté a : "))
b = float(input("Entrez la longueur du côté b : "))
c = float(input("Entrez la longueur du côté c : "))

# Détermination du type de triangle
type_tri = type_triangle(a, b, c)

# Affichage du résultat
print("Avec les longueurs données, il est possible de former un triangle", type_tri)
