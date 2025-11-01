AgentAI – Ticket Reservation for the FIFA World Cup 2026
Description

AgentAI is an intelligent API built with FastAPI for:

Booking tickets for the 2026 World Cup

Checking available stadium capacity

Notifying users who have made reservations

Launching the Application
uvicorn main:app --reload

Project Architecture
AgentAI/
│
├── gui/                  🌐 API Interface
│   └── interface.py
│
├── routes/               🚦 AI Routes
│   └── reservation_routes.py
│
├── data/                 📁 JSON Storage
│   └── billets.json
│
├── models/               🧩 Python Models
│   ├── utilisateur.py
│   ├── supporter.py
│   ├── lieu.py
│   ├── stade.py
│   ├── billet.py
│   └── evenement.py
│
├── services/             🔧 Business Logic
│   └── reservation_service.py
│
├── utils/                🛠️ Utility Functions
│   └── data_manager.py
│
├── main.py               🚀 FastAPI Entry Point
├── requirements.txt      📦 Dependencies
└── README.md             📖 Project Overview

UML Diagram (PlantUML)
@startuml

package models {
    class Utilisateur {
        - name : String
        - email : String
        - language : String
        + book_ticket(e : Evenement, n : int)
        + receive_notification(message : String)
    }

    class Supporter {
        - country : String
        - enthusiasm_rate : Float
        + cheer(e : Evenement)
    }

    class Lieu {
        - name : String
        - address : String
        - capacity : int
        + show_info()
        + check_capacity(num_people : int) : bool
    }

    class Stade {
        - stadium_name : String
        - field_type : String
        + get_stadium_details()
    }

    class Billet {
        - ticket_id : String
        - field_price : Float
        - category : String
        - match : String
        + get_details()
    }

    class Evenement {
        - event_id : String
        - name : String
        - date : datetime
        - ticket_price : Float
        - participants : List<Utilisateur>
        - tickets : List<Billet>
        - supporters : List<Supporter>
        + add_event()
        + notify_participants()
        + create_ticket(ticket_id : String, category : String) : Billet
        + add_supporter(s : Supporter)
    }

    Stade --|> Lieu
    Supporter --|> Utilisateur

    Evenement --> "1" Stade
    Evenement --> "*" Billet
    Evenement --> "*" Utilisateur : participants
    Evenement --> "*" Supporter : supporters
    Utilisateur --> Evenement : books
    Supporter --> Evenement : cheers
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
        + booking_logic()
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

Notes

The classes in the models/ folder are grouped into the models package.

Inheritance relationships (e.g., Supporter inherits from Utilisateur, Stade inherits from Lieu) are modeled.

Composition relationships (e.g., Evenement → Billet, Utilisateur, Supporter) are represented with arrows.

Other packages (gui, routes, services, utils) show how components interact with one another.

Available Routes
Route	Description
/ia/reservation_billet	Returns information about booked tickets
/ia/capacite_stade	Reports available stadium seats
/ia/notifications	Lists notifications sent to users
Example AI Questions

How many tickets have been booked?

Are there any seats available?

Who received a notification?

1. Route: /ia/reservation_billet

Goal: Find out how many tickets have been booked and get details.

Possible Questions:

How many tickets have been booked?

What are the reserved tickets?

Give me the ticket details.

Who booked a ticket for the match?

Expected Response:

3 tickets have been booked:

Oussama → Gate A, Row 3, Seat 14, Gold Category

Glody → Gate B, Row 2, Seat 7, Silver Category

Babatunde → Gate A, Row 1, Seat 1, Bronze Category
Match: Final – Address: BMO Field

2. Route: /ia/capacite_stade

Goal: Find out if there are still available seats in the stadium.

Possible Questions:

Are there still seats available?

How many seats remain in the stadium?

What is the remaining capacity?

Expected Response:

There are 47,000 seats available at BMO Field (capacity 50,000 – 3 tickets already booked).

3. Route: /ia/notifications

Goal: Find out who has received a notification.

Possible Questions:

Who received a notification?

Which users were notified?

Notifications sent to whom?

Expected Response:

A notification was sent to:

Oussama (oussama@example.com
)

Glody (glody@example.com
)

Babatunde (babatunde@example.com
)

How to Ask the Question

In the Swagger interface (http://127.0.0.1:8000/docs):

Click on the route /ia/reservation_billet

Click Try it out

In the “question” field, type:

How many tickets have been booked?


Click Execute


## FRENCH VERSION ##

# AgentAI - Réservation de billets pour la FIFA World Cup 2026 

## Descriptions
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



