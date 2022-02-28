from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_sum_endpoint():
    response = client.get("/add/?a=2&b=3")
    assert response.status_code == 200
    assert response.json() == {"sum": 5}


def test_add_user():
    response = client.post("/users/", json={"username": "IVAN"})
    assert response.status_code == 200
    assert response.json()['username'] == "IVAN"

