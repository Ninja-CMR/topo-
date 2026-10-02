from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class TopoBoardCreate(BaseModel):
    product_name: str
    product_url: str
    logo_url: Optional[str] = None
    hook_message: str
    description: Optional[str] = None
    feedback_question: str
    allow_rating: bool = True
    allow_whatsapp_contact: bool = True
    cta_text: Optional[str] = "Envoyer mon retour"
    brand_color: Optional[str] = "#FD711A"

class TopoBoardResponse(TopoBoardCreate):
    id: str
    user_id: Optional[str] = None
    created_at: Optional[str] = None

class ResponseCreate(BaseModel):
    topoboard_id: str
    rating: Optional[int] = 5
    comment: str
    whatsapp: Optional[str] = None

class ResponseDetail(ResponseCreate):
    id: str
    created_at: Optional[str] = None
