from fastapi.testclient import TestClient
from pytest import fixture
from ner.app import app


@fixture
def client():
    return TestClient(app)


def test_get_ner__valid_input(client):
    response = client.post("/ner", json={
        "text": "Apple is looking at buying U.K. startup for $1 billion"
    })

    assert response.status_code == 200
    assert len(response.json()['entities']) == 3
