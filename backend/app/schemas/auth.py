from pydantic import BaseModel, EmailStr
from typing import Optional, Dict, Any

class UserSignUp(BaseModel):
    email: EmailStr
    password: str
    user_metadata: Optional[Dict[str, Any]] = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: Dict[str, Any]

class UserProfile(BaseModel):
    id: str
    email: Optional[str] = None
    role: Optional[str] = None
    user_metadata: Optional[Dict[str, Any]] = None
