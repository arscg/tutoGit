import os

def afficher_nom_prenom():
    nom = os.environ.get('nom')
    prenom = os.environ.get('prenom')
    
    if nom is None or prenom is None:
        print("Usage: python script.py <nom> <prenom>")
    else:
        print("Nom :", nom)
        print("Prénom :", prenom)

# Appeler la fonction pour afficher le nom et le prénom
afficher_nom_prenom()
