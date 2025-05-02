from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_register():
    response = client.post("/api/users/", json={"email": "test@mail.com", "password": "123456"})
    assert response.status_code == 200
    assert "email" in response.json()
