from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home_status():
    response = client.get("/")
    assert response.status_code == 200
    assert "CidadãoConecta SP" in response.text

def test_elegibilidade_bolsa_familia():
    response = client.get("/api/elegibilidade?renda_per_capita=180&inscrito_cadunico=true")
    assert response.status_code == 200
    dados = response.json()
    assert "Bolsa Família" in dados["beneficios_identificados"]
    assert "Tarifa Social de Energia Elétrica" in dados["beneficios_identificados"]

def test_lista_cras():
    response = client.get("/api/cras")
    assert response.status_code == 200
    assert response.json()["cidade"] == "São Paulo - SP"
