import os
import sys

from fastapi.testclient import TestClient

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from main import app

client = TestClient(app)

def test_search_valid():
    resp = client.get("/search", params={"q": "iphone"})
    assert resp.status_code == 200
    body = resp.json()
    assert body["query"] == "iphone"
    assert len(body["results"]) == 2


def test_search_empty_query():
    resp = client.get("/search", params={"q": "   "})
    assert resp.status_code == 400
