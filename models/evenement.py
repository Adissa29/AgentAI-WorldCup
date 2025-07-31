class Evenement:
    def __init__(self, id_evenement, nom, date, lieu, prix_billet):
        self.id_evenement = id_evenement
        self.nom = nom
        self.date = date
        self.lieu = lieu
        self.prix_billet = prix_billet
        self.participants = []
        self.billets = []
        self.supporters = []

    def ajouter_evenement(self):
        pass

    def notifier_participants(self):
        pass

    def creer_billet(self, id_billet, categorie):
        billet = billet(id_billet, self.prix_billet, categorie, self.nom)
        self.billets.append(billet)
        return billet

    def ajouter_supporter(self, supporter):
        self.supporters.append(supporter)
