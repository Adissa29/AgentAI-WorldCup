# AgentAI - Réservation de billets pour la FIFA World Cup 2026 

## Description
AgentAI est une API intelligente construite avec FastAPI pour :
- Réserver des billets pour la Coupe du Monde 2026
- Vérifier la capacité disponible dans un stade
- Notifier les utilisateurs ayant réservé

## Lancement de l’application

```bash
uvicorn main:app --reload


Architecture du projet

AgentAI/
│
├── gui/                  🌐 Interface API
│   └── interface.py
│
├── routes/               🚦 Routes IA
│   └── reservation_routes.py
│
├── data/                 📁 Stockage JSON
│   └── billets.json
│
├── models/               🧩 Modèles Python
│   ├── utilisateur.py
│   ├── supporter.py
│   ├── lieu.py
│   ├── stade.py
│   ├── billet.py
│   └── evenement.py
│
├── services/             🔧 Logique métier
│   └── reservation_service.py
│
├── utils/                🛠️ Fonctions utilitaires
│   └── data_manager.py
│
├── main.py               🚀 Point d’entrée FastAPI
├── requirements.txt      📦 Dépendances
└── README.md             📖 Présentation du projet


###Diagramme UML PlantUML

@startuml

package models {
    class Utilisateur {
        - nom : String
        - email : String
        - langue : String
        + reserver_billet(e : Evenement, n : int)
        + recevoir_notification(message : String)
    }

    class Supporter {
        - pays : String
        - prix_enthousiasme : Float
        + encourager(e : Evenement)
    }

    class Lieu {
        - nom : String
        - adresse : String
        - capacite : int
        + afficher_info()
        + verifier_capacite(nbr_personnes : int) : bool
    }

    class Stade {
        - nom_stade : String
        - type_terrain : String
        + obtenir_details_stade()
    }

    class Billet {
        - id_billet : String
        - prix_terrain : Float
        - categorie : String
        - match : String
        + obtenir_details()
    }

    class Evenement {
        - id_evenement : String
        - nom : String
        - date : datetime
        - prix_billet : Float
        - participants : List<Utilisateur>
        - billets : List<Billet>
        - supporters : List<Supporter>
        + ajouter_evenement()
        + notifier_participants()
        + creer_billet(id_billet : String, categorie : String) : Billet
        + ajouter_supporter(s : Supporter)
    }

    Stade --|> Lieu
    Supporter --|> Utilisateur

    Evenement --> "1" Stade
    Evenement --> "*" Billet
    Evenement --> "*" Utilisateur : participants
    Evenement --> "*" Supporter : supporters
    Utilisateur --> Evenement : reserve
    Supporter --> Evenement : encourage
}

package routes {
    class reservation_routes {
        + router
    }
}

package gui {
    class interface {
        + app
    }
}

package services {
    class reservation_service {
        + logique_reservation()
    }
}

package utils {
    class data_manager {
        + load_json()
        + save_json()
    }
}

interface --> reservation_routes
reservation_routes --> reservation_service
reservation_service --> data_manager
reservation_service --> Evenement

@enduml


 ## À noter
Les classes du dossier models/ sont regroupées dans le package models.

Les relations d’héritage (Supporter hérite de Utilisateur, Stade hérite de Lieu) sont modélisées.

Les relations de composition (Evenement → Billet, Utilisateur, Supporter, etc.) sont représentées avec des flèches.

Les autres packages (gui, routes, services, utils) montrent comment les composants interagissent entre eux.



## Routes disponibles
/ia/reservation_billet : Répond sur les billets réservés

/ia/capacite_stade : Informe sur les places disponibles

/ia/notifications : Liste les notifications envoyées

##Exemple de question IA
Combien de billets réservés ?

Y a-t-il des places disponibles ?

Qui a reçu une notification ?


## 1. Route : /ia/reservation_billet
Objectif : Savoir combien de billets ont été réservés et obtenir les détails.

## Questions possibles :

Combien de billets ont été réservés ?

Quels sont les billets réservés ?

Donne-moi les détails des billets.

Qui a réservé un billet pour le match ?

## Réponse attendue :

3 billets ont été réservés :

Oussama → Porte A, Rang 3, Siège 14, Catégorie Or

Glody → Porte B, Rang 2, Siège 7, Catégorie Argent

Babatunde → Porte A, Rang 1, Siège 1, Catégorie Bronze
Match : Final - Adresse : BMO Field


## 2. Route : /ia/capacite_stade
Objectif : Savoir s’il reste de la place dans le stade.

## Questions possibles :

Y a-t-il encore des places disponibles ?

Combien de places restent dans le stade ?

Quelle est la capacité restante ?

## Réponse attendue :

Il reste 47 000 places disponibles au stade BMO Field (capacité 50 000 - 3 billets déjà réservés).


## 3. Route : /ia/notifications
Objectif : Savoir qui a reçu une notification.


## Questions possibles :

Qui a reçu une notification ?

Quels utilisateurs ont été notifiés ?

Notifications envoyées à qui ?


## Réponse attendue :

Une notification a été envoyée à :

Oussama (oussama@example.com)

Glody (glody@example.com)

Babatunde (babatunde@example.com)


## Comment poser la question :
Dans l’interface Swagger (http://127.0.0.1:8000/docs) :

Clique sur la route /ia/reservation_billet

Clique sur Try it out

Dans question, écris : Combien de billets ont été réservés ?

Clique sur Execute