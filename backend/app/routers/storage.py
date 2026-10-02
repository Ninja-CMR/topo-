from fastapi import APIRouter, HTTPException, status, UploadFile, File, Form, Depends
from app.supabase_client import supabase
from app.dependencies.auth import get_current_user

router = APIRouter(prefix="/storage", tags=["File Storage"])

@router.post("/upload")
async def upload_file(
    bucket_name: str = Form(...),
    file_path: str = Form(...),
    file: UploadFile = File(...),
    current_user=Depends(get_current_user)
):
    """Uploade un fichier vers un Bucket Supabase Storage."""
    try:
        contents = await file.read()
        res = supabase.storage.from_(bucket_name).upload(
            path=file_path,
            file=contents,
            file_options={"content-type": file.content_type or "application/octet-stream"}
        )
        # Générer l'URL publique du fichier
        public_url = supabase.storage.from_(bucket_name).get_public_url(file_path)
        return {
            "message": "Fichier uploadé avec succès",
            "path": file_path,
            "public_url": public_url
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Erreur lors de l'upload du fichier vers Supabase Storage: {str(e)}"
        )

@router.get("/public-url")
async def get_public_url(bucket_name: str, file_path: str):
    """Récupère l'URL publique d'un fichier hébergé sur Supabase Storage."""
    try:
        url = supabase.storage.from_(bucket_name).get_public_url(file_path)
        return {"bucket": bucket_name, "file_path": file_path, "public_url": url}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Impossible de récupérer l'URL publique: {str(e)}"
        )
