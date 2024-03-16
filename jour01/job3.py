# Affichage de l'alphabet en utilisant la fonction ord() et chr()
def afficher_alphabet():
    for i in range(97, 123):
        print(chr(i), end=' ')

afficher_alphabet()