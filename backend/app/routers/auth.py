from fastapi import APIRouter, HTTPException, status, Depends
from app.schemas.auth import UserSignUp, UserLogin, TokenResponse
from app.supabase_client import supabase
from app.dependencies.auth import get_current_user

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(user_data: UserSignUp):
    """
    Inscription d'un nouvel utilisateur directement dans Supabase Auth.
    """
    try:
        res = supabase.auth.sign_up({
            "email": user_data.email,
            "password": user_data.password,
            "options": {
                "data": user_data.user_metadata or {}
            }
        })
        
        if not res.user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Impossible de créer l'utilisateur dans Supabase."
            )
            
        user_dict = res.user.model_dump() if hasattr(res.user, "model_dump") else dict(res.user)
        session_dict = res.session.model_dump() if res.session and hasattr(res.session, "model_dump") else (dict(res.session) if res.session else None)
        
        return {
            "message": "Utilisateur créé avec succès dans Supabase !",
            "user": user_dict,
            "session": session_dict
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Erreur d'inscription Supabase: {str(e)}"
        )

@router.post("/login", response_model=TokenResponse)
async def login(credentials: UserLogin):
    """Connexion d'un utilisateur et récupération du token JWT Supabase."""
    try:
        res = supabase.auth.sign_in_with_password({
            "email": credentials.email,
            "password": credentials.password
        })
        if not res.session:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Identifiants invalides ou email non confirmé."
            )
        return {
            "access_token": res.session.access_token,
            "token_type": "bearer",
            "user": res.user.model_dump() if hasattr(res.user, "model_dump") else dict(res.user)
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Échec de la connexion: {str(e)}"
        )

@router.get("/me")
async def get_me(current_user=Depends(get_current_user)):
    """Récupère le profil de l'utilisateur actuellement connecté."""
    return {"user": current_user}
