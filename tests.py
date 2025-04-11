from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_products():
    response = client.get("/products")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_invalid_order():
    response = client.post("/orders", json={"items": [{"product_id": 999, "quantity": 5}]})
    assert response.status_code == 400
