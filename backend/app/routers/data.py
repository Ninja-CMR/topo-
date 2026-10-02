from fastapi import APIRouter, HTTPException, status, Depends
from typing import Dict, Any, Optional
from app.supabase_client import supabase
from app.dependencies.auth import get_current_user
from app.schemas.data import DataRecordCreate, DataRecordUpdate, DataQueryRequest

router = APIRouter(prefix="/data", tags=["Data Storage & Query"])

@router.post("/query")
async def query_table(
    query_req: DataQueryRequest,
    current_user=Depends(get_current_user)
):
    """Effectue des requêtes/lectures sur une table de la base de données Supabase."""
    try:
        q = supabase.table(query_req.table_name).select(query_req.columns)
        if query_req.filters:
            for col, val in query_req.filters.items():
                q = q.eq(col, val)
        if query_req.limit:
            q = q.limit(query_req.limit)
        
        response = q.execute()
        return {"data": response.data, "count": len(response.data) if response.data else 0}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Erreur de lecture Supabase: {str(e)}"
        )

@router.post("/insert", status_code=status.HTTP_201_CREATED)
async def insert_record(
    record: DataRecordCreate,
    current_user=Depends(get_current_user)
):
    """Insère des données dans la table spécifiée."""
    try:
        response = supabase.table(record.table_name).insert(record.data).execute()
        return {"message": "Données insérées avec succès", "data": response.data}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Erreur d'insertion Supabase: {str(e)}"
        )

@router.put("/update")
async def update_record(
    record: DataRecordUpdate,
    current_user=Depends(get_current_user)
):
    """Met à jour un enregistrement dans la table spécifiée."""
    try:
        response = supabase.table(record.table_name)\
            .update(record.data)\
            .eq(record.match_column, record.match_value)\
            .execute()
        return {"message": "Données mises à jour avec succès", "data": response.data}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Erreur de mise à jour Supabase: {str(e)}"
        )

@router.delete("/{table_name}/{record_id}")
async def delete_record(
    table_name: str,
    record_id: str,
    match_column: str = "id",
    current_user=Depends(get_current_user)
):
    """Supprime un enregistrement d'une table spécifiée."""
    try:
        response = supabase.table(table_name).delete().eq(match_column, record_id).execute()
        return {"message": "Enregistrement supprimé avec succès", "data": response.data}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Erreur de suppression Supabase: {str(e)}"
        )
