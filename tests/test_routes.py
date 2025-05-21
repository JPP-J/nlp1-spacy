from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the NLP API!"}

def test_get_modes():
    response = client.post("/modes")
    assert response.status_code == 200
    assert "available_modes" in response.json()

def test_get_pipelines():
    response = client.post("/pipelines")
    assert response.status_code == 200
    assert "available_pipelines" in response.json() 

def test_process():
    data = {
        "text1": "Hello, how are you?",
        "text2": "Doctor take care patient",
        "mode": "NER"
    }
    response = client.post("/process", json=data)
    assert response.status_code == 200
    assert "mode" in response.json()
    assert "result" in response.json()
    assert response.json()["mode"] == "NER"
    assert isinstance(response.json()["result"], list)  # Assuming NER returns a list of entities
