from fastapi.testclient import TestClient
from app.main import app

def test_crud():
    client = TestClient(app)
    r = client.post("/notes", json={"text": "hello"})
    assert r.status_code == 200
    nid = r.json()["id"]

    r = client.get(f"/notes/{nid}")
    assert r.status_code == 200 and r.json()["text"] == "hello"

    r = client.delete(f"/notes/{nid}")
    assert r.status_code == 200
    r = client.get(f"/notes/{nid}")
    assert r.status_code == 404
