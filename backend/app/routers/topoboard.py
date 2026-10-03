from fastapi import APIRouter, HTTPException, status, Header, Query
from app.supabase_client import supabase
from app.schemas.topoboard import TopoBoardCreate, ResponseCreate
from typing import List, Dict, Any, Optional

router = APIRouter(prefix="/topoboards", tags=["TopoBoards"])

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_topoboard(payload: TopoBoardCreate, user_id: Optional[str] = Query(None)):
    """
    Crée un nouveau topoBoard dans la base de données Supabase, associé à l'utilisateur si spécifié.
    Limite maximale : 3 topoBoards par utilisateur.
    """
    try:
        clean_user_id = user_id.strip() if (user_id and user_id.strip() and user_id not in ("null", "undefined")) else None
        
        # Vérification du nombre de topoBoards existants
        count_query = supabase.table("topoboards").select("id")
        if clean_user_id:
            count_query = count_query.or_(f"user_id.eq.{clean_user_id},user_id.is.null")
        
        count_res = count_query.execute()
        existing_count = len(count_res.data) if count_res.data else 0
        if existing_count >= 3:
            raise HTTPException(
                status_code=400,
                detail="Limite de 3 topoBoards atteinte. Vous ne pouvez pas en créer davantage."
            )

        data = payload.dict()
        if clean_user_id:
            data["user_id"] = clean_user_id
        else:
            data.pop("user_id", None)
            
        res = supabase.table("topoboards").insert(data).execute()
        if not res.data:
            raise HTTPException(status_code=400, detail="Échec de la création du topoBoard dans Supabase")
        return res.data[0]
    except HTTPException:
        raise
    except Exception as e:
        print("Erreur création topoBoard:", str(e))
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=List[Dict[str, Any]])
async def list_topoboards(user_id: Optional[str] = Query(None)):
    """
    Récupère la liste des topoBoards (filtrée par user_id ou unassigned si spécifié).
    """
    try:
        query = supabase.table("topoboards").select("*, responses(*)")
        if user_id and user_id.strip() and user_id not in ("null", "undefined"):
            query = query.or_(f"user_id.eq.{user_id.strip()},user_id.is.null")
        
        try:
            res = query.order("created_at", desc=True).execute()
            return res.data or []
        except Exception:
            query_simple = supabase.table("topoboards").select("*")
            if user_id and user_id.strip() and user_id not in ("null", "undefined"):
                query_simple = query_simple.or_(f"user_id.eq.{user_id.strip()},user_id.is.null")
            res = query_simple.order("created_at", desc=True).execute()
            return res.data or []
    except Exception as e:
        print("Erreur lecture topoboards:", str(e))
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{board_id}")
async def get_topoboard_detail(board_id: str):
    """
    Récupère un topoBoard par son ID (UUID Supabase) avec toutes ses réponses associées.
    """
    try:
        res = supabase.table("topoboards").select("*, responses(*)").eq("id", board_id).execute()
        if not res.data:
            raise HTTPException(status_code=404, detail="topoBoard non trouvé")
        return res.data[0]
    except Exception as e:
        print(f"Erreur get_topoboard_detail pour ID '{board_id}':", str(e))
        raise HTTPException(status_code=404, detail="topoBoard introuvable ou ID invalide")


@router.post("/{board_id}/responses", status_code=status.HTTP_201_CREATED)
async def add_response(board_id: str, payload: ResponseCreate):
    """
    Ajoute un avis utilisateur / retour d'expérience à un topoBoard.
    """
    try:
        data = payload.dict()
        data["topoboard_id"] = board_id
        res = supabase.table("responses").insert(data).execute()
        if not res.data:
            raise HTTPException(status_code=400, detail="Échec de l'enregistrement de la réponse")
        return res.data[0]
    except HTTPException:
        raise
    except Exception as e:
        print(f"Erreur ajout réponse pour board '{board_id}':", str(e))
        raise HTTPException(status_code=500, detail=str(e))
