import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API de Churn Prediction ativa!"}

def test_predict():
    payload = {
        "gender": 1.0,
        "SeniorCitizen": 0.0,
        "Partner": 1.0,
        "Dependents": 0.0,
        "tenure": 12.0,
        "PhoneService": 1.0,
        "MultipleLines": 0.0,
        "InternetService": 2.0,
        "OnlineSecurity": 1.0,
        "OnlineBackup": 1.0,
        "DeviceProtection": 1.0,
        "TechSupport": 0.0,
        "StreamingTV": 0.0,
        "StreamingMovies": 0.0,
        "Contract": 0.0,
        "PaperlessBilling": 1.0,
        "PaymentMethod": 1.0,
        "MonthlyCharges": 70.5,
        "TotalCharges": 845.3
    }
    response = client.post("/predict/", json=payload)
    assert response.status_code == 200
    assert "churn" in response.json()
    assert response.json()["churn"] in [True, False]


def test_missing_field():
    payload = {
        # omita um campo obrigatório, por exemplo 'gender'
        "SeniorCitizen": 0.0,
        "Partner": 1.0,
        "Dependents": 0.0,
        "tenure": 12.0,
        "PhoneService": 1.0,
        "MultipleLines": 0.0,
        "InternetService": 2.0,
        "OnlineSecurity": 1.0,
        "OnlineBackup": 1.0,
        "DeviceProtection": 1.0,
        "TechSupport": 0.0,
        "StreamingTV": 0.0,
        "StreamingMovies": 0.0,
        "Contract": 0.0,
        "PaperlessBilling": 1.0,
        "PaymentMethod": 1.0,
        "MonthlyCharges": 70.5,
        "TotalCharges": 845.3
    }
    response = client.post("/predict/", json=payload)
    assert response.status_code == 422  # Unprocessable Entity


def test_invalid_values():
    payload = {
        "gender": -1,  # inválido, já que gender é 0 ou 1
        "SeniorCitizen": 2,  # inválido
        "Partner": 1.0,
        "Dependents": 0.0,
        "tenure": 12.0,
        "PhoneService": 1.0,
        "MultipleLines": 0.0,
        "InternetService": 2.0,
        "OnlineSecurity": 1.0,
        "OnlineBackup": 1.0,
        "DeviceProtection": 1.0,
        "TechSupport": 0.0,
        "StreamingTV": 0.0,
        "StreamingMovies": 0.0,
        "Contract": 0.0,
        "PaperlessBilling": 1.0,
        "PaymentMethod": 1.0,
        "MonthlyCharges": 70.5,
        "TotalCharges": 845.3
        }
    response = client.post("/predict/", json=payload)
    assert response.status_code == 422  # Espera erro de validação


def test_not_found():
    response = client.get("/nonexistent")
    assert response.status_code == 404


def test_wrong_method():
    response = client.get("/predict/")  # método GET em endpoint POST
    assert response.status_code == 405  # Method Not Allowed


def test_root_message():
    response = client.get("/")
    assert response.json() == {"message": "API de Churn Prediction ativa!"}
