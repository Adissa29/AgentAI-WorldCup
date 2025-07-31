class Lieu:
    def __init__(self, nom, adresse, capacite):
        self.nom = nom
        self.adresse = adresse
        self.capacite = capacite

    def afficher_info(self):
        return f"{self.nom}, {self.adresse} - Capacité : {self.capacite}"

    def verifier_capacite(self, nbr_personnes):
        return self.capacite >= nbr_personnes
