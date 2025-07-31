from fastapi import FastAPI
from routes.reservation_routes import router as reservation_router

app = FastAPI(
    title="AgentAI - Réservation de billets pour la FIFA World Cup 2026",
    description="Une interface intelligente pour réserver et suivre les billets du match Portugal vs Argentine.",
    version="1.0.0"
)

app.include_router(reservation_router)
