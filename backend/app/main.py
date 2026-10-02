from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.routers import auth, data, storage, topoboard

app = FastAPI(
    title="Topo Application Backend API",
    description="Backend FastAPI avec intégration Supabase (Auth, Data, Storage, TopoBoards)",
    version="1.0.0"
)

# Configuration CORS recommandée pour autoriser toutes les origines et méthodes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclusion des routes
app.include_router(auth.router, prefix="/api")
app.include_router(data.router, prefix="/api")
app.include_router(storage.router, prefix="/api")
app.include_router(topoboard.router, prefix="/api")

@app.get("/health", tags=["Health"])
async def health_check():
    """Endpoint de santé pour valider que le serveur FastAPI fonctionne."""
    return {"status": "ok", "service": "FastAPI Supabase Backend"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
