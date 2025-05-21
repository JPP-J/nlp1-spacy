from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)  # Creates a test client for your API

# Test the root endpoint
def test_root():
    response = client.get("/")
    assert response.status_code == 200  # Check if status is OK
    assert response.json() == {"message": "Welcome to the NLP API!"}  # Check response content

# Test the modes endpoint
def test_get_modes():
    response = client.post("/modes")
    assert response.status_code == 200
    assert "available_modes" in response.json()  # Check if response has modes

# Test the pipelines endpoint
def test_get_pipelines():
    response = client.post("/pipelines")
    assert response.status_code == 200
    assert "available_pipelines" in response.json()  # Check if response has pipelines

# Test the process endpoint with NER
def test_process():
    data = {
        "text1": "Hello, how are you?",
        "text2": "Doctor take care patient",
        "mode": "NER"
    }
    response = client.post("/process", json=data)
    assert response.status_code == 200
    assert "mode" in response.json()     # Check if response has mode
    assert "result" in response.json()   # Check if response has result
    assert response.json()["mode"] == "NER"  # Check if mode is correct
    assert isinstance(response.json()["result"], list)  # Check if result is a list