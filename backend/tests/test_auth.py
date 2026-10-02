import pytest
from unittest.mock import MagicMock, patch
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    """Vérifie le bon fonctionnement du serveur FastAPI."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "FastAPI Supabase Backend"}

@patch("app.routers.auth.supabase")
def test_signup_success(mock_supabase):
    """Test réussi de l'inscription d'un développeur."""
    # Simuler la réponse de Supabase auth.sign_up
    mock_user = MagicMock()
    mock_user.id = "dev-12345"
    mock_user.email = "dev@exemple.cm"
    
    mock_res = MagicMock()
    mock_res.user = {"id": "dev-12345", "email": "dev@exemple.cm"}
    mock_supabase.auth.sign_up.return_return_value = mock_res
    mock_supabase.auth.sign_up.return_value = mock_res

    payload = {
        "email": "dev@exemple.cm",
        "password": "Password123!",
        "user_metadata": {
            "full_name": "Jean Dupont",
            "phone": "+237699999999"
        }
    }

    response = client.post("/api/auth/signup", json=payload)
    assert response.status_code == 201
    json_data = response.json()
    assert json_data["message"] == "Utilisateur créé avec succès"
    assert "user" in json_data

@patch("app.routers.auth.supabase")
def test_signup_failure(mock_supabase):
    """Test de l'échec de l'inscription en cas d'erreur de Supabase."""
    mock_supabase.auth.sign_up.side_effect = Exception("Email déjà utilisé")

    payload = {
        "email": "existant@exemple.cm",
        "password": "Password123!",
        "user_metadata": {
            "full_name": "Dev Existant",
            "phone": "+237699999999"
        }
    }

    response = client.post("/api/auth/signup", json=payload)
    assert response.status_code == 400
    assert "Échec de l'inscription" in response.json()["detail"]
