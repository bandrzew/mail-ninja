import pytest
from flask import json
from mcp_server import app
import sys
import os

# Ustawienie ścieżki do folderu src:
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../src")))
print("PYTHONPATH ustawiony na src:", sys.path)


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_mcp_analyze_success(client):
    payload = {
        "user_input": "Testowa treść wiadomości.",
        "style": "Profesjonalny"
    }
    response = client.post(
        "/analyze", data=json.dumps(payload), content_type="application/json"
    )

    assert response.status_code == 200
    data = json.loads(response.data.decode("utf-8"))
    assert "priority" in data
    assert "summary" in data
    assert "responses" in data


def test_mcp_analyze_failure(client):
    payload = {
        "user_input": "",
        "style": "Nieznany"
    }
    response = client.post(
        "/analyze", data=json.dumps(payload), content_type="application/json"
    )

    assert response.status_code == 500
    data = json.loads(response.data.decode("utf-8"))
    assert "error" in data
