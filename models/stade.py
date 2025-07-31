from .lieu import Lieu

class Stade(Lieu):
    def __init__(self, nom_stade, adresse, capacite, type_terrain):
        super().__init__(nom_stade, adresse, capacite)
        self.type_terrain = type_terrain

    def obtenir_details_stade(self):
        return f"{self.nom} - {self.type_terrain}"
