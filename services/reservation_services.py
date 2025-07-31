from utils.data_manager import lire_donnees, ecrire_donnees

def reserver_billet(utilisateur, categorie, prix, siege, rang, entree):
    billet = {
        "utilisateur": utilisateur,
        "categorie": categorie,
        "prix": prix,
        "siege": siege,
        "rang": rang,
        "entree": entree
    }
    billets = lire_donnees("data/billets.json")
    billets.append(billet)
    ecrire_donnees("data/billets.json", billets)
    return billet
