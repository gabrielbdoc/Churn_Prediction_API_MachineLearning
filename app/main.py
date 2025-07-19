from fastapi import FastAPI
from app.schema import CustomerData
from app.predict import predict_churn

app = FastAPI(
    title="Churn Prediction API",
    description="API para prever se um cliente irá cancelar o serviço",
    version="1.0.0"
)


@app.get("/")
def root():
    return {"message": "API de Churn Prediction ativa!"}


@app.post("/predict/")
def predict(data: CustomerData):
    result = predict_churn(data)
    return {"churn": bool(result)}
