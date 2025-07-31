from fastapi import APIRouter, Body
from pydantic import BaseModel
from utils.data_manager import lire_donnees, ecrire_donnees
from typing import List

router = APIRouter()

FICHIER = "data/billets.json"
CAPACITE_STADE = 45736

class QuestionRequest(BaseModel):
    question: str

@router.get("/", tags=["Accueil"])
def accueil():
    return {"message": "WE ARE 2026 - Bienvenue sur l'interface de réservation !"}

@router.post("/ia/reservation_billet", tags=["IA - Réservation de billets"])
def reservation_billet(req: QuestionRequest = Body(...)):
    billets = lire_donnees(FICHIER)
    question = req.question.lower()
    if "combien" in question or "réservé" in question:
        if not billets:
            return {"réponse": "Aucun billet n'a encore été réservé."}
        reponse = f"{len(billets)} billet(s) ont été réservés :\n"
        for i, billet in enumerate(billets, 1):
            reponse += (
                f"\nBillet #{i} :\n"
                f"- Utilisateur : {billet.get('utilisateur')}\n"
                f"- Catégorie : {billet.get('categorie')}\n"
                f"- Prix : {billet.get('prix')} $\n"
                f"- Siège : {billet.get('siege')}\n"
                f"- Rangée : {billet.get('rang')}\n"
                f"- Entrée : {billet.get('entree')}\n"
                f"- Match : Portugal vs Argentine\n"
                f"- Adresse : BMO Field"
            )
        return {"réponse": reponse.strip()}
    return {"réponse": "Question non reconnue pour cette route."}

@router.post("/ia/capacite_stade", tags=["IA - Capacité du stade"])
def capacite_stade(req: QuestionRequest = Body(...)):
    billets = lire_donnees(FICHIER)
    question = req.question.lower()
    if "place" in question or "disponible" in question:
        reserves = len(billets)
        disponibles = CAPACITE_STADE - reserves
        return {"réponse": f"Il reste {disponibles} places disponibles dans le stade (sur {CAPACITE_STADE})."}
    return {"réponse": "Question non reconnue pour cette route."}

@router.post("/ia/notifications", tags=["IA - Notifications"])
def notifications(req: QuestionRequest = Body(...)):
    billets = lire_donnees(FICHIER)
    question = req.question.lower()
    if "notification" in question or "qui a reçu" in question:
        notifications = [f"{billet['utilisateur']} a reçu une notification pour le match Portugal vs Argentine." for billet in billets]
        return {"réponse": "\n".join(notifications)}
    return {"réponse": "Question non reconnue pour cette route."}
