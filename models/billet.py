class Billet:
    def __init__(self, id_billet, prix_terrain, categorie, match):
        self.id_billet = id_billet
        self.prix_terrain = prix_terrain
        self.categorie = categorie
        self.match = match

    def obtenir_details(self):
        return f"Billet {self.id_billet} - {self.categorie} - {self.match} - {self.prix_terrain}€"
