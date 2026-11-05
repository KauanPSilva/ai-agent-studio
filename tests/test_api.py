from models.chat import ChatRequest
from pydantic import ValidationError
from fastapi.testclient import TestClient
from main import app
from services.chat_service import generate_response
from unittest.mock import patch

client = TestClient(app)


def test_health():

    response = client.get("/health")

    assert response.json() == {"status": "ok"}
    assert response.status_code == 200


def test_chat_request_valid_prompt():

    with patch("main.generate_response") as mock_generate:
        mock_generate.return_value = "Docker utiliza containers."

        response = client.post("/chat", json={"prompt": "Explique o funcionamento do Docker"})

        mock_generate.assert_called_once_with("Explique o funcionamento do Docker")

    assert response.status_code == 200
    assert response.json() == {"response": "Docker utiliza containers."}


def test_chat_request_invalid_prompt():

    response = client.post("/chat", json={"prompt": "                                    "})

    assert response.status_code == 422

