from fastapi.testclient import TestClient
from httpx import Response
from chatbot.main import app

client = TestClient(app=app)

def test_health():
    response: Response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
