import json

def lire_donnees(fichier):
    try:
        with open(fichier, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def ecrire_donnees(fichier, donnees):
    with open(fichier, "w", encoding="utf-8") as f:
        json.dump(donnees, f, indent=4, ensure_ascii=False)
